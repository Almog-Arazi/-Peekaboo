# 🚗 Peekaboo: The Smart Car Mirror 🚗

Welcome to **Peekaboo**, an innovative IoT project developed as part of Reichman University's milab - Media Innovation Lab. Peekaboo is a smart car mirror designed to encourage eye contact between parent and child during car journeys, promoting engagement and interaction in a unique and effective way.


<p align="center">
  <img src="https://github.com/user-attachments/assets/68f32f41-488e-4e5c-bce9-e091206a9ce3" alt="Peekaboo Hardware Design" width="220" height="220">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/abf26227-2d8a-40fc-bcce-8d8a29d534ea" alt="Peekaboo Hardware Design" width="220" height="220">
</p>
![1718980325551](https://github.com/user-attachments/assets/68f32f41-488e-4e5c-bce9-e091206a9ce3)
![image](https://github.com/user-attachments/assets/abf26227-2d8a-40fc-bcce-8d8a29d534ea)

![Peekaboo Logo](https://github.com/user-attachments/assets/68f32f41-488e-4e5c-bce9-e091206a9ce3)

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



