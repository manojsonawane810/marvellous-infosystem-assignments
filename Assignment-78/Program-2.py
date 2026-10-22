import streamlit as st

st.title("Check Even or Odd number")
st.header("Number checking application")

no1 = st.number_input("Enter a number", value = 0)

checkBt = st.button("Check")

if checkBt:
    if no1 % 2 == 0:
        st.success("Number " + str(no1) + " is Even number")
    else:
        st.success("Number " + str(no1) + " is Odd number")