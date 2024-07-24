# 🚗 Peekaboo: The Smart Car Mirror 🚗

Welcome to **Peekaboo**, an innovative IoT project developed as part of Reichman University's milab - Media Innovation Lab. Peekaboo is a smart car mirror designed to encourage eye contact between parent and child during car journeys, promoting engagement and interaction in a unique and effective way.

Our site: https://lihirosenwasser.wixsite.com/milab

<img src="https://github.com/user-attachments/assets/68f32f41-488e-4e5c-bce9-e091206a9ce3" alt="Peekaboo Hardware Design" width="600" height="400">


<img src="https://github.com/user-attachments/assets/abf26227-2d8a-40fc-bcce-8d8a29d534ea" alt="Peekaboo " width="600" height="400">
  
<img src="https://github.com/user-attachments/assets/ba1cb909-6941-447c-b628-ddab46197caf" alt="Peekaboo " width="600" height="400">


## Demonstration Video

You can watch a demonstration of the Peekaboo project in action by following this link:

- [Watch the Peekaboo Demo Video on YouTube](https://youtu.be/OVUpmxSjGho)
  
<a href="https://youtu.be/OVUpmxSjGho" target="_blank">
  <img src="https://img.youtube.com/vi/OVUpmxSjGho/maxresdefault.jpg" alt="Peekaboo Demo Video" width="300" height="169">
</a>


## Introduction

Peekaboo is more than just a mirror. It's an interactive tool that strengthens the bond between parents and children by enhancing their interaction during car rides. With its advanced pupil detection sensors, Peekaboo monitors the child's gaze and ensures that eye contact is maintained. If eye contact is lost for more than 60 seconds, the mirror uses precise motorized movements to regain attention, keeping the child engaged without causing discomfort.

## Features

- **Real-Time Gaze Detection:** Utilizing cutting-edge computer vision technology to track the child's gaze direction accurately.
- **Motorized Adjustments:** Automatically adjusts the mirror to recapture the child's attention if eye contact is lost.
- **Interactive Feedback:** Provides visual cues to encourage interaction between parent and child.


## Hardware and Software

### Hardware Components

- **Raspberry Pi 4:** Serves as the main processing unit for running the gaze detection algorithms.
- **3D Printed Components:** Custom-designed parts for housing the electronics and ensuring seamless integration into your vehicle.
- **Sensors:** Advanced sensors to accurately detect and track eye movement.

### Software Components

- **Python 3.11:** The main programming language used in this project.
- **OpenCV:** For image processing and computer vision tasks.
- **MediaPipe:** For efficient face and gaze detection.


### File Descriptions

- **`gaze_redCircule.py`**: This script handles the initial setup for gaze tracking, including camera initialization and basic configurations for pupil detection.
- **`main.py`**: The main entry point of the project, responsible for initiating the gaze detection and mirror control processes.
- **`mirror_controller.py`**: This script contains the logic for controlling the mirror's motorized adjustments based on the gaze data received.
- **`Gaze_pose.py`**: Implements the gaze direction estimation algorithm using the MediaPipe and OpenCV libraries.

## Installation

### Prerequisites

- **Python 3.11** or higher
- **OpenCV**: Install using `pip install opencv-python`
- **MediaPipe**: Install using `pip install mediapipe`


# Inspiration and Credits

The development of the Gaze Direction Estimation Algorithm in the Peekaboo project was inspired by the innovative work of a student from Stevens Institute of Technology in Hoboken, New Jersey. This remarkable algorithm focuses on detecting the precise direction of the pupils rather than analyzing the entire face, which significantly enhances accuracy and performance in real-world applications.

The original project laid a strong foundation for our implementation, offering valuable insights into pupil tracking techniques. The student behind this work has provided a comprehensive document that explains the architecture and methodology in detail. You can access this document and explore the original project on GitHub:

- **Architecture Document**: [View the Document](https://github.com/matthullstrung/gaze-estimation)
- **GitHub Repository**: [Gaze Estimation Project](https://github.com/matthullstrung/gaze-estimation)

Additionally, for a better understanding of the algorithm's functionality, you can watch a demonstration video here:  
- **Demonstration Video**: [Watch the Video](https://www.youtube.com/watch?v=BFOO-_9tMn4)

The inspiration and knowledge gained from this project have been instrumental in shaping the design and functionality of Peekaboo, allowing us to create a smart car mirror that effectively enhances parent-child interaction through advanced gaze tracking technology.
