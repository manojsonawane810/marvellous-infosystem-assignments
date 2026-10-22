import streamlit as st

st.title("Interest calculator")

st.header("Provide principle amount, rate of interest and tenure")

amount = st.number_input("Enter principle amount", value=1000.0, step = 100.0)
interest = st.number_input("Enter interest amount", value=7.5, step= 0.1)
tenure = st.number_input("Enter tenure in days", value=1, step=1)

tenureYears = tenure / 365

calBt = st.button("Calculate")

if calBt:
    totalInt = (amount * interest * tenureYears) / 100

    st.write(f"Total interest is : {str(totalInt)}")