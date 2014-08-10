Title: PYTHONPATH is a liar. site.py and easy-install.pth tell the truth
Date: 2014-03-03 20:15:41
Author: sciencemeetproductivity
Category: text
Tags: pythonpath, python
Slug: 2014-03-03-pythonpath-is-a-liar-site-py-and-easy-install-pth-tell

Lately I've been working in [virtualenvs](http://www.virtualenv.org/en/latest/) which as been **great** for developing but not so great for installing. I've run into numerous issues where I prepend my `PYTHONPATH` with the directory I want to get imported first, but to no avail. You've run into this: you `export PYTHONPATH` exactly as you want, only to see that `import sys; sys.path` includes all kinds of other junk before it!

So, after watching a [talk](http://blip.tv/pycon-us-videos-2009-2010-2011/pycon-2011-reverse-engineering-ian-bicking-s-brain-inside-pip-and-virtualenv-4899496) about reverse-engineering `virtualenv`. I realized I actually don't understand anything about what python does at startup. So after a lot of searching, I found out that to load packages, Python reads the `site.py` file. I read about [`site.py`](http://docs.python.org/2/library/site.html). And I found out.....

**TURNS OUT PYTHON SECRETLY LOADS PACKAGES BEFORE LOOKING AT PYTHONPATH.**

![Shocking!](http://media0.giphy.com/media/aCpmM0W4tfG48/giphy.gif)

And where it looks is the `*.pth` files found in `path/to/python/lib/site-packages/*.pth`. The biggest culprit is usually `easy_-nstall.pth`. Mine had all kinds of absolute paths to the bigger Python install that I had to remove.

On my computer, `easy-install.pth` looks like this:

    import sys; sys.__plen = len(sys.path)
    ./pytz-2013.8-py2.7.egg
    ./brewer2mpl-1.3.2-py2.7.egg
    ./pybedtools-0.6.2-py2.7-macosx-10.9-x86_64.egg
    /Users/olga/workspace-git/pandas
    /Users/olga/workspace-git/prettyplotlib
    /Users/olga/workspace-git/statsmodels
    /Users/olga/workspace-git/seaborn
    ./husl-2.1.0-py2.7.egg
    /Users/olga/workspace-git/gffutils
    ./simplejson-3.3.1-py2.7-macosx-10.9-x86_64.egg
    ./argcomplete-0.6.5-py2.7.egg
    ./argh-0.23.3-py2.7.egg
    ./moss-0.2.0-py2.7.egg
    /Users/olga/workspace-git/scikit-learn
    /Users/olga/workspace-git/matplotlib/lib
    ./Theano-0.6.0-py2.7.egg
    ./pysam-0.7.7-py2.7-macosx-10.9-x86_64.egg
    /Users/olga/workspace-git/YeoLab/gscripts
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)
    
So let's say I never wanted to use my development versions of something, then I'd remove that line from the file. Although eventually this got so much of a problem in my `virtualenv` at work that at I added the `site-packages` directory of that python distribution indirectly with `./`:

    import sys; sys.__plen = len(sys.path)
    ./
    ./distribute-0.6.14-py2.7.egg
    /home/obotvinnik/workspace-git/gscripts
    /home/obotvinnik/workspace-git/rnaseqlib
    import sys; new=sys.path[sys.__plen:]; del sys.path[sys.__plen:]; p=getattr(sys,'__egginsert',0); sys.path[p:p]=new; sys.__egginsert = p+len(new)

Because I *always* wanted to import from the `virtualenv` FIRST and never look at any other packages if I could help it. 

I honestly don't know how kosher this is but it worked for me. Hope it helps you!
