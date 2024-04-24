# Introduction to Artificial Intelligence

Artificial Intelligence refers to the field of computer science concerned with creating intelligent agents – systems that can reason, learn, and act autonomously in their environments [1]. These agents mimic human cognitive abilities such as problem-solving, decision-making, and perception to achieve specific goals.

Here's a relevant quote from Stuart Russell and Peter Norvig, authors of a widely used AI textbook: "AI is the study of intelligent agents: any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals" [1].

Some core characteristics of intelligent agents include:

- Learning: The ability to acquire knowledge and skills from experience. This can involve various techniques like supervised learning, unsupervised learning, and reinforcement learning. 
- Reasoning: The ability to use knowledge to draw inferences and make decisions. This involves processing information, evaluating options, and selecting the most appropriate course of action. 
- Problem-solving: The ability to find solutions to complex problems. This requires the agent to define the problem, explore possible solutions, and evaluate their effectiveness. 

## AI vs. Machine Learning (ML)

Machine learning (ML) is a subfield of AI that focuses on algorithms that can learn from data without being explicitly programmed. ML algorithms can identify patterns and relationships in data, which allows them to make predictions or decisions on new data.

Here's how AI and ML differ:
- Scope: AI is the broader concept encompassing various techniques to achieve machine intelligence. Machine learning is a specific approach to AI that relies on algorithms that can learn from data.
- Focus: AI is concerned with building intelligent agents that can reason, learn, and act autonomously. ML focuses on developing algorithms that can learn from data and make predictions or decisions.

## PEAS and Intelligent Agents

