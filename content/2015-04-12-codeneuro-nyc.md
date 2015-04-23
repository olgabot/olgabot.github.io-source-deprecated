Title: CodeNeuro NYC 2015
Date: 2015-04-12 22:21
Modified: 2015-04-22 22:21
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
from the outside! Check it out, plus some other photos I took from the conference:

<blockquote class="imgur-embed-pub" lang="en" data-id="a/q3c57"><a href="//imgur.com/a/q3c57">codeneuro nyc 2015</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>

(FYI If you want to look through all the tweets from the entire event, check out this [Storify](https://storify.com/yangbodu/codeneuro) board.)

The conference kicked off with some mingling and beer. I gravitated towards the three I knew people coming in to the conference, [Nick
Sofroniew](http://www.janelia.org/people/scientist/nick-sofroniew), with whom
I did an [undergrad summer program](http://www.janelia.org/student-programs/undergraduate-program#722) and invited me to talk, [Jeremy Freeman](http://www.jeremyfreeman.net/), the main organizer of
the whole freakin' thing, and [Ben
Sussman](https://twitter.com/bensussman), who co-taught the `gitgoing`
tutorial with me and is an all-around awesome person. But the space was rad,
we had a balcony and a nice view of the city, and I got to meet a bunch of
people doing super interesting things in neuroscience.

<blockquote class="twitter-tweet" lang="en"><p>view from <a href="https://twitter.com/CodeNeuro">@CodeNeuro</a>... <a href="http://t.co/kInTbaFWHW">pic.twitter.com/kInTbaFWHW</a></p>&mdash; Angela Radulescu (@angitweets) <a href="https://twitter.com/angitweets/status/586659812198522880">April 10, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>


We got started with the talks, which we had three 10 minute (ish) talks, followed by a half hour (ish) break. It was a nice format that we could chat and break in between the talks not only to get a mental break but also discuss the concepts presented by the previous talks in the context of neuroscience. Here's all the talks:

1. Adam Packer (UCL): All optical recording and manipulation of individual neurons
2. Eiman Azim (Columbia): Quantitative behavior and mouse genetics for probing motor circuit function
3. Randal Burns (Johns Hopkins): Open Connectome project using CATMAID [[github repo](https://github.com/openconnectome/ocpcatmaid)]
4. Paco Nathan (Databricks): Spark for big data
5. Eliza Chang (The Data Incubator): PhD to Data Scientist
6. Michael Dewar (NYT): Real-time analytics on streaming data [[github repo for presentation](https://github.com/mikedewar/codeneuro_streamtools)] | [[github repo for `streamtools` package](https://github.com/nytlabs/streamtools)] 
7. Hilary Parker (Etsy): Data science at Etsy (+[cute statistical plushies](https://twitter.com/CodeNeuro/status/586696965502689280)!)
8. Brendan Lake (NYU): Teaching computers to scribble characters like humans
9. Olga Botvinnik, me! (UCSD): `flotilla`: An open-source Python package for iterative machine learning analyses [[slides](http://nbviewer.ipython.org/format/slides/gist/olgabot/2ee1087d74df46c842df#/)]

As you can imagine from the caliber of all the other talks, I was super nervous for mine! because I'm not doing things at exabyte scale, I'm not doing streaming data, and I'm not even doing neuroscience! I'm just analyzing static datasets with the usual machine learning algorithms. But as Jeremy pointed out, we need better tools for analyzing the existing non-big data datasets that we have, plus I got great questions and feedback from the talk which was great.

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

**Optogenetics**. This was a really interesting talk which uses [optogenetics](http://en.wikipedia.org/wiki/Optogenetics), which is a way that you can control the brain with light. Researchers genetically insert [rhodopsin](http://en.wikipedia.org/wiki/Rhodopsin), which is the light-sensitive protein that makes our eyes work, into neurons, which then makes them light sensitive. As a result, you can then turn specific neurons on and off with light! This talk used both this tool of optogenetics to stimulate/inhibit specific neurons, and calcium imaging to record their responses. 

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

Then, people split up about 50/50 for the tutorials and the hackathon.

### `gitgoing` tutorial

Then, Ben Sussman and I taught a tutorial called
[gitgoing](https://github.com/CodeNeuro/gitgoing) to quickly teach scientists
the version control system
[`git`](http://en.wikipedia.org/wiki/Git_%28software%29) and code testing via
[`py.test`](http://pytest.org/) and integration systems via [Travis-CI](https://travis-ci.org/). We had about 20-30 attendees. The goal was to get the
scientists acquainted with common tools in open source software so that they
could contribute themselves. It was kind of like a mini [Software
Carpentry](http://software-carpentry.org/) workshop, but we assumed our target
audience had some coding experience, and we didn't take the time to explain
computer science fundamentals like variables, loops, flow control, etc.

Our class was structured exactly as laid out in the `README.md` file. First we
setup their computers so they had `git` and Python 2.7. This took about an hour
total to get everyone done. Some people finished faster and started moving on to
the `git` section. Then Ben did an awesome explanation of `git`, and I learned a
bunch of stuff! I didn't realize that when you `git clone` a repo, you're
getting ENTIRE history of the project, so that makes sense why downloading all
of [IPython](ipython.org)/[Jupyter](https://jupyter.org/) takes forever. It was
also a really helpful analogy to describe the entire repository as an "ocean of
code," and that a branch is a single window into that ocean. We also talked
about merge conflicts, and how they can be really easy to create if, say someone
renamed one of the arguments of a function, and someone else added an argument,
and then `git` doesn't know what to do anymore. They picked up on testing pretty
quickly, and someone asked "well `git` thinks it's okay, but how do you know
the code will run?" Which brought us directly to testing!

Next, I talked about testing and why it's important. I wrote some simple Python
code with functions like `mean_plus_one`, `std_plus_one`, and `cv` (coefficient
of variance). They were just slight variations on the true
[`numpy`](http://www.numpy.org/) functions so the learners couldn't just use the
`numpy` version. We looked at the test file, `test_gitgoing.py` which used
`py.test`'s fixtures, which take care of the `setUp` and `tearDown` methods that
some other testing frameworks have. We saw a simple example of fixtures, which
creates a 20x10 matrix of normally distributed random numbers. These could have
been set as integers, I just wanted to illustrate how you can create new
fixtures from existing ones.

```python
import numpy as np
import pytest

@pytest.fixture
def n_rows():
    return 20

@pytest.fixture
def n_cols():
    return 10

@pytest.fixture
def x_norm(n_rows, n_cols):
    return np.random.randn(n_rows, n_cols)
```

There is a commented out broken test in the repo which they had to fix, which was a great formative assessment because they had to use their newly formed `git` and testing knowledge to fix the test, commit the changes, make a branch of their "feature" fixing the test, pushing to the branch, and making a pull request to the master branch. It was really rewarding for the students to see their pull request on Github, and to see their commits on the network of contributors to the `gitgoing` repo.

We unfortunately didn't advertise the #gitgoing hashtag before the tutorial so we didn't get any live-tweets, but Ben and I mitigated this and took a picture afterwards:

<blockquote class="twitter-tweet" lang="en"><p><a href="https://twitter.com/hashtag/gitgoing?src=hash">#gitgoing</a> at <a href="https://twitter.com/CodeNeuro">@CodeNeuro</a>! Thanks <a href="https://twitter.com/bensussman">@bensussman</a> for being an awesome co-teacher and everyone for coming! <a href="http://t.co/l0BUhoeWja">pic.twitter.com/l0BUhoeWja</a></p>&mdash; Olga Botvinnik (@olgabot) <a href="https://twitter.com/olgabot/status/586980895397019650">April 11, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

### Spark tutorial

After the `gitgoing` tutorial we had a break and mingled. Then, I went to the Spark tutorial, taught by [Paco Nathan](http://liber118.com/pxn/) from [DataBricks](https://databricks.com/) (slides [here](http://training.databricks.com/workshop/dbc_intro.pdf)). I've seen Spark demos before but I haven't put in the time to play around with the tools, so this was a great way to get exposed!

I was a little late to the tutorial, so I missed the initial setup. I was handed a slip of paper with a url, username and password that was my personal login to the DataBricks cloud. Paco was doing a "preflight check" of explaining different Spark concepts before we dove in. The key things I took away were:

- **RDD**: Resilient Distributed Dataset. This is the core unit of a spark analysis, where you load in data, and use Spark to indicate that you want it to be parallelized.
- **`sc`**: "Spark context." This is the object that exists in all the Python library versions with Spark, and is the object that you will be using to create and operate on datasets. 

We used an IPython notebook-style [REPL](http://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) interface, which was really nice because we could see the output from our commands right away. We continued with learning how to:

1. Read text files and separate lines by tabs
2. Filter for the first word of the line to be `ERROR`
3. Get all the second words of the error lines
4. Find the errors that were caused by `"mysql"`.

You can see a summary of my notes for this first section here:

```python
lines = sc.textFile("/mnt/paco/intro/error_log.txt") \
  .map(lambda x: x.split("\t"))
errors = lines.filter(lambda x: x[0] == "ERROR")
messages = errors.map(lambda x: x[1])
messages.filter(lambda x: x.find("mysql") > -1).count()

# At this point, the data is loaded into memory on the workers and you don't
# need to attack disk again, so this operation is very fast
messages.filter(lambda x: x.find("php") > -1).count()
```

Yay, we learned how to read files! Always good :)

The next part of the tutorial, we learned how to use `flatMap`, and then how to `join` several RDDs on their `(key, value)` pairs. After the break, we had a mini lecture about "Computational thinking" where we had to use what we learned so far to find all the instances of the word "Spark" in two files. If you're interested, you can see my full notes [here](https://gist.github.com/olgabot/ab058876b3bda6198f25).

### Hackathon

The hackathon was centered around the [neurofinder](http://codeneuro.org/neurofinder/) challenge, which is to try and extract neuronal signals from Calcium imaging data. The goals were go:

1. Refine a standardized API for "source extraction" algorithms, including input/ouptut formats
2. Work on evaluation metrics for algorithms and agree on ground truth definition
3. Work on incorporating existing algorithms into this API
4. Work on the frontend/backend of a website that would automatically run submitted algorithms on the test data, get the results and upload them to a leaderboard

First, everyone introduced themselves and the group organically split into a few groups: the website, API input/output formatting, implementing algorithms, and designing metrics.

The website team was composed of five people with web development frontend/backend experience. They generated some prototype websites and code **Jeremy/Nick: is there a link for the code here??**

Another group of about 25 worked on the API and the input/output formats, with their final notes added to [this wiki](https://github.com/CodeNeuro/neurofinder/wiki).

Another group of 10-20 split to work on incorporating existing algorithms in to this API. The rest worked on defining evaluation metrics for algorithms and the "ground truth" definitions of "what is a neuron" for these methods. They implemented some evaluation metrics, and developed an initial ground truth definition of manual centers and morphological boundaries. They discussed that this initial "ground truth" risks circularity, but is still a solid start.

There were still people working well into the evening!

<blockquote class="twitter-tweet" lang="en"><p>the codeneuro hardcore, still rocking! <a href="http://t.co/TyxmlSNOZB">pic.twitter.com/TyxmlSNOZB</a></p>&mdash; CodeNeuro (@CodeNeuro) <a href="https://twitter.com/CodeNeuro/status/587072775057231872">April 12, 2015</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Afterwards, we all hung out at a nice dinner:

![CodeNeuro after-dinner party](http://i.imgur.com/KY9smQR.jpg)

## Acknowledgements

Finally, I want to acknowledge all the organizers of the event:

- [Jeremy Freeman](http://jeremyfreeman.net)
- [Nick Sofroniew](https://twitter.com/neuro_nick)
- [Michael Broxton](http://graphics.stanford.edu/~broxton/)
- [Matt Conlen](http://www.mathisonian.com/)
- [Logan Grosenick](http://web.stanford.edu/~logang/)
- [Deep Ganguli](https://twitter.com/dgangul1)
- [Jeff Hammerbacher](https://twitter.com/hackingdata)

