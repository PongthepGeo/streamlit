# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

from scipy import stats
from datetime import datetime

# Read the CSV file
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

df_1 = load_data('raw_data/plot_distribution.csv')
colors = {'2021': 'orange', '2022': 'green', '2023': 'black'}

st.subheader(f'Score Distribution Each Year')
fig, ax = plt.subplots()
for column in df_1.columns:
    data = df_1[column].dropna()  
    kde = sns.kdeplot(data, ax=ax, color=colors[column], label=column)
    x, y = kde.get_lines()[-1].get_data()  
    peak_estimate = x[np.argmax(y)]  
    ax.axvline(peak_estimate, color=colors[column], linestyle='--')
plt.xlabel('Score')
plt.legend()
st.pyplot(fig)

table_data = load_data('raw_data/table.csv')
st.table(table_data)

# Create a selectbox for user to select a name
name = st.selectbox("เลือกชื่อ:", ('พงศ์เทพ',
                                'ศาสตราจารย์ ดร.จักรพันธ์ สุทธิรัตน์',
                                'ศาสตราจารย์ ดร.มนตรี ชูวงษ์',
                                'ศาสตราจารย์ ดร.ศรีเลิศ โชติพันธรัตน์',
                                'ศาสตราจารย์ ดร.พิษณุพงศ์ กาญจนพยนต์',
                                'ศาสตราจารย์ ดร.สันติ ภัยหลบลี้',
                                'รองศาสตราจารย์ ดร.ฐานบ ธิติมากร',
                                'รองศาสตราจารย์ ดร.ฐาสิณีย์ เจริญฐิติรัตน์',
                                'รองศาสตราจารย์ ดร.ปิยพงษ์ เชนร้าย',
                                'รองศาสตราจารย์ ดร.สกลวรรณ ชาวไชย',
                                'ผู้ช่วยศาสตราจารย์ ดร.อัคนีวุธ จิรภิญญากุล',
                                'ผู้ช่วยศาสตราจารย์ ดร.วิชัย จูฑะโกสิทธิ์กานนท์',
                                'ผู้ช่วยศาสตราจารย์ ดร.ฐิติพรรณ อัศวินเจริญกิจ',
                                'ผู้ช่วยศาสตราจารย์ ดร.กันตภณ สุระประสิทธิ์',
                                'ผู้ช่วยศาสตราจารย์ ดร.สุคนธ์เมธ จิตรมหันตกุล',
                                'ผู้ช่วยศาสตราจารย์ ดร.อลงกต ฝั้นกา',
                                'อาจารย์ ดร.สุเมธ พันธุวงค์ราช'
                                ))

# Create a radio button for user input
status = st.radio("ความเห็น:", ('ไม่ออกความเห็น', 'อนุมัติ', 'ไม่อนุมัติ'))

# # Create a list for 'Approved' and 'Unapproved' choices for each name
# if 'status_names' not in st.session_state:
#     st.session_state['status_names'] = {'ไม่ออกความเห็น': [],
#                                         'อนุมัติ': [],
#                                         'ไม่อนุมัติ': []}

# # Create a button for submitting the form
# if st.button('Submit'):
#     # Update the list based on the user's choice
#     st.session_state['status_names'][status].append(name)
#     log_message = f"{datetime.now()}: User selected {name} and clicked {status}"

#     # Print the log message to the terminal
#     print(log_message)

#     # Write the log message to a file
#     with open('log.txt', 'a') as f:
#         f.write(log_message + '\n')

#     # Display the names
#     st.subheader('รายชื่อไม่ออกความเห็น')
#     st.write(', '.join(st.session_state['status_names']['ไม่ออกความเห็น']))
#     st.subheader('รายชื่ออนุมัติ')
#     st.write(', '.join(st.session_state['status_names']['อนุมัติ']))
#     st.subheader('รายชื่อไม่อนุมัติ')
#     st.write(', '.join(st.session_state['status_names']['ไม่อนุมัติ']))

# if 'status_names' not in st.session_state:
#     st.session_state['status_names'] = {
#         'ไม่ออกความเห็น': [],
#         'อนุมัติ': [],
#         'ไม่อนุมัติ': []
#     }

import os 

# Read the existing log file and populate session state
if 'status_names' not in st.session_state:
    st.session_state['status_names'] = {
        'ไม่ออกความเห็น': [],
        'อนุมัติ': [],
        'ไม่อนุมัติ': []
    }

    # Populate the state with existing data if log.txt exists
    if os.path.isfile('log.txt'):
        with open('log.txt', 'r') as f:
            for line in f:
                # Assuming log_message structure is "{timestamp}: User selected {name} and clicked {status}"
                parts = line.split("User selected ")
                if len(parts) >= 2:
                    name_status_parts = parts[1].split(" and clicked ")
                    if len(name_status_parts) == 2:
                        name_from_file = name_status_parts[0].strip()
                        status_from_file = name_status_parts[1].strip()
                        st.session_state['status_names'][status_from_file].append(name_from_file)

if st.button('Submit'):
    # Update the dictionary based on the user's choice
    st.session_state['status_names'][status].append(name)
    log_message = f"{datetime.now()}: User selected {name} and clicked {status}"

    # Print the log message to the terminal
    print(log_message)

    # Write the log message to a file
    with open('log.txt', 'a') as f:
        f.write(log_message + '\n')

    # Display the names
    st.subheader('รายชื่อไม่ออกความเห็น')
    st.write(', '.join(st.session_state['status_names']['ไม่ออกความเห็น']))
    num_approved = len(st.session_state['status_names']['อนุมัติ'])
    # print(f"There are {num_approved} approved names.")
    st.subheader(f"รายชื่ออนุมัติ {num_approved}/17")
    st.write(', '.join(st.session_state['status_names']['อนุมัติ']))
    st.subheader('รายชื่อไม่อนุมัติ')
    st.write(', '.join(st.session_state['status_names']['ไม่อนุมัติ']))