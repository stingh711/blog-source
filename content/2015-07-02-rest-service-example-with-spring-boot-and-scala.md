Title: Rest service by spring-boot and scala
Date: 2015-07-02 13:31:03
Tags: scala, rest, spring-boot
Category: scala
Slug: rest-service-by-spring-boot-and-scala
Author: Sting
Summary: Rest service by spring-boot and scala

I like spring-boot. I think it will be the future of java framework. Only a few files, you can setup a java micro service. You can even write all codes in groovy or scala.

This project is an example to use scala with spring-boot to provide a simple rest service. Comparing to java version, following issues need to be solved.

1. Spring's default message resolver cannot handle scala class. Need to register a new one.
1. When invoking java code from scala, need to do some convertion from scala's AnyVal to their relavant java object type and scala's collection to java's when passing parameters to java code.

Github repository is [Here](https://github.com/stingh711/spring-boot-jdbc-scala-example)
