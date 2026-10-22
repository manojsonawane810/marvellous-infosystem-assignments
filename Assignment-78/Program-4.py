import streamlit as st

st.title("Student Result calculator")

st.header("Provide Student Name, Marks of subjects")

name = st.text_input("Enter student name")
mathMarks = st.number_input("Enter marks obtained in Mathematics", value = 0.00, min_value=0.00, max_value=100.00)
englishMarks = st.number_input("Enter marks obtained in English", value = 0.00, min_value=0.00, max_value=100.00)
scienceMarks = st.number_input("Enter marks obtained in Science", value = 0.00, min_value=0.00, max_value=100.00)

st.text("Check if Student is passed or failed in any subject")
checkBt = st.button("Check")

if checkBt:
    if mathMarks < 40 or englishMarks < 40 or scienceMarks < 40:
        st.error("Student "+ name + " is failed in some subject(s)")
    else:
        st.success("Student " + name + " is passed")

st.text("Calculate total marks obtained in all subjects")
calcTotal = st.button("Calculate Total")

if calcTotal:
    total = mathMarks + englishMarks + scienceMarks
    st.write("Total marks of student " + name + " are : " + str(total))

calcPer = st.button("Calculate percentage")

if calcPer:
    mean = (mathMarks + englishMarks + scienceMarks) / 3
    st.write("Percentages of student " + name+ " are : " + str(mean) + "%")
