#Cyber-Physical Systems (CPS)

##What is CPS?
Cyber-physical systems (CPS) are a type of engineered system that integrates physical components with computational algorithms and networking capabilities. In simpler terms, they are systems where the physical world and the digital world are tightly connected and work together.

Here's an analogy: Imagine a car. The engine, wheels, and brakes are the physical components. The computer system that controls the engine performance, monitors tire pressure and activates airbags is the computational part. When these two parts work together seamlessly, you have a CPS – a smart car that can adjust its performance and respond to situations in real-time.

##Examples of CPS:
- Self-driving cars: These cars use sensors, cameras, and computers to perceive their surroundings and navigate roads autonomously.
- Smart grids: These power grids use sensors and communication networks to monitor electricity use and automatically adjust power generation and distribution for efficiency.
- Industrial robots: These robots are programmed to perform specific tasks in factories and often have sensors that allow them to interact with their environment.
- Wearable health monitors: These devices track your heart rate, activity levels, and other health data, providing insights into your well-being.

##Key Components of CPS
CPS relies on a tight integration of various components to bridge the physical and digital worlds. Here's a detailed breakdown of some key elements:
1. Sensor and Sensor Networks:
   - Function: Sensors are the eyes and ears of a CPS. They convert physical quantities like temperature, pressure, or motion into electrical signals that computers can understand. Sensor networks connect multiple sensors to gather data from a wider area.
   - Example: In a self-driving car, numerous sensors like LiDAR (Light Detection and Ranging), cameras, and ultrasonic sensors work together to create a 360° perception of the surroundings.
   - Resource: "A Survey on Wireless Sensor Networks for Cyber-Physical Systems" provides a technical overview of sensor networks in CPS https://ieeexplore.ieee.org/document/6096958.
3. Communication
   - Function: Communication networks are the nervous system of a CPS. They enable data exchange between sensors, controllers, and actuators, allowing for coordinated actions. Communication protocols ensure reliable and timely data transfer.
   - Example: Industrial control systems often utilize wired communication protocols like CAN (Controller Area Network) for real-time data exchange between machines.
   - Resource: Check out this paper: https://arxiv.org/abs/2102.07166 on task-oriented communication design for CPS.
5. Decision Making
   - Function: The decision-making component analyzes sensor data and control algorithms to determine the optimal response for the physical system. This can involve real-time processing, machine learning techniques, and increasingly, data-driven approaches. Data-driven decision-making leverages historical data and statistical analysis to inform choices. Machine learning algorithms can be trained on vast amounts of data to identify patterns, predict future outcomes, and recommend actions for the CPS.
   - Advantages of Data-Driven Decision-Making in CPS:
       - Improved Efficiency and Performance: By analyzing past data, CPS can optimize resource allocation, predict maintenance needs, and fine-tune control algorithms for better efficiency.
       - Enhanced Adaptability: Data-driven systems can learn and adapt to changing environments. For instance, a self-driving car can adjust its behavior based on real-time traffic data and weather conditions.
       - Increased Autonomy: As CPS collects more data and refine their decision-making models, they can operate with greater autonomy, reducing human intervention.
   - Challenges of Data-Driven Decision-Making in CPS:
       - Data Quality and Security: The quality and security of the data used to train algorithms are crucial. Biased or inaccurate data can lead to suboptimal decisions, and security breaches can compromise system integrity.
       - Explainability and Trust: Complex machine learning models can be opaque, making it difficult to understand how they arrive at decisions. This can raise concerns about trust and accountability in safety-critical CPS.
       - Computational Demands: Training and running sophisticated machine learning models can require significant computational resources, which may be a constraint for resource-limited CPS.
  - Example: A robotic vacuum cleaner is a good example of a data-driven CPS. It uses sensors like LiDAR to map its environment, cameras to detect obstacles, and bump sensors to avoid collisions. The control system analyzes sensor data in real-time and employs decision-making algorithms to navigate efficiently, clean designated areas, and dock itself for charging. Machine learning can further enhance the robot's capabilities. By analyzing past cleaning patterns and user preferences, the robot can optimize cleaning routes, personalize cleaning schedules, and even anticipate user needs.
