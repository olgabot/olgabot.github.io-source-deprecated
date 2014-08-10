Title: The R script that will change your life
Date: 2013-05-03 10:01:30
Author: sciencemeetproductivity
Category: text
Tags: R, programming, Rprofile, automation, updating packages
Slug: 2013-05-03-the-r-script-that-will-change-your-life

If you use the [`R`](http://www.r-project.org/) programming language, you probably know how much of a pain it is to keep your packages updated. You've run `update.packages(...)` on the few that you want to keep up to date, but it's a pain in the neck to do that for every package, every time. Thankfully, where there's a will, there's a way!

When `R` starts up, it looks at your `.Rprofile` file (if you have one), and runs it. Mine looks like this:

    #!/usr/bin/Rscript
    
    options("repos"="http://cran.stat.ucla.edu/")
    library(utils)
    update.packages(ask = FALSE)
    my.packages = c("CvM2SL2Test", "MASS", "verification", "gtools", "ROCR",
    	    "RColorBrewer", "heatmap.plus", "gmodels", "gplots",
    	    "profr", "proftools",
    	    "colorRamps")
    to.download = which(!my.packages %in% rownames(installed.packages()))
    if( length(to.download) > 0){
        install.packages(my.packages[to.download], clean=TRUE, dependencies=TRUE)
    }

This script has three awesome features:

1. It will update ALL the packages I have without asking.
2. It has an A-list of packages that I always want to have.
3. It iterates over the A-list and makes sure they're updated.

It may be a little redundant, but having a few fail-safes never hurt anyone.

Feel free to steal this `.Rprofile` for your own usage.
