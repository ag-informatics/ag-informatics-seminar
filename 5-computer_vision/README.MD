# Computer Vision: A Glimpse into Seeing Machines

Computer Vision (CV) is a field of artificial intelligence that trains computers to interpret and understand the visual world. By processing, analyzing, and understanding images and videos, computers can identify objects, classify them, and react to what they "see" using cameras, data, and algorithms.

In this section, we first look at the human vision loop and the goal of CV. Taking a brief overview of color models and cameras, we look at the challenges in CV and the algorithms available to us. 

While this page provides a brief overview of the CV landscape, I encourage you to read this book which is considered the gold standard in learning CV. [https://szeliski.org/Book/] It is free to download. 

## Human Vision and CV 
The Human Eye:
	- Structure: The human eye is a complex organ that captures light and transmits visual information to the brain. It consists of the cornea, iris, pupil, lens, retina, and optic nerve.
	- Image Formation: Light enters the eye through the cornea and pupil, focusing on the retina by the lens. The retina contains photoreceptor cells called rods and cones, which convert light into electrical signals. These signals are then transmitted through the optic nerve to the brain, where they are interpreted as images.

Computer vision aims to emulate human visual perception by enabling computers to "see" and understand the world through digital images and videos. This involves extracting meaningful information from visual data and using it to achieve various goals, including
	- Image processing: Enhance, manipulate, and analyze images.
	- Feature extraction: Identify and describe key points in an image.
	- Object recognition: Classify and locate objects within an image.
	- Scene understanding: Interpret the overall context and content of an image.

Human vision serves as a powerful inspiration for achieving these goals in computer vision. The human visual system, comprising the eyes and the visual cortex in the brain, performs remarkable feats of perception through a complex interplay of biological processes:

    - Eyes: Capture light information through the retina, containing photoreceptor cells (rods and cones) that convert light into electrical signals.
    - Visual Cortex: Processes these signals, extracting features like edges, shapes, and textures.
    - Higher-level brain regions: Integrate these features with prior knowledge and experience to achieve object recognition, scene understanding, and other cognitive tasks.

## Color Models and Color Theory in Computer Vision

### Understanding Color:

    - Light: Composed of electromagnetic waves with varying wavelengths.
    - Color: Our perception of these different wavelengths. Different wavelengths of light are perceived as different colors.
    - Pixels: Individual elements in a digital image, representing a specific color value.

### Common Color Models: Different color models represent and manipulate color information in various ways. Some common models used in computer vision include:

    - RGB (Red, Green, Blue): Additive model used for displaying colors on screens. Combines varying intensities of red, green, and blue to create a wide range of colors.
    - HSV (Hue, Saturation, Value): Represents color in terms of hue (color angle), saturation (color intensity), and value (brightness). Often used for image manipulation and segmentation.
    - CMYK (Cyan, Magenta, Yellow, Key (Black)): Subtractive model used in printing. Combines inks to absorb specific wavelengths of light, creating the perceived color.

### Applications of Color Models:

    - RGB: Standard for digital images and displays.
    - HSV: Useful for tasks like color tracking and object segmentation due to its intuitive representation of color properties.
    - CMYK: Used in printing to achieve accurate color reproduction.

## Camera Technologies for Computer Vision

Cameras play a crucial role in capturing visual data for computer vision applications. Different camera types offer varying capabilities and are suited for specific tasks:

### Monocular Cameras:
    - Most common type of camera, using a single lens to capture images.
    - Provide rich color information and are relatively inexpensive.
    - Limited depth perception, making it challenging for tasks like 3D reconstruction and object pose estimation.

Relevant Links:
    - High-Speed Monocular Camera for Motion Analysis: https://photron.com/
    - Building a Monocular Depth Estimation System: https://github.com/nianticlabs/monodepth2

### Stereo Cameras:
    - Equipped with two lenses positioned slightly apart, mimicking human binocular vision.
    - Capture two slightly different viewpoints of the scene, enabling depth perception through triangulation.
    - Well-suited for tasks like 3D object reconstruction and robot navigation.

A stereo camera I used: ZED Stereo Camera for Depth Perception: https://www.stereolabs.com/

### Event Cameras:
    - Bio-inspired cameras that capture only changes in pixel intensity over time, not entire image frames.
    - Highly sensitive to motion and offer high temporal resolution, making them suitable for applications like object tracking and high-speed motion analysis.
    - Limited spatial resolution and lack color information, requiring additional processing for scene understanding.

Relevant Links:

    - Dynamic Vision Sensor (DVS) Event Camera: https://services.ini.uzh.ch/research/37839
    - Event-Based Vision for Autonomous Vehicles: https://ieeexplore.ieee.org/document/9129849

### Optical Flow Cameras:

    - Specialized cameras that directly measure the apparent motion of pixels between consecutive frames.
    - Provide information about object movement and scene dynamics without explicit depth estimation.
    - Useful for tasks like motion tracking, object segmentation, and video stabilization.

Applications of Optical Flow in Computer Vision: https://charlesnimo.me/project/computer-vision/

### Choosing the Right Camera:

The selection of a camera for computer vision applications depends on various factors, including:

    - Task requirements: Depth perception, motion analysis, or high-speed imaging.
    - Cost and complexity: Monocular cameras are generally more affordable, while stereo and event cameras might involve higher costs and processing demands.
    - Environmental conditions: Consider lighting variations, dynamic scenes, and operational requirements.

By understanding the strengths and limitations of different camera technologies, computer vision practitioners can make informed decisions to capture the most suitable visual data for their specific tasks.
Sources 


## Challenges in Computer Vision
### Low-level challenges (Image formation and transformation):

    - Illumination variations: Images can be captured under different lighting conditions, significantly affecting object appearance and color information.
    - Noise and artifacts: Sensor noise, compression artifacts, and other distortions can hinder accurate feature extraction and analysis.
    - Occlusion and clutter: Objects may be partially hidden or obscured by other objects, making it difficult to identify and segment them.

### Mid-level challenges (Reconstruction):

    - 3D scene reconstruction: Recovering the 3D structure of a scene from 2D images is a complex task due to limitations in depth perception and missing information.
    - Motion estimation and tracking: Accurately tracking moving objects across consecutive frames requires dealing with factors like motion blur, occlusion, and camera movement.

### High-level challenges (Recognition and understanding):

    - Object recognition ambiguity: Differentiating between visually similar objects or objects in unusual poses can be challenging for computer vision algorithms.
    - Scene interpretation: Understanding the context and relationships between objects in a scene requires incorporating knowledge and reasoning beyond basic object recognition.
    - Scalability and robustness: Computer vision systems need to be robust to handle diverse real-world scenarios with varying image quality, content, and environmental condition

## Overview of Common Computer Vision Algorithms:

### Image Filtering and Enhancement:

    - Gaussian Filter: Blurs the image to remove noise and smoothens edges.
    - Median Filter: Replaces each pixel with the median value of its neighborhood, effective for removing salt-and-pepper noise.
    - Canny Edge Detector: Detects edges based on gradient magnitude and direction, widely used for feature extraction.
    - Sobel Filter: Calculates the image gradient in horizontal and vertical directions, useful for edge detection and feature orientation estimation.

### Feature Extraction and Matching:

    - Scale-Invariant Feature Transform (SIFT): Identifies and describes keypoints in images that are invariant to scale, rotation, and illumination changes.
    - Speeded Up Robust Features (SURF): Similar to SIFT but faster to compute, often used for real-time applications.
    - Histogram of Oriented Gradients (HOG): Represents local object appearance based on the distribution of oriented gradients, effective for pedestrian detection.
    - Local Binary Patterns (LBP): Captures local spatial patterns of intensity variations, useful for texture analysis and object recognition.

### Image Segmentation and Representation:

    - Thresholding: Segments the image based on a single intensity threshold, suitable for simple foreground-background separation.
    - K-means Clustering: Groups pixels with similar features into clusters, often used for image segmentation and color quantization.
    - Graph Cut: Segments the image by minimizing an energy function based on pixel similarities and boundary smoothness, effective for complex object boundaries.
    - Watershed Algorithm: Segments the image by simulating water flooding from regional minima, useful for separating overlapping objects.

### Image Matching and Registration:

    - Template Matching: Compares a template image to different regions of a larger image to find similar patterns.
    - Optical Flow: Estimates the apparent motion of pixels between consecutive video frames, useful for motion tracking and object analysis.
    - Image Pyramids: Represents an image at different resolutions, facilitating scale-invariant feature matching and object detection across varying scales.
    - Feature Transforms: Transform features extracted from one image to another for matching and registration purposes, such as SIFT and SURF descriptors.

### Object Recognition and Classification:

    - Support Vector Machines (SVM): Classifies objects based on learned decision boundaries in a high-dimensional feature space.
    - Convolutional Neural Networks (CNNs): Deep learning models that automatically learn hierarchical feature representations for robust object recognition and classification.
    - Object Detection Frameworks: Pre-trained deep learning models like YOLO, R-CNN, and SSD, used for real-time object detection and localization in images and videos.

6. Additional Algorithms:

    Homography Estimation: Computes the transformation matrix between two images of the same scene captured from different viewpoints.
    Structure from Motion (SfM): Reconstructs the 3D structure of a scene from multiple images, useful for robotics and augmented reality applications.

The list is long, but these cover the major areas and the common names you might come across in CV literature. For further reading, please refer the book mentioned earlier. 

# Expected Submission
Considering your own research work, pick a non-ML algorithm from the CV book and write a two page approach on why is it relevant and how you plan to use it. 

