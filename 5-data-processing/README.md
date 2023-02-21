# Data Processing

## The Data Processing Lifecycle
Even if you took my class last semester, please review Lecture 2.1 that introduces the data life cycle. This supplements the Data Acquisition module, and sets up to dig into data processing in this module.

Brief Review: www.aginformaticslab.org/ag-informatics-course/module2/lecture2.1.html

## Note on the O'Reilly Links in this document
We have access to the O'Reilly library via Purdue, so make sure you put in your Purdue email address and use Boilerkey to access the materials.


## Intro to Tidy Data

**EVERYONE READ** this introduction to the concept of "tidy data". Though it was initially implemented in R, this paper overviews how and why we need to clean up data to make it easy to work with: https://www.jstatsoft.org/article/view/v059i10. The lessons learned here will port to any language, though you may have to find analogous functions. If you're interested in a more code-heavy version of the paper you can [optionally check this out](https://tidyr.tidyverse.org/articles/tidy-data.html). 

Note: If you are using python, pandas should provide much of what you need. Tools like openRefine also provide appropriate support.

## Data Processing
The goal of data processing is to clean, structure, and prep the data for use. In this section, I've gathered a few resources with varying levels of complexity for you to review, depending on where in your data processing journey you are.

As helpfully described in the introduction of the [Data Carpentry Lesson on Data Organization in Spreadsheets](https://datacarpentry.org/spreadsheet-ecology-lesson/):

> "Much of your time as a researcher will be spent in the initial ‘data wrangling’ stage, where you need to organize the data to perform a proper analysis later. It’s not the most fun, but it is necessary. In this lesson you will learn how to think about data organization and some practices for more effective data wrangling. With this approach you can better format current data and plan new data collection so less data wrangling is needed."

**PICK ONE** of the following resources to review. You don't have to actually do the entire tutorial/lesson/chapter, but review the basics so that (a) during the class discussion you can share lessons applicable to your work, and (b) you can come back later and use the guidance in your own data processing work. 

1. **Want the basics on how to organize data in spreadsheets?**Review [Data Carpentry Lesson on Data Organization in Spreadsheets](https://datacarpentry.org/spreadsheet-ecology-lesson/): They provide some excellent guidance on how to approach your tabular data in a way that sets you up to analyze it more easily down the line. Be sure to look through all 6 components linked in the "Schedule" section. 
	- Want something a little more advanced? Review this chapter on Tabular Formats: https://learning.oreilly.com/library/view/cleaning-data-for/9781801071291/Text/Chapter_1.xhtml#_idParaDest-21 

2. **Figuring out exactly what to "clean"?** Review this practical guide on how to detect issues with your data, AKA "Anomaly Detection", using python: https://learning.oreilly.com/library/view/cleaning-data-for/9781801071291/Text/Chapter_4.xhtml#_idParaDest-104. Topics include how to find missing data, miscoded data, sentinels, outliers, and more!

3. **Looking for low-code support on data cleaning?** Review this lesson on using the open source tool OpenRefine: Data Carpentry Lesson on Data Cleaning with OpenRefine: https://datacarpentry.org/OpenRefine-ecology-lesson/. It is a followup from the previous lesson shared on spreadsheet data organization.


# Topic Submission

In this week's submission, you will describe how and why you need to clean data! In **<1 page**, please answer the following questions:


1. Describe a messy data set from your research? Write less than 1 paragraph, and if available, give us a snapshot!
2. What challenges will you face in cleaning this? 
3. If applicable, how have you previously handled this sort of data? 
3. Consider writing up a quick outline of a proposed plan of action to clean your data using one of the methods described in the resources provided (or something similar that you think is more applicable to your work). 


# Moderator's Discussion Brief
Author: [name]
GitHub: [username]

## Overview of the topic

*insert 1-2 paragraphs here*

## Short Synopsis of Readings

*For each resource provided, create a <1 paragraph summary.]*

## Summary of Key Takeaways from the Materials

*4-5 key takeways, a few sentences to one paragraph each*

## Discussion Questions

*>4-5 questions*

## Further Resources

*>2-3 resources you'd like to share*


# Discussion Notes and Feedback
Note taker: [name]

[notes from the class discussion]


# FYI: Creating a Pull Request

*IMPORTANT:*

Before beginning your work ensure that you first create a "fork" from the course GitHub page. This creates a copy of the ag-informatics-seminar course content onto *your* GitHub repository. From this point you should git clone this repository onto your device and proceed by making edits to the desired file in that location. Below are three YouTube videos that I found helpful when learning how to create a pull request, additionally I also encountered some issues when using Terminal git commands and was able to fairly easily find solutions on stackoverflow.com . Let me know if you have any additional questions!

https://youtu.be/rgbCcBNZcdQ

https://youtu.be/npnfDwmHKhY

https://youtu.be/8A4TsoXJOs8
