from dotenv import load_dotenv
# Load All the envirenment variaables
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure our API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load google gemini model and provide sql query as response


def get_response(quesion,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],quesion])
    return response.text

# Function to retrive query from the sql database
def get_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)

    return rows


## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_response(question,prompt)
    print(response)
    response=get_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)