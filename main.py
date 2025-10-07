import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("marksheet.csv")

st.title("📚 student performance analyzer")

age = ["All"] + sorted(data["Age"].unique())
gender = ["All"] + sorted(data["Gender"].unique())
sections = ["All"] + sorted(data["Section"].unique())
with st.sidebar:
    selectedsections = st.selectbox("selectetd sections ",sections)
    gender = st.selectbox("selected gender ",gender)
    age = st.selectbox("selected age ", age)
    sectionsdata = data["Section"]
    filtereddata = ""

    if selectedsections =="All" :
        filtereddata = data
    else:
        filtereddata = data.loc[data["Section"]==selectedsections]

    if gender != "All" :
        filtereddata = filtereddata.loc[data["Gender"]==gender]

    if age != "All" :
        filtereddata = filtereddata.loc[data["Age"]==age]

avgmarks = filtereddata[["Maths","Science","English","History"]].mean()

st.write(f"### maths average :{avgmarks["Maths"]:.2f}")
st.write(f"### history average :{avgmarks["History"]:.2f}")
st.write(f"### science average :{avgmarks["Science"]:.2f}")
st.write(f"### english average :{avgmarks["English"]:.2f}")      
avgmarks.plot(kind="bar",color="#8A96A2")
plt.ylabel("marks")
plt.xlabel("subjects")
st.pyplot(plt)


st.dataframe(filtereddata)  