7. Actuators: Actuators are the muscles of a CPS. They convert electrical signals from controllers into physical actions, influencing the environment. Robots are actuators commonly used now in CPS.
8. Embedded Systems
  - Function: Embedded systems are specialized computers dedicated to specific tasks within a CPS. They are often compact, low-power, and tailored to interact with sensors and actuators.
  - Example: The engine control unit (ECU) in a car is an embedded system that monitors engine sensors, controls fuel injection and ignition timing, and ensures optimal engine performance.

##Characteristics of Cyber-Physical Systems (CPS)
CPS exhibits unique characteristics that set them apart from traditional computing systems. Here's a breakdown of some key features:
1. Systems of Systems (SoS):
    - Concept: CPS often comprises interconnected sub-systems, each with its own functionalities, forming a complex SoS. These sub-systems can be geographically dispersed and communicate with each other to achieve a larger goal.
    - Example: A smart grid is an SoS. It integrates power generation plants, transmission lines, distribution networks, and even individual homes with smart meters. All these sub-systems work together to ensure efficient and reliable electricity delivery.

2. Reactive Computations:
    - Function: Unlike traditional computer programs with predefined sequences, CPS computations are reactive. They continuously react to real-time data from the physical world through sensors. This necessitates algorithms that can process data and make decisions quickly, often within milliseconds.
    - Example: An anti-lock braking system (ABS) in a car is a reactive CPS. It constantly monitors wheel speed sensors and adjusts brake pressure instantaneously to prevent wheel lockup during emergency braking.

3. Concurrency:
    - Concept: Multiple tasks or processes in a CPS may need to be executed simultaneously. This concurrency is crucial for handling the real-time nature of physical interactions. Efficient scheduling and synchronization mechanisms become essential to ensure smooth operation.
    - Example: In a self-driving car, multiple processes run concurrently. One process might be responsible for perception (interpreting sensor data), another for planning the driving route, and a third for controlling the vehicle's actuators (steering, braking).

4. Novel Interactions Between Cyber and Physical Worlds:
    - Concept: CPS blur the lines between the digital and physical realms. The cyber world controls and influences the physical world through actuators based on sensor data. This tight integration creates new challenges and opportunities for system design and analysis.
    - Example: A smart thermostat is a simple example. It receives temperature readings from the physical environment (your home) and uses software algorithms to adjust the heating or cooling system, influencing the physical comfort level in your home.

5. Novel Interactions Between Communications/Computing/Control:
    - Concept: Traditional systems often have separate communication, computing, and control functionalities. In CPS, these functions are tightly intertwined. Communication protocols ensure reliable data exchange, computing resources analyze data and make decisions, and control algorithms translate these decisions into actions for the physical world.
    - Example: An industrial robot arm exemplifies these interactions. Communication protocols enable communication between the control system and sensors/actuators on the robot arm. Computing power analyzes sensor data (joint positions, object location) and control algorithms determine the robot's movement based on the program and real-time feedback.

6. Humans in the Loop:
    - Concept: While CPS are increasingly autonomous, human involvement remains crucial. Humans may be needed for system design, supervision, maintenance, and intervention in critical situations. Effective human-machine interfaces (HMI) are essential for smooth interaction between humans and CPS.
    - Example: Airplanes with advanced autopilot systems are CPS. While the autopilot can handle routine flight operations, human pilots are still on board for critical decision-making during emergencies or adverse weather conditions.

7. Handling Uncertainty and Unpredictability:
    - Concept: The physical world is inherently uncertain, and CPS need to be robust in the face of unexpected events or sensor noise. Techniques like fault tolerance, redundancy, and real-time adaptation are crucial for reliable operation.
    - Example: Self-driving cars need to handle unexpected situations like sudden weather changes or erratic driver behavior. The CPS must be able to adapt its behavior based on real-time data and make safe decisions even in uncertain situations.

##Further Readings:
Here are published works regarding CPS and agriculture that I encourage you to read and critique:
- Smart monitoring of potato crop: a cyber-physical system architecture model in the field of precision agriculture (https://doi.org/10.1016/j.aaspro.2015.08.041)
- Smart Field Monitoring using ToxTrac: A Cyber-Physical System Approach in Agriculture (https://ieeexplore.ieee.org/abstract/document/9215282)
- Agricultural cyber-physical system enabled for remote management of solar-powered precision irrigation (https://www.sciencedirect.com/science/article/pii/S1537511017311455)

## Submission
1. Read the papers listed above and write a critique of their strengths and gaps. 1 page per paper.
2. In your own work detail how the system you are developing is a CPS and what is lacking. 1 page.
