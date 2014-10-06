Title: No longer actively developing prettyplotlib
Slug: no-longer-actively-developing-prettyplotlib
Date: 2014-10-06 10:10:39
Tags: python, visualization, prettyplotlib, seaborn, flotilla
Category: software
Author: Olga Botvinnik
Lang: en
Summary: It is with heavy heart that I announce that I am no longer actively developing [`prettyplotlib`](https://github.com/olgabot/prettyplotlib). I just don't have the bandwidth available to do the project justice. It was a fantastic experience to bundle up that piece of code and share it with the world, and discover that there are many other people who want pretty plots. Over the last year, I discovered a much better visualization library in Python called [`seaborn`](https://github.com/mwaskom/seaborn), which is much more mature and covers more ground than `prettyplotlib` ever could. From working on [clustered heatmaps](https://github.com/mwaskom/seaborn/pull/230) on `seaborn`, I've become a much better Python program, and am forever grateful to [Michael Waskom](https://twitter.com/michaelwaskom) for creating it.

It is with heavy heart that I announce that I am no longer actively developing [`prettyplotlib`](https://github.com/olgabot/prettyplotlib). It was a fantastic experience to bundle up that piece of code and share it with the world, and discover that there are many other people who want pretty plots. Over the last year, I discovered a much better visualization library in Python called [`seaborn`](https://github.com/mwaskom/seaborn), which is much more mature and covers more ground than `prettyplotlib` ever could. From working on [clustered heatmaps](https://github.com/mwaskom/seaborn/pull/230) on `seaborn`, I've become a much better Python programmer, and am forever grateful to [Michael Waskom](https://twitter.com/michaelwaskom) for creating it.

Using `seaborn`, to get the `prettyplotlib` style, do:

    import seaborn as sns
    sns.set(style='ticks', palette='Set2')

And to remove "chartjunk", do:

    sns.despine()

If you have discrete pull requests, I will accept them, but I personally will no longer fix bugs.

Thank you to all the `prettyplotlib` users, especially [Phillip Guo](http://www.pgbovine.net/) for tweeting about it and setting off the publicity storm, and [all the contributors](https://github.com/olgabot/prettyplotlib/graphs/contributors) who took my measly code and made it great. I've learned so much from the Python open source community and am so thankful that it is so easy to learn from others in this wonderful environment.

If you want to check out what I've been working on instead, take a look at [`flotilla`](https://github.com/YeoLab/flotilla), the package I've been working on with [Michael Lovci](https://github.com/mlovci) for reproducible single-cell analysis. The package is still in its infancy (read: be prepared for bugs), and we are actively developing it!