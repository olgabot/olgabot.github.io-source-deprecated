Title: CodeNeuro NYC 2015
Date: 2015-04-12 22:21
Modified: 2015-04-12 22:21
Category: conferences
Tags: programming, conferences, bioinformatics, neuroscience
Slug: codeneuro-nyc-2015
Authors: Olga Botvinnik
Summary: Last weekend I attended the [CodeNeuro NYC](http://codeneuro.org/2015/NYC/) conference, which is a conference for neuroscientists, programmers, and everything in between. It was a unique experience because it had both the excitement and energy of a tech conference, and the pure, unadulterated zest for knowledge of a scientific conference.

Last weekend I attended the [CodeNeuro NYC](http://codeneuro.org/2015/NYC/)
conference, which is a conference for neuroscientists, programmers, and
everything in between. It was a unique experience because it had both the
excitement and energy of a tech conference, and the pure, unadulterated zest
for knowledge of a scientific conference.

## Day 1: Talks and panel

The first day of the conference started after the workday on Friday at 5pm at
the [New Museum](http://www.newmuseum.org/) in Little Italy, Manhattan, NYC.
This was the first time I'd been to this place and it was really awesome, even
from the outside! Check it out:

[photo of outside]

The conference kicked off with some mingling and beer (Pabst Blue Ribbon aka
PBR to be specific ... a little too bro-y/hipster-y for me personally so I
abstained. I *did* tell the organizers I would have appreciated some wine,
though :).

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/hashtag/PBR?src=hash">#PBR</a> a plenty <a href="https://twitter.com/CodeNeuro">@CodeNeuro</a> and we&#39;re ready to start! <a href="http://t.co/QpJ3nIYk2J">pic.twitter.com/QpJ3nIYk2J</a></p>&mdash; paco nathan (@pacoid) <a href="https://twitter.com/pacoid/status/586649963133853697">April 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

I only knew three people coming in to the conference, [Nick
Sofroniew](http://www.janelia.org/people/scientist/nick-sofroniew), with whom
I did an [undergrad summer program](http://www.janelia.org/student-programs/undergraduate-program#722) and put me in touch with the conference in the
first place, [Jeremy Freeman](http://www.jeremyfreeman.net/), who organized
the whole freakin' thing and invited me to give a talk and tutorial, and [Ben
Sussman](https://twitter.com/bensussman), who co-taught the `gitgoing`
tutorial with me and is an all-around awesome person. But the space was rad,
we had a balcony and a nice view of the city, and I got to meet a bunch of
people doing super interesting things in neuroscience.

<blockquote class="twitter-tweet" lang="en"><p>view from <a href="https://twitter.com/CodeNeuro">@CodeNeuro</a>... <a href="http://t.co/kInTbaFWHW">pic.twitter.com/kInTbaFWHW</a></p>&mdash; Angela Radulescu (@angitweets) <a href="https://twitter.com/angitweets/status/586659812198522880">April 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[photo collage/click through? of photos, mine plus curated from twitter from the event]

We got started with the talks, which we had three 10 minute (ish) talks, followed by a half hour (ish) break. It was a nice format that we could chat and break in between the talks not only to get a mental break but also discuss the concepts presented by the previous talks in the context of neuroscience. Here's all the talks:

1. Adam Packer (UCL)
2. Eiman Azim (Columbia): Using optogenetics to understand interneurons
3. Randal Burns (Johns Hopkins): Open Connectome project using CATMAID [[github repo](https://github.com/openconnectome/ocpcatmaid)]
4. Paco Nathan (Databricks): Spark for big data
5. Eliza Chang (The Data Incubator): 
6. Michael Dewar (NYT): Real-time analytics on streaming data [[github repo for presentation](https://github.com/mikedewar/codeneuro_streamtools)] | [[github repo for `streamtools` package](https://github.com/nytlabs/streamtools)] 
7. Hilary Parker (Etsy): Data science at Etsy (+cute statistical plushies!)
8. Brendan Lake (NYU): Teaching computers to scribble characters like humans
9. Olga Botvinnik, me! (UCSD): `flotilla`: An open-source Python package for iterative machine learning analyses [[slides](http://nbviewer.ipython.org/format/slides/gist/olgabot/2ee1087d74df46c842df#/)]

My top three favorite talks were:

**NYT R&D demo** This was a fantastic talk about streaming data analytics.  He
and his team had created an interactive way to analyze real-time data. They
had a GUI interface where you could select boxes that represented an action on
data ([extract, transform, load aka
ETL](http://en.wikipedia.org/wiki/Extract,_transform,_load)-like things), and
you could string these boxes together to create an analysis pipeline. It
reminded me a lot of the [Galaxy](https://usegalaxy.org/) interface for
reproducible bioinformatics pipelines. Check out the tweet below for a
screenshot:

<blockquote class="twitter-tweet" lang="en"><p>Picture of <a href="https://twitter.com/hashtag/realTimeData?src=hash">#realTimeData</a> including mine <a href="https://twitter.com/hashtag/codeNeuro?src=hash">#codeNeuro</a> <a href="http://t.co/VCIfFlFHTK">pic.twitter.com/VCIfFlFHTK</a></p>&mdash; aybuke turker (@aybuketurker) <a href="https://twitter.com/aybuketurker/status/586678871942111232">April 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Optogenetics**.

<blockquote class="twitter-tweet" lang="en"><p>A. Packer shows some amazing tools to simultaneously record + stimulate ensembles of neurons with <a href="https://twitter.com/hashtag/CaImaging?src=hash">#CaImaging</a> and <a href="https://twitter.com/hashtag/optogenetics?src=hash">#optogenetics</a>. <a href="https://twitter.com/hashtag/codeneuro?src=hash">#codeneuro</a></p>&mdash; Felipe Gerhard (@neuroflips) <a href="https://twitter.com/neuroflips/status/586685623068717056">April 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

**Spark**. This was an awesome talk by [Paco Nathan](http://liber118.com/pxn/)
on using big data tools. Paco had worked with both Hadoop and Spark and gave a
great overview of the history of Big Data (which he pinpointed to Q3 1997),
the different papers about it and tools for it, and where Spark fits in that
ecosystem. He gave a few use cases and was overall just a very entertaining
presenter.

<blockquote class="twitter-tweet" lang="en"><p>Great talk by <a href="https://twitter.com/placoid">@placoid</a> at <a href="https://twitter.com/CodeNeuro">@CodeNeuro</a> just now - apparently rotational bearings on planes create 12 exabytes of data / day... wow <a href="https://twitter.com/hashtag/bigdata?src=hash">#bigdata</a></p>&mdash; Alice Lloyd George (@AMLG23) <a href="https://twitter.com/AMLG23/status/586689726196883458">April 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
[The most retweeted talks?? Maybe a Storify of the @CodeNeuro account for April 10th 2015]

After all the talks, there was a panel led by Jeremy with some giants of
neuroscientists, Tony Movshon, Eve Marder and Larry Abbott. A recurring theme
was that the fundamental questions of how the brain works hasn't changed, but
the tools have drastically changed.

One story that stuck with me was Eve describing that when she was doing
experiments, she used an
[oscilloscope](http://en.wikipedia.org/wiki/Oscilloscope) to listen (yes, with
her ears! I thought this was amazing!) to the measurements from neurons, and
there was a direct, phsyical, visceral reaction that when you designed an
experiment and heard specific tones, you knew **exactly** what that meant,
because you were intimately familiar with the exact tones and sounds produced
by the device. But now, she said, the high throughput methods, while capable
of measuring many things at once, are so detached from the physicality of
neurons firing that she feels people aren't connected to what they're
measuring anymore. I found that interesting because in my field of RNA
biology, we'll do these newfangled [high-throughput sequencing
experiments](http://en.wikipedia.org/wiki/DNA_sequencing#Next-
generation_methods) to measure RNA expression as a proxy for protein
abundance, and study the [alternative
splicing](http://en.wikipedia.org/wiki/Alternative_splicing) of these RNA
transcripts, but every time, we always have to validate our findings using an
older, low-throughput method like [RT-PCR](http://en.wikipedia.org/wiki/Revers
e_transcription_polymerase_chain_reaction). I don't know what the equivalent
experiments are in neuroscience, because it seems all very magical to me that
they're able to manipulate individual neurons in mice, but I also wonder if
it's known that the neuron in the exact same position in one animal and
another animal, do the exact same thing. So far, biology has relied on laws of
averages, so if you do a high throughput experiment on a bunch of cells and
get an average signal, you should get that same result if you do a low-
throughput version of that experiment. I don't know what the equivalent of
that is in neuroscience, but it was refreshing to hear that neuro has its own
share of growing pains as its adopted its own high-throughput techniques, and
that biology wasn't the only one.

It was interesting to hear about the challenges of neuroscience, of how
excited people are about optogenetics, and how many people are apparently
skeptical of [functional magentic resonance
imaging](http://en.wikipedia.org/wiki/Functional_magnetic_resonance_imaging)
(fMRI) data, and how nobody knows what the [cerebral
cortex](http://en.wikipedia.org/wiki/Cerebral_cortex) does!


## Day 2: Tutorials + Hackathon

The next morning we were in the [New, Inc](http://www.newinc.org/) coworking
space, and started off with some kickass bagels and lox/salmon:

<blockquote class="twitter-tweet" lang="en"><p>breakfast begins <a href="http://t.co/55QljXZqkw">pic.twitter.com/55QljXZqkw</a></p>&mdash; CodeNeuro (@CodeNeuro) <a href="https://twitter.com/CodeNeuro/status/586893786212651008">April 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>




[Photo of everyone from dinner]
If you want to look through all the tweets from the entire event, check out this [Storify](https://storify.com/yangbodu/codeneuro) board.
