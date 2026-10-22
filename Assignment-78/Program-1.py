import streamlit as st

st.title("Addition of Numbers")
st.header("Sum Calculation")

no1 = st.number_input("Enter first number", value = 0.0, step = 1.0)
no2 = st.number_input("Enter second number", value = 0.0, step = 1.0)

add = st.button("Add")

if add:
    sum = no1 + no2
    st.success("Addition of numbers is " + str(sum))

