# 🕒 AI Face Attendance System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://face-recognition-attendance-system-git.streamlit.app/)

A modern, web-based attendance tracking application using **Facial Recognition**. This system allows users to "Punch In" and "Punch Out" using their webcam, with all data logged into a downloadable CSV report.

## ✨ Features
* **👤 User Registration:** Capture and save new faces to the database instantly.
* **🕒 Punch In/Out:** Track arrival and departure with a simple toggle and scan.
* **🤖 Deep Learning:** Powered by **DeepFace** (VGG-Face) for high-accuracy recognition.
* **📊 Live Activity Feed:** View recent logs directly on the web interface.
* **📥 Excel Export:** Download a complete attendance report for record-keeping.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Engine:** [DeepFace](https://github.com/serengil/deepface)
* **Image Processing:** OpenCV
* **Data Management:** Pandas

## 📝 Usage
1. Open the app via the Streamlit link.

2. Use "Register New User" to add your face to the system.

3. Use "Log Attendance" to clock in or out.

4. Go to "View Logs" to see the history and download the Excel file.

## 🚀 Local Setup

If you want to run this project on your own machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/face-attendance.git](https://github.com/YOUR_USERNAME/face-attendance.git)
   cd face-attendance

2. **Install dependencies:**
pip install -r requirements.txt

3. **Run the app:**
python3 -m streamlit run app_streamlit.py

## Built with ❤️ using Python and Streamlit.
