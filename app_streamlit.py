import streamlit as st
import cv2
import numpy as np
from deepface import DeepFace
import os
import pandas as pd
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="AI Attendance System", layout="wide", page_icon="🕒")

# --- INITIALIZATION ---
if not os.path.exists("dataset"):
    os.makedirs("dataset")

LOG_FILE = "attendance.csv"

# --- HELPER FUNCTIONS ---
def save_attendance(name, status):
    """Saves name, timestamp, and Punch status (In/Out) to CSV."""
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame({
        'Name': [name], 
        'Timestamp': [dt_string], 
        'Status': [status]
    })
    
    file_exists = os.path.isfile(LOG_FILE)
    new_entry.to_csv(LOG_FILE, mode='a', index=False, header=not file_exists)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("System Menu")
menu = ["Log Attendance", "Register New User", "📊 View Logs"]
choice = st.sidebar.selectbox("Go to:", menu)

# --- MAIN LOGIC ---
if choice == "Register New User":
    st.header("👤 New User Registration")
    name = st.text_input("Enter Full Name")
    img_file = st.camera_input("Take a registration photo")

    if img_file and name:
        file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)
        cv2.imwrite(f"dataset/{name}.jpg", frame)
        st.success(f"✅ Registered: {name}")

elif choice == "Log Attendance":
    st.header("🕒 Mark Your Attendance")
    
    # --- NEW: PUNCH IN/OUT TOGGLE ---
    status = st.radio("Select Action:", ["Punch In", "Punch Out"], horizontal=True)
    
    st.write(f"Please scan your face to **{status}**")
    check_img = st.camera_input("Verify Identity")

    if check_img:
        file_bytes = np.asarray(bytearray(check_img.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, 1)
        temp_path = "temp_verify.jpg"
        cv2.imwrite(temp_path, frame)

        with st.spinner("Checking Face..."):
            try:
                results = DeepFace.find(img_path=temp_path, db_path="dataset", enforce_detection=False)
                
                if len(results) > 0 and not results[0].empty:
                    full_path = results[0]['identity'][0]
                    user_name = os.path.basename(full_path).split('.')[0]
                    
                    # Log with the selected Status
                    save_attendance(user_name, status)
                    st.balloons()
                    st.success(f"✅ {status} Recorded for {user_name}!")
                else:
                    st.error("❌ Recognition Failed. Are you registered?")
            except Exception as e:
                st.error(f"Error: {e}")
        
        if os.path.exists(temp_path):
            os.remove(temp_path)

elif choice == "📊 View Logs":
    st.header("Attendance Records")
    if os.path.exists(LOG_FILE):
        df = pd.read_csv(LOG_FILE)
        st.dataframe(df, use_container_width=True)

        csv_bytes = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Excel Report",
            data=csv_bytes,
            file_name=f"attendance_{datetime.now().strftime('%Y-%m-%d')}.csv",
            mime="text/csv",
        )
    else:
        st.info("No logs available.")