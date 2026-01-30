# 🕒 AI Face Attendance System

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

## 📂 Project Structure
* app_streamlit.py - The main application logic.

* requirements.txt - List of Python libraries required.

* dataset/ - Directory storing registered user face images.

* attendance.csv - The local log file for attendance records.

* .gitignore - Prevents junk files from being uploaded to GitHub.

## 📝 Usage
1. Open the app via the Streamlit link.

2. Use "Register New User" to add your face to the system.

3. Use "Log Attendance" to clock in or out.

4. Go to "View Logs" to see the history and download the Excel file.

## Built with ❤️ using Python and Streamlit.

---

### How to add this in VS Code:
1. Create a new file named `README.md`.
2. Paste the code above into it.
3. Save the file.
4. Run these terminal commands to send it to GitHub:
   ```bash
   git add README.md
   git commit -m "Add professional README"
   git push origin main