Title: Two ways to write a simple navbar
Date: 2015-07-01 13:18:57
Tags: css, html
Category: web
Slug: two-ways-to-write-simple-navbar
Author: Sting
Summary: CSS to style a simple navbar.

html如下：

```html
<div class="navbar">
	<ul class="nav">
		<li class="nav-item"><a class="nav-link" href="">Home</a></li>
		<li class="nav-item"><a class="nav-link" href="">Home</a></li>
		<li class="nav-item"><a class="nav-link" href="">Home</a></li>
		<li class="nav-item"><a class="nav-link" href="">Home</a></li>
		<li class="nav-item"><a class="nav-link" href="">Home</a></li>
	  </ul>
</div>
```

### 使用inline-block

css is as following:

```css
body {
	width: 960px;
	margin: 0 auto;
}
.navbar {
	background: red;
}
ul.nav {
	width: 100%;
	display: inline-block;
	list-style: none;
	margin: 0;
	padding: 0;
}
.nav-item {
	display: inline-block;
	border-right: 1px solid #fff;
}
a.nav-link {
	display: block;
	color: #fff;
	text-decoration: none;
	text-align: center;
	width: 50px;
	font-size: 16px;
	line-height: 1.4;
}
a.nav-link:hover {
	color: #000;
	background-color: #fff;
}
```
用inline-block的问题是，在每个li之间，会多一点莫名其妙的空白。解决方法是把html里li写成这样:

```html
<li class="nav-item"><a class="nav-link" href="">Home</a></li
><li class="nav-item"><a class="nav-link" href="">Home</a></li
><li class="nav-item"><a class="nav-link" href="">Home</a></li>
```

或者让所有的li都在一行。

### 使用float

css如下：

```css
body {
	width: 960px;
	margin: 0 auto;
}
.navbar {
	background: red;
}
ul.nav {
	width: 100%;
	list-style: none;
	margin: 0;
	padding: 0;
	float: left;
}
.nav-item {
	border-right: 1px solid #fff;
	float: left;
}
a.nav-link {
	display: block;
	color: #fff;
	text-decoration: none;
	text-align: center;
	width: 80px;
	font-size: 16px;
	line-height: 1.4;
	padding: 5px 8px;
}
a.nav-link:hover {
	color: #000;
	background-color: #fff;
}
```

因为用了float，所以div.navbar并不占用整个文本流，所以需要在.navbar关闭之前加上clear。现在流行的方法是给div.navbar加个.clearfix类，然后.clearfix代码如下：

```css
.clearfix:after {
	content: ".";
	visibility: hidden;
	display: block;
	height: 0;
	clear: both;
}
```
