import streamlit as st
import pandas as pd
import os
import glob

csv_files = glob.glob("Attendance_*.csv")
attendance_data = {}

for file in csv_files:
    date_str = file.split("_")[1].split(".")[0]
    date = pd.to_datetime(date_str, format="%d-%m-%Y").date()
    attendance_data[date] = pd.read_csv(file)

st.title("Attendance Records")

if attendance_data:
    selected_date = st.selectbox("Select Date", sorted(attendance_data.keys()), format_func=lambda x: x.strftime("%d-%m-%Y"))
    if selected_date in attendance_data: 
        st.write(f"Attendance for {selected_date.strftime('%d-%m-%Y')}:")
        st.dataframe(attendance_data[selected_date].style.highlight_max(axis=0))
else:
    st.info("No attendance records found.")