Title: Teaching "Data cleaning"
Slug: teaching-data-cleaning
Date: 2015-01-29 13:51:43
Tags: teaching, python, programming
Category: python
Author: Olga Botvinnik
Lang: en
Summary: 
	Our compute cluster is down for maintenance, so obviously instead of working on my advancement exam presentation, I'm gonna write a blog post about teaching "data cleaning" to graduate students in UCSD's BIOM 262: "Quantitative Methods in Genetics" class, where I taught [Python](http://www.python.org/), [IPython Notebook](http://ipython.org/), and [pandas](http://pandas.pydata.org/), using [Software Carpentry](http://software-carpentry.org/) techniques for teaching technical skills.

Our compute cluster is down for maintenance, so obviously instead of working on my advancement exam presentation, I'm gonna write a blog post.

Today I taught a 1-hour lesson on "Cleaning data" for graduate students in UCSD's BIOM262: Quantitative Methods in Genetics class. Here is the [IPython notebook](http://nbviewer.ipython.org/gist/olgabot/edebccd736d051d8a1c7) that I used. While designing the lesson, I used concepts I learned from [Software Carpentry](http://software-carpentry.org/)'s [Training for instrutors](http://teaching.software-carpentry.org/), such as:

* Designing the lesson incrementally, so every step builds upon itself
* When designing a lesson, have the final task in mind and teach to that
* Being as clear as possible for each step

During the workshop, I again implemented things we learned in software carpentry, such as working in pairs and using stickie notes to indicate progress. Overall, I thought it went quite well, with students being engaged for most of the time. Here's the results of what went well and what could be improved.

## The Good

Here are some of the things I thought went well.

**Everyone worked in pairs**. Before we split into pairs, I surveyed the class to check for previous experience with [Python](http://www.python.org/), [IPython Notebook](http://ipython.org/), and [pandas](http://pandas.pydata.org/). Then, the person who has **less** experienc was the one who did all the typing (aka "driving" in pair-programming parlance), and the more experienced person wasn't allowed to type. We did this at the software carpentry training while doing a Github](https://github.com/) exercise. I paired with someone who was less experience with Github, and it was a good experience for me to have to sit on my hands and talk through every step. This was very useful because the more experienced person had to be explicit and describe every step, and the less experienced person automatically had a mentor to ask "dumb" questions to, without having to grab an instructor. An additional benefit is that when working in pairs, you're held more accountable, so you can't just do some exercises and then switch to your email or facebook, because your partner is right there.

**Used pink and blue stickies to show progress.** Pink was "still working" and blue was "done." This was helpful to be able to scan the room and get a sense of the progress. We used this at software carpentry as well, but it was definitely more helpful as an instructor than as a student, because you got an implicit sense of progress, without having to check in personally with everyone.

Here's what the students said they liked.

* In-class verbal feedback (everyone has to give one feedback, alternate good and bad, no repeats)
	* Working in pairs 
	* Hands-on activity
	* Cleanly organized
	* Could go at your own pace
	* My partner was very helpful!
	* Learned IPython
* Anonymous written feedback. All of these are direct quotes.
	* Thorough
	* Progressive - ideas built upon each other well
	* Paired activity
	* This was a great session - should have done this in the first week. Your tutorial was EXCELLENT. It would be nice to have this introduced earlier, in this manner. You're a great instructor. Great job and thank you!
	* Very nice. Work on IPython exercises.
	* Very well put together exercise, referenceable for the future
	* Very practical skills
	* Step by step instructions with logic very helpful
	* "Awesome worksheet, really well made. My favorite parts were the ones that made me think harder, so the worksheet could be even harder."
	* Good instructions on platform
	* Easy to follow
	* IPython format
	* Thanks for your patience! I liked the tutorial a lot! Using IPython is fun :)
	* The steps and instructions were clear and built on each other. I would be happy if all homework was set up in this way.

## The Bad

The instructions for getting set up with downloading an IPython notebook, and having to `cd` and navigate to that directory, and start up an IPython notebook were confusing and need to be rewritten or completely reworked. Maybe give them a `wget` or similar command? Then they'll be directly in that folder where the `.ipynb` was downloaded to, and don't have to do any navigation. This took up a good 15 minutes at the beginning, that could have been used on programming instead.

Windows was a much larger impediment than I thought. The first part of the lesson was performing Unix commands such as `head`, `tail`, `wc`, and searching for a command to count the number of columns in a file (ends up being either `awk` or a combo of `head` and `wc`). I didn't plan for this, or test the lesson on a Windows machine, but half the class was using Windows. So that's definitely something I will plan for in the future. I felt really bad.

Here's what the students said could be improved.

* In-class verbal feedback
	* Felt rushed for me
	* Show the results on my computer, as well as hands on
	* Hard to get started without the right programs
	* **too much help** in the instructions [This one took me off guard!]
	* Windows :(
	* No Memes :(
* Anonymous written feedback
	* Bad. Windows machines. Bad
	* Would be nice to work with genomics data
	* It's hard for me not to be the "driver"
	* Umm, too much feedback?
	* Hard to find equivalent commands for Windows on my own because I don't know how to parse through other people's tips and know which one will work or not. Not your fault though!
	* There should be resources and instructinos on how to make this applicable to our own work

## The Ugly

Windows :(
