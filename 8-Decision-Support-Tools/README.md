# Decision Support Tools

> "Decision Support Tools are interactive software tools used by decision-makers to help answer questions, solve problems, and support or refute conclusions."

Source: [U.S. EPA, "Decision Support Tools - Development of a Screening Matrix for 20 Specific Software Tools"](https://frtr.gov/decisionsupport/PDF/DST%20Matrix%20Report.pdf) 

Two quick reads on decision support tools:

1. Beyond modelling: considering user-centred and post-development aspects to ensure the success of a decision support system: https://www.ahri.uwa.edu.au/publication/beyond-modelling-considering-user-centred-and-post-development-aspects-to-ensure-the-success-of-a-decision-support-system/

2. Bridging the gap between models and users: A lightweight mobile interface for optimized farming decisions in interactive modeling sessions: https://www.sciencedirect.com/science/article/pii/S0308521X21002687#bb0070https://www.sciencedirect.com/science/article/pii/S0308521X21002687#bb0070

# SUBMISSION

Your topic analysis this week is in two parts (2 pages max). The first half is related to this topic DSTs, the second, related to the ML to AI topic. You'll see this exact same text in both topics.

I want you to think about your own research in two ways, first, with respect to short term decision support, and second, with respect to longer term ML/AI applications.

1. Empowering users to make decisions: We've read a couple of papers that focus on the human-centered design of decision support tools. In the context of your work:
	- What are 3 knowledge-intensive decisions faced by people in your work?
	- What types of decision support tools, if any, are people already using?
	- What decision support tools do you think might be *actually useful* to the stakeholders of your work?

2. Imagining the future of ag tech: We watched a fairly techno-optimistic vision of the potential of machine learning in our current society. In the context of your work:
	- What is ONE challenge that may be solved/supported through ML solutions? Who are the main beneficiaries of this work? Are there any potential inequalities ML may create?
	- What are some of the challenges you may face in developing ML in your work?
	- How might you define "real" Artificial Intelligence in your work, or a "General Purpose" AI?


# Moderator's Discussion Brief
Author: Steven Doyle

GitHub: StevenDoylePurdue

## Overview of the Topic

Decision support systems (DSSs), or decision support tools (DSTs), are a broad category of tools whose purpose is to help users make key decisions by either providing them with information or predicting outcomes of different choices. In agriculture, DSSs are typically used by farmers to identify optimal crop and farm management choices. Tools can range from highly specialized pest management systems to general purpose, seed-to-harvest models. Additionally, DSSs can be as simple as printed worksheets requiring manual calculations or as complex as machine learning-assisted plant growth simulations. Common DSSs include Climate’s FieldView ((https://climate.com/)) and AgWorld’s suite of products ((https://www.agworld.com/us/)). 


## Short Synopsis of Materials

Beyond modeling: considering user-centred and post-development aspects to ensure the success of a decision support system (Lacoste and Powles, 2016) focuses on the updating of the Ryegrass Integrated Management (RIM) DSS, a tool for weed management that has seen widespread use despite its simple design. In this article, Lacoste and Powles seek to document the rationale behind their design decisions with an overall goal of identifying key aspects of a successful DSS.
RIM was a weed management tool that saw extensive adoption in the southern grain belt of Australia in the 1990s and 2000s. It relied on a simple model of weed growth and herbicide resistance evolution to help farmers determine optimal management practices for long term sustainability. RIM was built in Microsoft Excel due to its accessibility to farmers and featured an interface based on filling out input cells within a spreadsheet. Users would be prompted to input characteristics of their field and select from a combination of over 40 different ryegrass management options. The tool’s outputs were estimations of crop economic performance and ryegrass prevalence over time.
In redesigning the RIM tool, Lacoste and Powles prioritized the preservation of key features that made the tool successful in its initial form. A key component of this was opting to retain the scenario customizability of the original tool instead of creating a prescriptive model that specifies the optimal management choice. This is because research has shown that farmers prefer to choose from a range of options what they deem to be the best choice for their operation. Additionally, the number of unknowns designers would have to factor into a prescriptive model would be unrealistic to implement for all user farming scenarios. It was also deemed necessary for the long term viability of the tool to keep Microsoft Excel as the platform, because it is continuously updated and very widely used by farmers already.
To ensure its accessibility to users, RIM’s user interface was refined and modernized with intuitive graphs and buttons. Similarly, help and guidance icons were placed at every point to describe their function. Backend refinements to the model were made to improve its functioning and make the tool adaptable to different weeds and environments by other researchers.
Lacoste and Powles identified participatory workshops as the best method for introducing users to RIM. This is because moderators are present to provide technical assistance, but more importantly, to stimulate discussion between farmers on the annual ryegrass management approaches they favor.

Bridging the gap between models and users: A lightweight mobile interface for optimized farming decisions in interactive modeling sessions (Mossinger, Troost and Berger, 2022) describes a case study for combining farmer-derived farm management information with mathematical programming (MP) to yield unforeseen insights. MP, also known as mathematical optimization, refers to the use of optimization problems to model complex systems. Mossinger et al. used MP based on farmer input to produce a farm planning model that relies on farmer knowledge. This model could then be used by farmers to guide future decision making and policymakers to identify suitable agricultural policy.
The impetus for this study came from the knowledge gap between researchers who develop models and farmers who are intended to use them. To capture decision making and the rationale behind it, Mossinger et al. built a computer-accessible user interface from the R Shiny package. This allowed farmers to record the factors that were relevant to each farm management decision they made on a computer. Each computer was preloaded with a farm planning model and sample data based on researchers’ expectations. However, as farmers entered more decisions into their computer’s database, the model would be updated to account for these new data points. As a result, the model could give more accurate decision predictions as its use increased.
This method of model optimization was trialed with smallholder farmers in southeastern Paraguay. In an iterative process, farmers walked through their cultivation and farm management practices during interactive sessions. Their decision data points were then used to calibrate the model, farmer feedback was incorporated to account for unexpected variables, and the interactive sessions were repeated. Farmers could then use the models to simulate the productivity and profitability of different management practices on their farming systems.
Farmers generally reacted positively to the tool, finding its recommendations insightful and the ability to experiment with possible land use plans helpful in their decision making process. Additionally, farmers found the simple user interface easy to navigate despite limited computer familiarity.


## Summary of Key Takeways from the Materials

DSSs typically use theory-based mathematical models to approximate real world conditions. They may rely on highly localized calibrations or provide only a general estimation of the processes they model. Whether providing predictive management recommendations or simply additional information, these tools are designed to help farmers optimize their farming operations.

While all DSSs are intended to provide farmers with valuable insights, their use by consumers is relatively low. This is largely due to the disconnect between farmers and the scientists and programmers who create DSSs. Tool designers may not be familiar with the intricacies of their intended user group’s farming operation. Additionally, they are often not designed with realistic expectations of their users’ technological literacy.

Successful DSSs will have clearly defined purposes and user groups around which the tools are designed. This entails exploration of each user group’s needs and consultation of these user groups throughout the development process. They also must have user interfaces that are easily accessible to their users. Furthermore, DSSs will not replace or invalidate farmer and extension staff knowledge because these stakeholders have a greater understanding of their particular context than a DSS can account for. Instead, they should be viewed as augmentations for the decision making process.


## Discussion Questions

1. This week’s readings emphasized the ability of a tool to allow users to experiment with different decision options as an important component of a useful DSS. Can you think of any other ways of engaging technology users that might be useful for DSSs, or digital agriculture in general?
2. The MP paper uses farmer-inputted decisions as data points to train its model. Do you see any advantages in this? What about potential pitfalls?
3. Has anyone worked with a tool that could be considered a DSS before, either as a user or a designer? If so, in what context and did you find it useful?
4. Can you think of any information challenges in your own field of interest that could benefit from the development of a DSS?


## Further Resources

1. A recent article about farmer use of climate change DSSs that Purdue’s Linda Prokopy collaborated on: [doi: 10.1016/j.jenvman.2020.111758](https://www.sciencedirect.com/science/article/pii/S0301479720316832?_ga=2.64209583.1001126463.1650236161-368217501.1641613724)
2. A simple cover crop decision support tool by the NRCS that runs in Excel: https://www.nrcs.usda.gov/wps/portal/nrcs/mo/soils/health/
3. A review of decision support systems in modern agriculture: [doi: 10.1016/j.compag.2020.105256](https://www.nrcs.usda.gov/wps/portal/nrcs/mo/soils/health/)
4. A review of DSS development strategies: [doi: 10.1007/s11119-016-9491-4](https://link.springer.com/article/10.1007/s11119-016-9491-4)


## Discussion Notes and Feedback
