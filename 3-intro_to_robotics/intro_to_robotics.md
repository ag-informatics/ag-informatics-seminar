# INTRODUCTION TO ROBOTICS-I: FOUNDATION AND TERMINOLOGY

Robots are all around us, from the industrial assembly lines to the robotic vacuum cleaners in our homes, but what exactly are they? Before we delve deeper into the world of robotics, let's take a moment to reflect on your own understanding of what makes a robot. Jot down your thoughts – what characteristics define a robot in your mind? 

## Historical Perspective
The journey of robotics has been a fascinating one, marked by continuous innovation and evolution. From the rudimentary automata of the ancient world to the sophisticated machines of today, robots have captured our imagination and reshaped our lives.
The first robots were simple machines designed to perform repetitive tasks. However, robots have become much more sophisticated in recent years. Today, there are robots that can walk, talk, and even see.
Please read this article (https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=5274297 ) to get a glimpse of its history. 

## Robot Categorization
Robots can be characterized and categorized in many ways. A common methodology is to view them as industrial, social, and intelligent robots.
Similarly, they can also be categorized by application as medical robots, agricultural robots, underwater robots, etc. 
A more technical and traditional approach is to categorize robots based on the configurations of their linkages and joints.
    
## Anatomy of a Robot
A robot usually has three main components: 
- physical structure
- sensors and actuators
- control system 

![The components of a Robot.](robot_components.jpg)
### Physical Structures and Configuration
The physical structures include links and joints. A link can be thought of as a rigid structure that bears weight and provides support to the robot. A joint is typically driven by a motor and provides sliding (prismatic) or rolling (revolute) motion to the structure. The links and joints can be arranged in a variety of configurations. 
There are three main types: serial, parallel, and mobile robots. 

![(a) Serial manipulator with 6 DOFs, (b) A Stuart platform (parallel robot), and (c) A mobile robot] (robot_configs.jpg)

Serial manipulators are those which have mechanical links connected in a serial chain, whereas in a parallel configuration, links are connected between two bases, forming a closed loop. 
A good example of a serial robot is an industrial robot arm. Stuart (and Go) platform is a great example of a parallel robot. It has a fixed base and a mobile top, which is moved by actuating the links.

Both serial and parallel robots can have revolute and prismatic joints. Please read this paper (https://link.springer.com/chapter/10.1007/978-3-030-85980-0_1) to get a general overview of these configurations. 

Mobile robots are robots with wheels, whegs, and propellers such as drones and autonomous cars. In this, wheel and propeller dynamics of balancing forces are used to control their motion and orientation.
#### Degree of Freedom
The degrees of freedom (DOF) of a robot refers to the number of independent ways in which it can move. For example, a robotic arm with three joints (shoulder, elbow, and wrist) has 3 DOF, allowing it to move in three-dimensional space. This video further explains DOFs (https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-1-degrees-of-freedom-of-a-rigid-body/). DOFs are important designing the controls and the path planning routes for the robot. 

### Sensors and Actuators
Sensors are transducers that convert one form of signal into another, usually electrical. It is important to note here that their goal is to just convert, it is the mathematical logic that helps us quantify that conversion and derive a measurmeent. Thinking about this deeply, can you explain why I said so?
There are many types of sensors used in robotics, from tactile to vision. LIDARs, GPS, stereo cameras, IMU, and encoders are some common ones. 

An Actuator generates a physical force or torque when a command is given to it. It converts electrical impulses or signals into mechanical forces. Stepper motors, Pneumatic pumps, and piezoelectric actuators are some common types.   

###Control Systems
Control is the brain of the robot. Robot controls decide what or how the robot should move given a set of sensor feedback. This is the case in closed-loop control. Some robots have open-loop control, such as industrial arms. They work on pre-programmed ionstructions and have limited ways of correcting their behavior. 

Controls are based on perception and planning. Perception is building a state of "your reality". This is all the knowledge that the robot has about its surroundings and its own state in it. 
Planning involves using the knowledge of the environment and the robot dynamics, along with the task goals, to decide future actions. This can be finding a path around an obstacle to picking up an object. In planning, mathematical trajectories are defined between the current state and the goal state. 

## Key terminology 
- End Effector: The tool attached to the robot to accomplish the task. For example, grippers. 
- Payload: The maximum amount of weight a robot can manipulate. 
- Workspace: The volume of space a robot can operate within.
- Dextrous workspace: the set of all positions that can be reached with all possible orientations.
- Repeatability: The consistency with which a robot can reach the same point in the world frame.


## Moving the Robot: Kinematics
The study of the motion of the links and joints of a robot is called kinematics. This is a fundamental topic in the study of any robot, wherein mathematical relationships are derived to map joint coordinates and the world coordinates. 
This has two main types: forward and inverse. Forward kinematics maps the joint configuration to the position of the robot in the real world. In inverse kinematics, often the more important and difficult one, we derive mathematical relationships to map world coordinates to the joint coordinates.
For simple robots, such as a cartesian robot, it is fairly simple to derive the kinematics. However, as structures become complex, instantaneous motion in terms of Jacobians is used to study the kinematics. If you are interested in looking at this more deeply, please read: http://motion.cs.illinois.edu/RoboticSystems/Kinematics.html   

Also, if you want to try out moving a robot yourself and see both forward and inverse kinematics, check out this software. This allows you to use many of the already-built robots to study their kinematics. You can also import your own robot model and calculate its kinematics, given you have the correct DH parameters. 


# Expected Submission

Everyone should submit a 2-page document on Brightspace answering the following questions:

1. What is your understanding of a robot? Is a washing machine a robot?
1. What stands out to you in the evolution of robotics?
1. Which robot categorization did you find most useful and why?
1. Why is a dextrous workspace different than just a workspace?
1. Do you think human and robot perception is alike? Explain.
1. After reading these resources, how has your understanding of a robot changed?


## Further Resources

A few more helpful articles for grasping an overview of robotics:
- Overview of Robotics: https://www.science.org/doi/full/10.1126/scirobotics.aau8479
- Is the future all robots? Bill Gates thinks so : https://modernrobotics.northwestern.edu/nu-gm-book-resource/2-1-degrees-of-freedom-of-a-rigid-body/

## Discussion Notes and Feedback
Note taker: [name]

[notes from the class discussion]


# FYI: Creating a Pull Request

*IMPORTANT:*

Before beginning your work ensure that you first create a "fork" from the course GitHub page. This creates a copy of the ag-informatics-seminar course content onto *your* GitHub repository. From this point, you should git clone this repository onto your device and proceed by making edits to the desired file in that location. Below are three YouTube videos that I found helpful when learning how to create a pull request, additionally I also encountered some issues when using Terminal git commands and was able to fairly easily find solutions on stackoverflow.com . Let me know if you have any additional questions!

https://youtu.be/rgbCcBNZcdQ

https://youtu.be/npnfDwmHKhY

https://youtu.be/8A4TsoXJOs8


# Topic Analysis 

At minimum, you should read/view/parse these materials and write a one page reflection. **You will submit a 1-2 page topic analysis every Discussion week, starting Week 2.** Your topic analysis should contain the following:

1. Heading: contains your name, the week, the date, and the discussion topic title.

2. Summary: A 1 paragraph summary of the topic based on the readings and other materials shared for the week.

3. Analysis: A 2-3 paragraph analysis about what you think the open issues are in this area of research and practice. You can include critiques of the papers and other materials, and bring in other concepts you think are relevant to the discussion. Consider writing about your reactions to the topic, your ideas/positions on the topic driven/contradicted by the materials, or 

4. Questions: A list of 3-5 questions for the in-class discussion.



