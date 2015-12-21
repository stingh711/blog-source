Title: For loop in scala
Date: 2015-07-02 13:39:49
Tags: scala
Category: scala
Slug: for-loop-in-scala
Author: Sting
Summary: For loop in scala.

`for` in scala is more powerful than `for` in java. The basic usage is the same with java.

```scala
val names = List("Sting", "Ben", "Georte", "Jacky")
for (name <- names) {
  println(name)
}
```

You can have more control over the loop.

```scala
val names = List("Sting", "Ben", "George", "Jacky")
for (name <- names; if name.length > 3) {
  println(name)
}
```

You may even iterate more than one list.

```scala
for (i <- 1 to 10; j <- 11 to 20) {
    println(s"$i * $j")
}
```

Or

```scala
for (i <- 1 to 10; if i % 2 == 0; j <- 11 to 20; if j % 2 == 1) {
  println(s"$1 * $j")
}
```

If you are tied of \`;\`, it is also legal to use {} to replace ()

```scala
for {i <- 1 to 10
  if i % 2 == 0
  j <- 11 to 20
  if j % 2 == 1} {
  println(s"$i * $j")
}
```

Just like other expression in scala, `for` loop can have return value.

```scala
val names = List("Sting", "Ben", "George", "Jacky")
val filtered = for (name <- names; if name.length > 3) yield name
```

You may say map and filter can do the same thing, why should I still use `for` loop?

The answer is if you have more than one generator, `for` loop is more clear.

```scala
val numbers = for (i <- 1 to 10; if i % 2 == 0; j <- 11 to 20; if j % 2 == 1; if i * j < 200) yield (i * j)
```

`for` can also iterate map. Each element in the `for` loop is a (k, v) tuple.

```scala
val m = Map("sting" -> 30, "ben" -> 24, "george" -> 30)
for ((k, v) <- m) {
  println(k, v)
}
```