The PEAS framework is a conceptual model used to describe the essential components of an intelligent agent. PEAS stands for:
- Performance: The measure of success for the agent in its environment. This could be winning a game, maximizing efficiency, or completing a task accurately. (https://www.geeksforgeeks.org/understanding-peas-in-artificial-intelligence/)
- Environment: The surroundings in which the agent operates. This includes all the physical and informational aspects that can influence the agent's actions.
- Actuators: The mechanisms through which the agent interacts with the environment. These allow the agent to take actions that affect the environment.
- Sensors: The components that enable the agent to perceive its environment. Sensors gather information about the environment, which the agent processes to make decisions.

### 4. Examples of AI and PEAS in Action

Here are some real-world examples illustrating AI and the PEAS framework:
1. Self-driving car:
        - Performance: Maximize safety and arrive at the destination efficiently.
        - Environment: Roads, traffic, pedestrians, weather conditions.
        - Actuators: Steering wheel, brakes, accelerator.
        - Sensors: Cameras, LiDAR, radar, GPS.
2.  Spam filter:
        - Performance: Minimize spam emails reaching the inbox.
        - Environment: Incoming emails with text and attachments.
        - Actuators: None (acts by classifying emails as spam or not spam).
        - Sensors: Analyzes email content and sender information.
3. Recommendation system:
        - Performance: Recommend products or content relevant to the user's interests.
        - Environment: User browsing history, purchase history, and product information.
        - Actuators: Displays recommendations on a website or app.
        - Sensors: Analyzes user data and product information.

These examples demonstrate how AI systems are designed with specific goals (performance) in mind, operate within defined environments, and interact with the environment through actuators and sensors.

## Rationality in AI Agents

According to Russell and Norvig (2021), a cornerstone of AI research is the concept of a rational agent: an entity that acts with the aim of achieving its goals in a way that is optimal within its environment.
Imagine your friend playing chess. They consider the board, their opponent's moves, and possible strategies before making their next move. This is a form of rationality – making informed decisions to achieve a goal. In AI, we strive to create rational agents that do the same.
- What it means: An AI agent is rational if it consistently chooses actions that maximize its chances of achieving its goals, given its current perception of the environment.
- Example: A self-driving car should choose the safest route based on traffic conditions, weather, and its destination. A bad decision could be running a red light to save a few seconds, potentially causing an accident.

### A breakdown of rationality in AI:
- Decision-making: A rational agent strives to make decisions that maximize its chances of achieving its goals based on its current understanding of the environment.
- Logical reasoning: Rational agents employ logical reasoning to analyze situations and determine the best course of action.
- Bounded rationality: In real-world scenarios, agents may exhibit "bounded rationality" due to limitations in processing power, knowledge, or time. This can lead to suboptimal but still effective decisions.

## Components of AI Systems
AI systems are complex entities composed of various interacting components that mirror the capabilities of an intelligent agent:
- Agent: The AI system itself, acting as an intelligent entity within the environment.
- Reasoning: The capability to use logic, knowledge, and perception to draw conclusions and make decisions.
- Environment: The surroundings in which the agent operates, including all the factors that can influence its actions and perception.
- Actions: The set of possible actions the agent can take to manipulate the environment or achieve its goals.
- Perception: The ability to sense and interpret the environment through sensors or other means of information gathering.

Here are some additional details on the core components:
- Knowledge representation and reasoning (KR&R): This refers to how the AI system stores and manipulates knowledge about the world. Techniques include logic statements, semantic networks, and probability distributions. (Source: Brachman and Levesque, 1985)
- Learning: AI systems can learn from data through various techniques like supervised learning, unsupervised learning, and reinforcement learning.
- Problem-solving: The system employs search algorithms, heuristics, and optimization techniques to tackle complex problems and find solutions.
- Planning and decision-making: AI systems can plan future actions and make decisions based on their knowledge, goals, and perceived environment.

## Environment Properties of AI Systems

The environment in which an AI agent operates significantly impacts its performance. Here are some key properties to consider:

- Accessibility: Can the agent fully perceive the environment through its sensors?
- Determinism: Is the environment predictable, or are there elements of randomness?
- Static vs. Dynamic: Does the environment remain constant, or does it change over time?
- Discrete vs. Continuous: Are the states of the environment discrete (finite) or continuous (infinite)?

Example: Self-Driving Car in Different Environments

A self-driving car's performance depends on the environment:

- Highly accessible environment: A well-mapped highway with clear lane markings and predictable traffic is easily perceived by sensors.
- Deterministic environment: Traffic rules and predictable driver behavior make the environment somewhat deterministic.
- Dynamic environment: Weather conditions, unexpected obstacles, and unpredictable pedestrian movement pose challenges.
- Continuous environment: The car's position, speed, and surrounding objects constantly change, requiring continuous decision-making.

## Agents in AI Systems
Within the realm of AI, agents are intelligent entities that perceive their environment, take actions, and strive to achieve goals. However, not all agents are created equal. Let's explore different types of agents, each with its strengths and limitations:

1. Simple Reflex Agents: The Simplest Response

    - Function: React directly to the current percept (sensory input) based on pre-defined rules. (Source: Stuart Russell and Peter Norvig, Artificial Intelligence: A Modern Approach, 3rd Edition (2021))
    - Strengths: Simple to design and implement, efficient for well-defined environments.
    - Weaknesses: No memory of past experiences, limited adaptability to changing environments.
    - Example: A thermostat that turns on the heater when the temperature falls below a set point (percept) and turns it off when it reaches the desired temperature.

2. Reflex Agents with State: Remembering the Past

    - Function: Similar to simple reflex agents, but they maintain some internal state to track the environment's history.
    - Strengths: Can handle situations where past actions influence current decisions.
    - Weaknesses: Limited memory can still restrict adaptability in complex environments.
    - Example: A vending machine that remembers the amount of money inserted (state) and dispenses the product only when sufficient payment is received.

3. Goal-Based Agents: Driven by Objectives

    - Function: Possess a specific goal and actively seek actions to achieve it.
    - Strengths: More flexible than reflex agents, capable of planning and reasoning. 
    - Weaknesses: Requires defining goals explicitly, may struggle in environments with obstacles or unknown paths.
    - Example: A robot vacuum cleaner programmed with the goal of cleaning an entire room. It uses sensors to navigate and adjust its path based on obstacles.

4. Utility-Based Agents: Making Value Judgments

    - Function: Similar to goal-based agents but consider the "utility" (degree of satisfaction) associated with different outcomes.
    - Strengths: Can make nuanced decisions based on the desirability of various options.
    - Weaknesses: Defining utility functions can be complex, especially for subjective goals.
    - Example: A chess-playing AI agent that evaluates each move based on its potential to lead to a winning position (higher utility).

5. Learning Agents: Continuously Evolving

    - Function: Can learn and improve their performance over time through experience or interaction with the environment.
    - Strengths: Highly adaptable to changing environments, capable of handling complex and uncertain situations.
    - Weaknesses: Learning algorithms can be computationally expensive, and may require a large amount of training data.
    - Example: A recommendation system that learns user preferences based on past interactions and suggests items with high predicted utility for the user.

## Further Reading
Books:
- Artificial Intelligence: A Modern Approach by Stuart Russell and Peter Norvig (3rd Edition, 2021): This classic textbook provides a comprehensive introduction to AI concepts, algorithms, and applications.
- Artificial Intelligence by Melanie Mitchell (McGraw-Hill, 1997): Another well-regarded text offering a broader perspective on AI, including philosophical and historical aspects.

## Analysis for Submission
- Please write a 2-page paper on a specific problem in your domain of research or interest that you would like to solve with AI. Define the components and justify the environment definition. Write the justification for the approach you would like to take in designing this AI agent. 
