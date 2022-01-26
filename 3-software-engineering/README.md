# Software Engineering 101: Review Materials

As I was assembling this week's reading list, I wasn't able to find my ideal resource: a light overview of the steps from software design to deployment. Instead of having you read software engineering papers, I'm going to overview the software development life cycle and describe some resources for you to look at - this document is review material #1. 

Here's the rest of the materials first: 
1. RedHat video, Farming for the Future: https://www.youtube.com/watch?v=3YoboO1HO6k

2. The Digital Services Playbook: https://playbook.cio.gov/. Though some of the recommendations are specific to building goverment tools (e.g. language in Play 11 on security re: FEDRAMP), I think many of the recommendations are applicable to our work.

**Some example tools** I tried to pick papers that described *how* the tools are built and covered topics you have each talked about. Pick ONE or TWO from this list, OR, find something more appropriate for your discipline that details *how* the software was made:

1. Aquaculture farm management tool: https://dl.acm.org/doi/abs/10.1145/2835966.2836277?

2. Dairy herd management tool: https://onlinelibrary.wiley.com/doi/10.1002/spe.2704

3. Wireless dairy goat monitoring: https://dl.acm.org/doi/pdf/10.1145/3330180.3330182

4. Serveless farm management tool incl. smart contracts: https://dl.acm.org/doi/pdf/10.1145/3460866.3461770

5. Pest warning system for rice growers: https://dl.acm.org/doi/pdf/10.1145/2857218.2857271

6. Stored grain management and visualization system: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7120671

7. GHG Modeling Tool (COMET FARM): https://acsess.onlinelibrary.wiley.com/doi/abs/10.2134/agronmonogr59.c16

8. Mobile on-farm weather data collection tool: https://www.mdpi.com/2073-4433/11/9/902

## A brief overview of the Software Development Life Cycle (SDLC) for agricultural researchers
Author: @sudokita, Ankita Raturi

The SDLC is a set of defined stages in software engineering to move from an idea to a software product. You may be familiar with the high-level headings of the engineering process from other engineering design classes. These phases, though described as separate portions of work, often overlap, and especially as folks developing software in the research space, you may find yourself jumping around in the development life cycle depending on priorities, funding availability, skills, and other factors. Still, I think it's useful to have an idea of what each of the phases are and what tasks you may need to do in each of them. Consider this as modules of a development roadmap.

Software Engineering as a discipline often deals with helping teams of people build a one or more products togehter. These are often costly ventures, with lots of moving parts. On the other hand, you're probably building out your software alone, or as part of a small research group. Nevertheless, there are techniques from the discipline of Software Engineering that we can apply, in the small, in our own programming efforts.

Let's assume that you have an idea for a digital technology. Now what?

The SDLC has four major steps (depending on how you slice them):

