Title: Django List and Detail View
Date: 2015-06-15 16:42:41
Tags: python, django
Category: django
Author: Sting
Slug: django-list-and-detail-view
Summary: Django ListView and DetailView example

开始学习Django的class based view。

最简单的是ListView和DetailView。

Model如下：

```python
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    category = models.ForeignKey("Category")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __unicode__(self):
        return self.title
```

第一个view是按category列出post，第二个view是post的detail view。

```python
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Post


class ViewPostByCategoryView(ListView):
    template_name = 'news/posts_by_category.html'
    paginate_by = 2

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.args[0])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(ViewPostByCategoryView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PostDetailView(DetailView):
    template_name = 'news/post.html'
    #queryset = Post.objects.all()
    model = Post

```

对于第一个view，因为要根据category来filter posts，所以覆盖了get_queryset方法。get_context_data方法是返回其他的context objects，比如说这里需要用到category的列表用来做菜单。

urls如下：

```python
from django.conf.urls import patterns, url

from .views import ViewPostByCategoryView, PostDetailView

urlpatterns = patterns('',
   url(r'category/(\d+)', ViewPostByCategoryView.as_view(), name='view_posts_by_category'),
   url(r'post/(?P<pk>\d+)', PostDetailView.as_view(), name='post_detail_view'),
   )

```

请注意第一个url里面的参数，会在view的get_queryset里用到(self.args[0])
第二个url里面要注明参数名为pk。

对于ListView，默认就有分页支持。只需要注明每页的记录数。

template如下：

posts_by_category.html

```html
{% raw %}
<ul>
  {% for category in categories %}
  <li><a href="{% url 'news:view_posts_by_category' category.id %}">{{category.name}}</a></li>
  {% endfor %}
</ul>

<ul>
  {% for post in object_list %}
  <li><a href="{% url 'news:post_detail_view' post.id %}">{{post.title}}</a></li>
  {% endfor %}
</ul>

{% if is_paginated %}
<nav>
  <ul class="pagination">
    {% if page_obj.has_previous %}
    <li>
      <a href="?page={{ page_obj.previous_page_number }}"> <span>Previous</span> </a>
    </li>
    {% else %}
    <li class="disabled"> <a href="#"> <span>Previous</span> </a> </li>
    {% endif %}
    {% for page in paginator.page_range %}
    <li {% if page == page_obj.number %}class="active"{% endif %}> <a href="?page={{ page }}">{{ page }}</a> </li>
    {% endfor %}
    {% if page_obj.has_next %}
    <li> <a href="?page={{ page_obj.next_page_number }}"> <span>Next</span> </a> </li>
    {% else %}
    <li {% if not page_obj.has_next %}class="disabled"{% endif %}> <a href="#"> <span>Next</span> </a> </li>
    {% endif %}
  </ul>
</nav>
{% endif %}
{% endraw %}
```

post.html

```html
{% raw %}
<h2>{{object.title}}</h2>
<p>{{object.created_at|date:'Y-m-d'}}</p>
<p>
{{object.content}}
</p>
{% endraw %}
```
