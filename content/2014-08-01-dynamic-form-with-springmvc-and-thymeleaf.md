Title: Dynamic Form with SpringMVC and Thymeleaf
Date: 2014-08-01 10:50
Category: java
Tags: java, spring, thymeleaf
Author: Sting
Slug: dynamic-form-with-springmvc-and-thymeleaf
Summary: Dynamic form with springmvc and thymeleaf

## Requirements

SubjectGroup and SubjectGroupOption has one-to-many relationship. When adding a subject group, subject group options can be added inline.

## Things I’ve learned.

* When adding an option, don’t need to use javascript to handle the added html snippet. Just submit the add request to controller and handle the adding in the controller (Add a new options into the option list of subject group), then return to the add page. Spring mvc’s data binding and thyme leaf’s for loop will handle the html. (In EDC, I use javascript to append option html. It works. But there are some duplicate codes in JSP and javascript)
* Can use the same way to handle subject option removing.
* If there are multiple submit button in one form. We can use button’s name to separate them. In controller, use RequestMapping’s params to make the submit request to the right controller method.

## Code

SubjectGroupController.java

```java
package edc.web;

import edc.model.SubjectGroup;
import edc.model.SubjectGroupOption;
import edc.service.SubjectGroupService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@RequestMapping("/sg")
public class SubjectGroupController {
    private SubjectGroupService subjectGroupService;

    @Autowired
    public void setSubjectGroupService(SubjectGroupService subjectGroupService) {
        this.subjectGroupService = subjectGroupService;
    }

    @RequestMapping(value = "add")
    public String add(SubjectGroup subjectGroup) {
        return "subjectGroup/add";
    }

    @RequestMapping(value = "add", params = {"addOption"})
    public String addOption(SubjectGroup subjectGroup, BindingResult result) {
        subjectGroup.getOptions().add(new SubjectGroupOption());
        return "subjectGroup/add";
    }

    @RequestMapping(value = "add", method = RequestMethod.POST)
    public String save(SubjectGroup subjectGroup, BindingResult result) {
        this.subjectGroupService.save(subjectGroup);
        return "redirect:/sg/add";
    }
}

```

add.html

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="utf-8"/>
    <title></title>
</head>
<body>
<section>
    <h2>Add Subject Group</h2>
    <form action="#" th:action="@{/sg/add}" th:object="${subjectGroup}" method="POST">
      <p><input type="text" th:field="*{name}" placeholder="Name..."/></p>
        <h3>Options</h3>
        <button type="submit" name="addOption">Add Option</button>
        <table>
            <tr th:each="option, rowStat : *{options}">
              <td><input type="text" th:field="*{options[__${rowStat.index}__].label}" placeholder="Option..."/></td>
            </tr>
        </table>
        <button type="submit">Add</button>
    </form>
</section>
</body>
</html>
```
