Title: Succinct loop testing in Python
Date: 2013-11-21 11:00:54
Author: sciencemeetproductivity
Category: text
Tags: python, for loops, testing, data science
Slug: 2013-11-21-succinct-loop-testing-in-python

Since I'm a data scientist and all, my datasets can be too big to deal with when I'm initially testing an idea. So to test a for loop in Python with just a few examples, I used to do this kind of stuff:

    n = 0
    for thing in things:
        print thing
        n += 1
        if n > 10:
            break

But python's `zip` is smart in that it stops when the shortest item in the zip stops!

So you can do:

    for i, thing in zip(range(5), things):
        print thing

And it will only show you the first 5 things! And it's so succinct! This is especially pertinent when your `things` is a generator and you can't necessarily get the `len` of it.

Hope that helps you out! It saves me some headache, KeyboardInterrupts, and keystrokes.
