# WordLens
# 📚 Real-Time Word Meaning Extractor

A computer vision and machine learning-powered tool developed by a team of three. This project enables users to retrieve real-time meanings of words from physical or digital text material simply by pointing at the word — helping to maintain focus and reduce distractions during reading.

---

## 🚀 Features

- 📷 Real-time word detection using a webcam
- 🔍 Meaning extraction from pointed words
- 🧠 Powered by YOLOv5 for object detection
- 📝 OCR using EasyOCR for text recognition
- 🤖 Improves reading focus by avoiding constant lookup distractions

---

## 🛠️ Tech Stack

- **Object Detection**: YOLOv5 (via PyTorch)
- **OCR**: EasyOCR
- **Language**: Python
- **Libraries**: OpenCV, EasyOCR, PyTorch

---

## 📸 Overview

1. The user points at a word in the text material (e.g., book or screen).
2. YOLOv5 detects the pointing gesture or word region.
3. EasyOCR extracts the text from the detected region.
4. The program searches for the word’s meaning in a local or predefined dictionary.
5. The meaning is displayed in real-time (via terminal or overlay).

---

## 🧑‍💻 Team

- Satya Pandian
- Sudhindra Devulapalli https://github.com/sudhindra01
- Vaibhav Vemani https://github.com/vaibhavvemani

---

## 📂 Project Structure

WordLens/
│
├── yolo_weights/            # Pretrained YOLOv5 weights
│
├── Dictionary.py            # Local dictionary module (for meaning lookup)
├── EasyOCR.py               # OCR implementation using EasyOCR
├── FindWord.py              # Logic to detect and extract the target word
├── PointDetection.py        # YOLO-based hand/finger detection
├── WordDisplay.py           # Displays word and its meaning on screen
├── main.py                  # Entry point for the application
│
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

---

## ✅ Future Improvements

Multi-language support
GUI for a more intuitive experience
Eye-piece camera integration
Mobile app integration
Enhanced detection of hand gestures or finger pointing
