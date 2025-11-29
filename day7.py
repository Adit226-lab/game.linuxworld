
import streamlit as st
import pandas as pd
import matplotlib as plt
st.title("i'm aditya :")
st.text("i m tall")
st.header("Going Forward")
st.write("you can write :",10+5)
name = st.text_input("enter your nname :")
age = st.number_input("enter your age :")
st.write(" your name is :","your age is :",age)
st.selectbox("enter your course",["BCA","BTECH"])
if st.button("CLICK ME"):
    st.success("Clicked button")
file = st.file_uploader("upload your file")
if file:
    content = file.read
    st.write("file uploaded successfully")

data = {"name":["tom","adi","jack"], "Marks": [10,20,30]}
df= pd.DataFrame(data)
data = pd.DataFrame({
    "Marks":[10,20,30]
})

st.line_chart(data)
st.bar_chart(data)

subject = ["Python","c++","java"]
marks = [20,10,15]
fig, ax = plt.subplots()
ax.pie(marks,labels=marks)





