# Eye-Blink-Count
Eye Blink Count
👁️ Eye Blink Detection with Python and OpenCV
A real-time eye blink detection system using facial landmark tracking. This project counts how many times you blink — useful for drowsiness detection, human-computer interaction, health monitoring, and more!

<div align="center"> <img src="https://img.shields.io/badge/OpenCV-RealTime-blue?logo=opencv" /> <img src="https://img.shields.io/badge/dlib-FaceDetection-success?logo=python" /> <img src="https://img.shields.io/badge/Python-3.8+-yellow?logo=python" /> </div>
🎯 Project Overview
This application uses your webcam to detect facial landmarks and measure eye aspect ratio (EAR) to detect blinks. Every time you blink, a counter is incremented. A red "QUIT" button is embedded into the video feed so you can exit the app by clicking it.

🔍 How It Works
Uses Dlib’s 68-point facial landmark detector

Calculates Eye Aspect Ratio (EAR):

If EAR drops below threshold (0.3) for a few consecutive frames → counted as a blink

Real-time frame processing with OpenCV

Built-in GUI button to quit without keyboard

📸 Demo
👁️ Blink and see the counter go up!
🖱️ Click the red "QUIT" button on the screen or press Q to exit.

<p align="center"> <img src="https://media.giphy.com/media/3ov9jExd1O4vDnxrva/giphy.gif" width="400"> </p>
🧠 Dependencies
Python 3.8+

OpenCV

dlib

imutils

scipy

📦 Install Requirements
bash
Copy code
pip install opencv-python dlib imutils scipy
⚠️ Note: Make sure you have the pretrained shape predictor file:

shape_predictor_68_face_landmarks.dat

Place it in the same directory as your script.

🧪 Run the App
bash
Copy code
python blink_counter.py
A window will open showing your webcam feed. Start blinking!

📁 Project Structure
bash
Copy code
.
├── blink_counter.py                      # Main script
├── shape_predictor_68_face_landmarks.dat # Required dlib model (download separately)
└── README.md
⚙️ Eye Aspect Ratio (EAR)
The EAR is calculated using 6 key eye landmarks:

ini
Copy code
EAR = (||p2−p6|| + ||p3−p5||) / (2 * ||p1−p4||)
When the eye is open: EAR is high (around 0.3+)

When blinking: EAR drops below 0.25–0.30

💡 Use Cases
🛑 Drowsiness detection while driving

🖱️ Hands-free interfaces (e.g., blink to click)

🧠 Mental health tracking (fatigue, stress)

🧪 Human-computer interaction research

📌 Future Improvements
Add sound alerts for excessive blinking

Integrate with eye tracking for cursor control

Save blink data to CSV for analytics

🙏 Acknowledgements
Dlib by Davis King

PyImageSearch tutorials

OpenCV and the computer vision community 💻👁️

🧾 License
MIT License. Feel free to modify and share!

✨ Author
[Vedanth] — Building smarter interfaces through computer vision.

Let me know if you’d like this version to include:

Setup with virtual environment

Screenshot/GIF demo

Streamlit or GUI integration (Tkinter/PyQt)

CSV logging for blink stats

I can also generate the requirements.txt for deployment if needed.
