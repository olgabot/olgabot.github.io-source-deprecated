Title: Bio-what?
Slug: bio-what
Date: 
Tags: science, bioinformatics
Category: science
Author: Olga Botvinnik
Lang: en
Summary: When I tell people I do "bioinformatics," the response is usually "bio-*what*?" And honestly, bioinformatics is hard to define even for people WITHIN the field. In this post I will describe what I see as the two main threads of bioinformatics.

When I tell people I do "bioinformatics," the response is usually "bio-*what*?" And honestly, bioinformatics is hard to define even for people WITHIN the field. In this post I will describe what I see as the two main threads of bioinformatics.

First of all, there's the issue of naming. To some people, "Computational Biology" is separate from "Bioinformatics," but two people rarely agree on exactly what constitutes one or the other. Secondly, our PhD program is named *"Bioinformatics and Systems Biology"*, and according to my friend on the systems biology side who worked in a Harvard lab during undergrad before coming to UC-San Diego, there's a huge difference between "East Coast Systems Biology" and "West Coast Systems Biology," even though I can't tell.

Secondly, there's a huge range of topics that consist of bioinformatics in one way or another. The way I see it, there's two main divisions: *"Classic Bioinformatics"* and *"Applied Bioinformatics."* These should be taken with a heavy grain of salt, as I am a newcomer to the Bioinformatics field. These are my opinions on the current state, not absolute truth. Additionally, these two "halves" are symbiotic, and need each other to sustain life.

## Classic Bioinformatics

This is where it all started. It used to be that when people thought of bioinformatics, they thought of comparing sequences. A few years ago I read a blog post that stated "All of bioinformatics is essentially `strcmp` [string compare]," which made my blood boil because the subtleties of comparing these strings requires sophisticated algorithms to account for gaps, substitutions, and repetitive regions. Most of the tools below are analyzing strings or 

The focus here is to make sense and organize what we have of biological data into organized data structures.

These are the algorithms and tools that we learn in our first-year graduate school classes, like:

- [De Bruijn graphs for genome assembly](http://www.pnas.org/content/98/17/9748.full)
- [Genome rearrangements and sorting by reversals](http://dl.acm.org/citation.cfm?id=586673)
- [Smith-Waterman local alignment of sequences](http://en.wikipedia.org/wiki/Smith%E2%80%93Waterman_algorithm)
- [Needleman-Wunsch global alignment of sequences](http://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Burrows-Wheeler transform for aligning reads to the genome](http://genomebiology.com/2009/10/3/R25)
- [Maximum Entropy determination of splice site strengths](http://genes.mit.edu/burgelab/maxent/Xmaxentscan_scoreseq.html)
- [*k*-mer counting and filtering](https://github.com/ged-lab/khmer)
- [Hidden Markov Models for genome and protein structure and domain prediction](http://www.nature.com/nbt/journal/v22/n10/pdf/nbt1004-1315.pdf)
- [Optimal leaf ordering for hierarchical clustering](http://www.psrg.csail.mit.edu/pubs/BarGifJaa-ismb01.pdf)
- [Mass spectrometry for proteomics](http://www.nature.com/nature/journal/v415/n6868/full/415180a.html)
- [Cyclic peptide sequencing by mass spectrometry](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3398611/)

I see this as *Computer science applied to biology.*

## Applied Bioinformatics

This is where we are now. This is closer to what I do on a daily basis. Honestly, I don't build any of the algorithms above, but I do need to understand them to know where my data is coming from.

Honestly, the skills I learned in my classes was a good basis for the broad field of biology, but I barely use them on a day-to-day basis. Mostly I 

The focus here is to attribute *biological function* to data.

- [Bayesian network inference](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0030129)
- [Network flow]()
- []()

I see this as *Data science applied to biology.* These require the output of the *"Classic Bioinformatics"* tools, and use statistics, machine learning, and other applied tools to extract information.

## Classic vs Applied and Awards by the ISCB

What's interesting is that this division is especially evident in the awardees of the [International Society of Computational Biology](http://www.iscb.org/) (ISCB), where the Overton awards to early-career scientists tend to be more "Applied," and the Senior Scientist tend to be more "Classic."

As I am human, I certainly may have missed a paper or two that pushed one person into one of the other categories, and I am happy to correct any errors.

### Overton Award (Early-career)

- [2015: Applied] [Curtis Huttenhower](http://www.iscb.org/iscb-awards/2383)
	- [Applied] Justification: [Functional maps of the human genome](http://www.ncbi.nlm.nih.gov/pubmed/19246570?dopt=Abstract) Analysis of large-scale microbiome datasets
- [2014] [Dana Pe'er](http://www.iscb.org/iscb-awards/2225)
	- [Applied] Justification: [Inferring subnetworks from perturbed expression profiles using Bayesian Networks](http://bioinformatics.oxfordjournals.org/content/17/suppl_1/S215.full.pdf)
- [2013] [Goncalo Abecasis](http://www.iscb.org/iscb-awards/1837)
	- [Classic] Justification: [Quantitative Test Loci in nuclear families](http://www.sciencedirect.com/science/article/pii/S0002929707622538), [Gene flow trees](http://www.nature.com/ng/journal/v30/n1/full/ng786.html), [Sequence Alignment Map (SAM) format](http://bioinformatics.oxfordjournals.org/content/25/16/2078.short)
- [2012] [Ziv Bar-Joseph](http://www.iscb.org/iscb-awards/1224)
	- [Classic] Justification: [Optimal Leaf Ordering](http://www.psrg.csail.mit.edu/pubs/BarGifJaa-ismb01.pdf), [Maximal Independent Sets in *Drosophila* development](http://www.sciencemag.org/content/331/6014/183)
- [2011] [Olga Troyanskaya](http://www.iscb.org/iscb-awards/1117)
	- [Applied] Justification: [Missing value imputation for microarrays](http://bioinformatics.oxfordjournals.org/content/17/6/520.full.pdf), [A Bayesian framework for combining heterogeneous data sources for gene function prediction (in Saccharomyces cerevisiae)](http://www.pnas.org/content/100/14/8348.long)
- [2010] [Steven E. Brenner]()
- [2009] [Trey Ideker]()
- [2008] [Aviv Regev]()
- [2007] [Eran Segal]()
- [2006] [Mathieu Blanchette]()
- [2005] [Ewan Birney]()
- [2004] [Uri Alon]()
- [2003] [Jim Kent]()
- [2002] [David Baker]()
- [2001] [Christopher B. Burge]()


### Senior Scientist Accomplishment Prize

- [2015] [Cyrus Chothia]()
- [2014] [Gene Myers](http://www.iscb.org/iscb-awards/2224)
	- [Classic] Justification: [BLAST aka Basic Local Alignment Search Tool](http://www.ncbi.nlm.nih.gov/pubmed/2231712?dopt=Citation)
- [2013] [David Eisenberg]()
- [2012] [Gunnar von Heijne]()
- [2011] [Michael Ashburner]()
- [2010] [Chris Sander]()
- [2009] [Webb Miller]()
- [2008] [David Haussler]()
- [2007] [Temple Smith]()
- [2006] [Michael Waterman]()
- [2005] [Janet Thornton]()
- [2004] [David Lipman]()
- [2003] [David Sankoff ]()