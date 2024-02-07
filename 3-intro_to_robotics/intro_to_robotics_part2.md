# INTRODUCTION TO ROBOTICS-II: Sensors, Controls, and Intelligence

Building the mechanical structure and figuring out the kinematics is half the story of robotics. Automation, re-programmability, and repeatability are key to building a successfull robot. 

## Sensing and Perception 
Sensors, both intrinsic and extrinsic, provide a pathway to observe the world and the robot's place in it. The raw data captured, in the form of videos or just electrical signals, is just the first step. To extract information out of this involves processing these signals. Mathematical models, from simple Fast Fourier Transforms to cutting-edge generative models, are all an attempt to extract information. Another way to look at these is an absolute and guided categorization. In FFTs, for example, you will always get frequency bins. But, in neural networks and other such models, by providing annotated inputs, you can guide the model to show what you want.

Perception is defined by APA as "the process or result of becoming aware of objects, relationships, and events by means of the senses". Therefore, it is not just the acquisition of data from physical senses, but your own awareness, information extraction, from that data. The mathematical models, including neural networks, are what enable perception in robots when working together with the sensors.

Cognition is the "mental action or process of acquiring knowledge and understanding through thought, experience, and the senses". It therefore alludes to a more subjective experience of the world. Can robots have cognition? What is needed for it?

## Robot Controls
Control is the brain of the robot. Robot controls decide what or how the robot should move given a set of sensor feedback. This is the case in closed-loop control. Some robots have open loop control, such as industrial arms. They work on pre-programmed ionstructions and have limited ways of correcting their behavior. 

Controls are based on perception and planning. Perception is building a state of "your reality". This is all the knowledge that the robot has about its surroundings and its own state in it. 
Planning involves using the knowledge of the environment and the robot dynamics, along with the task goals, to decide future actions. This can be finding a path around an obstacle to picking up an object. In planning, mathematical trajectories are defined between the current state and the goal state. 

## Common Control Approaches
A robot usually has three main components: 
- Open-Loop Control: Think of a record player. You set the needle, and the music plays at a predetermined speed. That's open-loop control. The robot follows pre-programmed instructions without any feedback. It's simple, fast, and good for repetitive tasks. But if something unexpected happens, the robot has no way to adjust. Like a record player hitting a scratch, it might stumble or even crash!
- Closed-Loop Control: Now imagine a music player that adjusts the volume based on the song's loudness. That's closed-loop control. The robot constantly monitors its performance (like the volume) and compares it to its desired goal (like a comfortable listening level). If there's an error, it adjusts its actions (like changing the volume) to get back on track. This makes it more adaptable and robust, handling bumps and changes better than its open-loop friend. Think of a self-driving car adjusting its speed based on traffic, that's closed-loop in action!
- Neural Network Driven Controls: Imagine a music player that not only adjusts volume but also learns your preferences over time. That's the power of neural networks! These complex algorithms mimic the human brain, allowing robots to learn and adapt from experience. They can handle even more complex situations and even anticipate potential problems.  Think of a robot arm learning to grasp different objects delicately, that's neural network control at its finest!

Remember: Each approach has its strengths and weaknesses. The best choice depends on the robot's task and environment. But one thing's for sure, these control algorithms are the brains behind the brawn, making robots move, learn, and interact with the world around them!

### Control Algorithms
#### PID Control: Imagine a car's cruise control. It maintains a desired speed despite hills and wind. That's PID in action!
  - Proportional (P): Reacts to the current error (like how far off the car is from the desired speed). Larger errors lead to bigger adjustments.
  - Integral (I): Considers past errors, remembering how long the issue has persisted. It helps eliminate lingering errors gradually.
  - Derivative (D): Predicts future errors based on the error's change. It anticipates and counteracts changes before they become big problems.

By combining these, PID controllers achieve precise and stable control, making them popular in various applications, from robots to airplanes.

Here is an interesting video to see this in action: "The Robot That Learned to Walk" by Wired: https://m.youtube.com/watch?v=77LCA3rY1y0

#### Reactive Control: Think of a reflex. You see a ball coming, you duck! Reactive control is similar. Robots sense their surroundings and react instantly without complex calculations.
1. Simple and fast: Perfect for quick responses in dynamic environments. Imagine a robot arm avoiding obstacles while reaching for an object.
2. Limited learning: Relies on pre-defined rules, making it less adaptable to complex situations.

Reactive control shines in dynamic environments where fast responses are crucial, but for more nuanced tasks, it might need help from other algorithms.

Reactive Robotics is the brainchild of Ronald "Rodney" Brooks, a visionary and the founder of iRobot. Here is an article that explains reactive planning in Roomba of iRobot: "How Roomba Avoids Obstacles" by iRobot: https://www.thezebra.com/resources/home/how-roomba-works/