1. Requirements Gathering: Decide on what you are going to build via user research, domain understanding, articulating your scope and goal.
2. Software Design and Architecture: Exploring the problem and solution space, coming up with a plan. Decide on how the software will be structured (incl. user interface, models, databases, and other components)
3. Software Implementation: Pick a language and build it, that is, preparing data, writing code, integrating features, deployment. Bug hunting and user testing. Did you build what you said you were going to? Identify areas to work on next.
4. Public Release & Maintenance: go live! Make it publicly accessible, and make a plan for how to keep it alive, especially as things break and evolve. Then, update it, fix bug, implement new features, provide user support. If needed, make a transition plan (who's going to take care of it next?).

You will not build ONE LARGE SOFTWARE all at once. Instead you will likely do phase 1 to identify a minimal set of features you think your users want. You'll then go through all the phases and likely iterate through the process. This approach is known as the iterative software development paradigm and it does what it says on the box - loop through the steps, incrementally adding complexity, features, reducing bugs, and increasing robustness. Learn more about spiral/iterative software development in the original Barry Boehm "Computer" article available at: [https://ieeexplore.ieee.org/abstract/document/59](https://ieeexplore.ieee.org/abstract/document/59).

![Spiral Model by Barry Boehm](https://upload.wikimedia.org/wikipedia/commons/3/33/Spiral_model_%28Boehm%2C_1988%29.png)

Image Source: Spiral Model by B.W. Boehm, 1988. Conny [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/), via Wikimedia Commons

Here are some additional recommendations I have for using a Spiral/Iterative SDLC:

1. Conduct user research first, and use this to guide the rest of our development. You can always check back in with users later too (in fact I strongly recommend testing with users early and often), but, consider your user research as a way of establishing your scope and workspace.
2. Design and architecture is where you need to make your next set of major decisions. Once you have an idea of what you want to build, I like to create a set of mockups to lay out what the design of my application is going to be. If you have a critical algorithm to implement, you will likely want to get this done here too. From this point on, you've likely settled on an overall structure for your application and then just want to think abut how to eat the elephant.
3. After you have identified your core features, divide up your proposed timeline into manageable chunks. Whether it's 2 weeks or 5. Pick something that is short enough that you have a milestone that you can check in with your collaborators. 
4. Identify a set of features you want to implement together, chunk them, and do them together during one "cycle" through implementation->testing->deployment->maintenance. Come back and loop through this. This allows for you to always have a "working product" at the end of each cycle :)

This is a rough overview, but should give you somewhere to begin. Let's go through the phases in a bit more detail. I'll provide links to external resources.


## Phase 1: Requirements Gathering
In this phase, you are primarily concerned with outlining a set of specifications for the software that you intend to build. 

1. **User Research:** Whether you are a single developer, or a large software engineering team, good user research is key to building something that people actually want! Methods for gathering requirements include interviews, focus groups, mapping the technology landscape, literature reviews, and more. We'll talk a bit more about user research next week when we look at Human-Computer Interaction, since that discipline offers methods for understanding your users (i.e., conducting user research) and translating your understanding into a specification of what you will build.

2. **Specification Documents**: These are common for large-scale software of significant complexity. Consider the develpoment of software for Medicare and Medicaid Services (CMS). If you're a contractor interested in building tools for the government, in this case for the CMS IT team, you need to utilize their [formal framework](https://www.cms.gov/research-statistics-data-and-systems/cms-information-technology/tlc). Here's an example [requirements document](https://www.cms.gov/Research-Statistics-Data-and-Systems/CMS-Information-Technology/TLC/Downloads/Requirements-Document.docx), provided by CMS as a template. It is a nice example of a formal requirements specification document. It details many aspect of the software to be built before a line of code is written. This allows for all stakeholders to agree on what is to be built up front, including estimating time effort and cost. 

But, you're an agricultural researcher, developing software as part of your dissertation, education, or as a prototype of an idea for future work. Some recommendations for this phase:

1. You don't need a formal specification, but you **SHOULD** specify what your Minimal Viable Product (MVP) is! This allows for you to develop a clear idea of what functionality you will need to implement, data to collect, what you'd like your intended user to achieve by using your tool, whether it's a mobile app or just a set of data visualizations.
2. Last semester, we looked at a few techniques for how to begin the process of going from idea to wireframes. Think back to examples like [Lab 1.2](https://github.com/ag-informatics/ag-informatics-course/tree/main/module1/lab1.2) and the subsequent sketching and design methods.
3. Create a "light" specifications document. That is a document that outlines the key functionality that you think your users want, that you will implement in your MVP i.e., your first prototype of the software. Include considerations for the next phase, and treat this more as a living document that you update over time. 
4. Create a timeline that allows you to estimate how long each chunks of functionality are going to take. You will iterate over this in the next phase, and will get better at estimating time effort (and eventually cost) the more you do this :).

## Phase 2: Software Design & Architecture

When you get to this phase, you know WHAT your going to build. You're goal is to determine HOW it will be built. So, your core tasks will really depend on what you're building. Consider some examples:

- Web App? Need to design the user interface, through the overarching software architecture will likely be something like what we see in Django, where the model and the view are separated. Using data not collected by user input? You'll need to think through the design of your data collection/aggregation scripts. 
- IoT App? Need to design the data pipeline. How will data move from point of data collection (e.g., water sensor) to being visualized for the user (e.g., graph on a dashboard). If the data collection tool doesn't exist, you may need to build this dipping your feet into design of a microcontroller or sensor. If the data collection tool exists, you can focus on data aggregation, cleaning, and how you will serve it to the front end. You will likely want this pipeline automated so that you're not manually cleaning data as it's collected in-situ.
- Mobile App? Additional considerations for data usage, whether your app needs to function offline, user interface constaints etc. If you want it to work on a computer as well, you might actually be thinking of a "responsive web app" and not a true mobile app for IOS or Android. 

Here's an overview of [web application architectures](https://docs.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures). Though they focus on the Microsoft .NET framework, it provides a nice introduction to the topic + overview. Another quick/useful read is this list of [architectural principles](https://docs.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/architectural-principles) that apply beyond the Microsoft ecosystem (the article is actually a synthesis of common design principles that are taught in software engineering classes across the world).

Some additional recommendations for this phase:

1. Pick your programming language(s). Since you are new to programming, it will be more helpful for you to constrain your design and architectural choices. That is, your software architecture is most likely going to be dictated by the language you use or domain constraints. For example, if you're building a django web app, you're going to use the model-view-template architecture, becuase that's how it's built. 
2. Create a high-level box-and-arrow diagram to serve as your software architecture diagram. It should desribe the major components of your proposed software. This allows you to have an idea of what the large efforts are going to be and how the pieces connect.
2. Create a set of wireframes that describe every major screen you plan to implement. This will give you a concrete sense of what you need to build. Add this to your living specification document as you are adding another layer of detail.
3. For each type of data you need to use, whether it's data you are producing or data that is coming from a third-party (e.g., USDA), determine: how you are going to collect, process, and serve the data. Add this to your spec doc! If you have complex data sharing restrictions, you may benefit from creating a [data management plan](https://purr.purdue.edu/dmp).
4. Figure out how you are going to [license your software](https://tldrlegal.com/). Chances are you may want to "open source" your research project for others to use and learn from. Whatever path you and your collaborators choose, I find it helpful to have this discussion up front, as you are still designing the software so that you can work within the boundaries of whatever license you choose. For example, if you are building a closed-source project, there are some libraries that have open-source licenses that you would not be able to use, or may need to adhere to the restrictions. 


## Phase 3: Software Implementation

In addition to actually writing the code, you will want to do things like debug/test different pieces of it, deploy it to a web server (so you're not just saving that to the end), and update your documentation. 

My recommendations for this phase:

1. **Version Control:** If you are writing any code. Even if it's just a snippet, I cannot stress this enough, use version control, like git. You can use a private repository to begin, but at least you are getting the benefit of your code versions being saved. Popular products include: Github, Gitlab, and Bitbucket. 

2. **Project Management:** Make sure that you don't let your project specification wither. Convert it into a format that actively encourages you to keep track of what's been built, what remains, document open issues, and track your progress. People usually use a bugtracker, whether it's integrated into your version control system, or is a separate tool is up to you. This is a useful way of keeping track of all the moving parts. It doesn't matter what tool you use, just pick something you will *actually* use, and that helps you communicate with your collaborators. Some tool suggestions:

	- If you're already using github, you can use the github "issues" feature: https://github.com/features/issues/. You break down your features into specific tasks and track progress, problems in there. 
	- "Kanban" boards are a simple way of trackign tasks. You have three columns: todo, in progress, and done. And you simply move post-it notes, virtual stickies, whatever, from column to column as you make progress. Trello, a todo tracking tool has a [KanBan templates](https://trello.com/templates/engineering/kanban-template-LGHXvZNL). So does [Miro](https://miro.com/kanban/), the digital whiteboard I use in class.
	- Airtable is another tool that offers a range of [project management templates](https://www.airtable.com/templates/product-design-and-ux). For example, check out the [Product Roadmap Template](https://www.airtable.com/templates/product-design-and-ux/exphVKuL99S35ZsMi/product-roadmap).

3. **Deployment:** Don't wait till you've finished building your entire project to try deploying to the web. Test the waters, try it out with your initial skeleton, make sure you understand how to go from git -> your computer -> web server, or whatever stack it is you have. Since I've been hearing lots of questions around how to go from building something on your computer, to having a hosted web application, I figured I'd focus a bit on deployment. **If you have other questions, let me know in the discussion and I'll update this document.** Here are a selection of tutorials that cover web application development, including, deploying to a cloud server. I suggest that, if you haven't already, try a couple of these out. Alternatively, depending on what you are building, find an analogous tutorial that includes that crucial step of deploying to a web server. 

	- Mozilla Foundation's Django Web Tutorial. If you took my previous course, you may recognize some of the early parts of this, but we didn't cover parts 6-11, which includes things like user authentication, testing, and deployment. Find it here: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django The Deployment section includes instructions for using Heroku, an excellent webhost.

	- Amazon AWS tutorial to build a "hello world" web application using NodeJS (Javascript). I would only recommend this if you know that you will be using AWS infrastructure for your project, since it focuses on, AWS tech! They say it only takes 30 minutes, so if you just want to take a peek into this world, it might not be too big a deal: https://aws.amazon.com/getting-started/guides/deploy-webapp-elb/. More options here: https://aws.amazon.com/getting-started/

	- Here's a Microsoft Azure example that uses Django as well: https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-django. There are links to many other tutorials in the sidebar, so you can pick whatever is most relevant to your needs.

	- Check out this tutorial on deploying a web app on Digital Ocean (I use this webhost): https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3 Note, it does use Flask, a lightweight python web framework, not unlike Django.


4. **Testing:** There are a couple of different types of testing you will want to do. For instance: user testing to find usability issues, debugging to fix programming errors, code review to make sure you don't accidentally have any passwords or keys visible, some automated testing to make sure your program produces expected outputs, and so on. The exact forms of testing you will need to do, again, will depend on what you're building. Here's some resources to get you going:

	- A nice little overview of debugging techniques: https://www.cs.cornell.edu/courses/cs312/2006fa/lectures/lec26.html This should help with run of the mill bug hunting.
	-  The [Nielsen Norman Group here](https://www.nngroup.com/articles/usability-testing-101/) has an excellent introduction to usability testing. Usability.gov also describes [usability evaluation methods here](https://www.usability.gov/how-to-and-tools/methods/usability-evaluation/index.html), including [an overview of user-focused techniques](https://www.usability.gov/how-to-and-tools/methods/running-usability-tests.html) provides a nice overview of techniques available. Given the domain-dependence of your software, you may want to consider doing "expert reviews" as well where you have a group of experts test out your tool. 
	- Many programming languages come with what's known as a "Unit testing suite" that allows you to write test cases to run your code against. For example, here is info about the [Django Unit Tests](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/), and here's a tutorial on [unit testing in python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python/). Unit testing is an excellent way to programmatically test your code for things like validation errors, data type mismatches, out-of-bounds errors.
	- When in doubt, print it out. When I'm stuck with my code two approaches have proven useful. 1) Insert a print statement and force my code to spit out the value(s) on the screen, for example in the middle of a loop, so that I can see if it's processing correctly. 2) Literally print out the coe on paper and proof-read it like a paper, working through the logic of the algorithm side-by-side to find my bugs.

## Phase 4: Maintenance
Though this phase is listed at the end, I strongly recommend you see these are ongoing practices - especially keeping documentation. 

1. **Open Source:** If you chose to open source your work, your may want to go through the entire codebase again ensuring that you are set up correctly. Here's a primer that I recently came across, by [Github](https://lab.github.com/githubtraining/create-an-open-source-program). 
2. **Documentation:** Keeping good documentation is always easier said than done, since once you're in the thick of development it can get overwhelming to have to document everything. Still, creating a good system for keeping this up can help. There are a couple of types of documentation you will want to maintain:

	- Remember your specification document that you were tracking in issues? That can serve as a good framework for your documentation. It has your major components and features and design considerations. Keep it up to date as things change.
	- In-line comments are your friend. Comment your code, explaining what functions are doing, where data is coming from, and if you're feeling bold, keeping a "changelog" of major changes you've made since the last time you updated a file. 
	- Project-level documentation that describes how things are built, any external libraries or packages being used. If you're software is developer facing, you can include, for instance, documentation on how to access your API here.
	- User-facing documentation. Once you've built your MVP you can start iterating on your user documentation to help people understand how to use your tool. While a good tool is intuititve, good documentation can serve as a helpful bridge.


# Moderator's Discussion Brief
Author: 

GitHub: 

## Overview of the Topic

 

## Short Synopsis of Materials


## Summary of Key Takeways from the Materials




## Discussion Questions



## Further Resources



## Discussion Notes and Feedback