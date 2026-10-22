import streamlit as st

st.title("Celcius to Fahrenheit conversion")

st.header("Please provide temperator value in Celcius")

temp = st.number_input("Enter temperature value", value = 0.0, step = 0.1)

convertBt = st.button("Convert")

if convertBt:
    tempInF = (temp * 1.8) + 32

    st.write(f"Temperature in Fahrenheit is : {tempInF:.4f}")
    st.success(f"{tempInF:.3f}")
    st.success("{:.2f}".format(tempInF))