#### Reinforcement Learning: Imagine a robot chef trying different recipes, learning from successes and failures. That's reinforcement learning!

1. Neural networks: Mimic the brain, allowing robots to learn from experience.
2. Trial and error: The robot interacts with its environment, receiving rewards for good actions and penalties for bad ones. Over time, it learns the best course of action.

This approach is powerful for complex tasks where the rules are unclear. Think of a robot learning to walk or a self-driving car navigating traffic. However, it can be slower than other methods and requires careful design of the reward system.

Here are some cool thought pieces on RL use cases: 
-"How AI is Learning to Play Games (and Beat Humans)" by MIT Technology Review: https://news.mit.edu/2011/game-artificial-intelligence-1031
-"The Robot Chef That Learned to Make Pizza" by The New York Times: https://www.youtube.com/watch?v=BMkpEAgYlxU

Structure of an RL Algorithm: While the idea of robots learning through trial and error might seem simple, Reinforcement Learning (RL) algorithms have a specific structure that enables them to achieve this feat. Here's a breakdown:

Main Components:
 - Agent: This is the "learner," the robot or program interacting with the environment.
 - Environment: This is the world the agent interacts with, providing rewards or penalties for its actions.
 - Action Space: The set of possible actions the agent can take.
 - State Space: The set of possible states the environment can be in.
 - Policy: This is the "brain" of the agent, deciding which action to take in a given state.
 - Reward Function: This defines what's considered good (positive reward) or bad (negative reward) for the agent.

The Learning Loop:
    - Observe: The agent perceives its current state (e.g., the robot sees its surroundings).
    - Act: The agent chooses an action based on its policy (e.g., the robot moves its arm).
    - Receive Reward: The environment provides a reward based on the action's outcome (e.g., +1 for reaching the object).
    - Update Policy: The agent learns from the experience, adjusting its policy for future decisions (e.g., increases the chance of repeating the successful action).

This loop continues repeatedly, allowing the agent to gradually improve its behavior towards maximizing rewards.

Types of RL Algorithms:
   - Value-based: These estimate the value of taking an action in a given state. Examples: Q-learning, SARSA.
   - Policy-based: These directly learn the policy for choosing actions. Examples: Deep Deterministic Policy Gradients (DDPG), Proximal Policy Optimization (PPO).

# Expected Submission

Everyone should submit a 2-page document on Brightspace answering the following questions:
 1. Pick an application close to your research or interest. Define the environment and the task for which you need a robot. Based on what you have learned so far, define the constraints, the mechanical structure, the sensors, actuators, and the controls you might need for this robot. Justify your choices. 
 2. Considering RL, can you imagine what the training environment will be like for this robot? Define the rewards, action space, and workspace for your robot. 
 3. What do you think are the failure points for your robot?

# Further Resources

1. OpenAI Gym: A popular toolkit for building and experimenting with RL environments: https://gym.openai.com/: https://gym.openai.com/
2. Stable Baselines3: A Python library for implementing various RL algorithms: https://stable-baselines3.readthedocs.io/en/master/: https://stable-baselines3.readthedocs.io/en/master/

## Discussion Notes and Feedback
Note taker: [name]

[notes from the class discussion]


# FYI: Creating a Pull Request

*IMPORTANT:*

Before beginning your work ensure that you first create a "fork" from the course GitHub page. This creates a copy of the ag-informatics-seminar course content onto *your* GitHub repository. From this point you should git clone this repository onto your device and proceed by making edits to the desired file in that location. Below are three YouTube videos that I found helpful when learning how to create a pull request, additionally I also encountered some issues when using Terminal git commands and was able to fairly easily find solutions on stackoverflow.com . Let me know if you have any additional questions!

https://youtu.be/rgbCcBNZcdQ

https://youtu.be/npnfDwmHKhY

https://youtu.be/8A4TsoXJOs8


# Topic Analysis 

At minimum, you should read/view/parse these materials and write a one page reflection. **You will submit a 1-2 page topic analysis every Discussion week, starting Week 2.** Your topic analysis should contain the following:

1. Heading: contains your name, the week, the date, and the discussion topic title.

2. Summary: A 1 paragraph summary of the topic based on the readings and other materials shared for the week.

3. Analysis: A 2-3 paragraph analysis about what you think the open issues are in this area of research and practice. You can include critiques of the papers and other materials, and bring in other concepts you think are relevant to the discussion. Consider writing about your reactions to the topic, your ideas/positions on the topic driven/contradicted by the materials, or 

4. Questions: A list of 3-5 questions for the in-class discussion.


