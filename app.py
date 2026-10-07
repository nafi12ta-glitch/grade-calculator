import streamlit as st

st.title("Student Grade Calculator")
st.write("Calculate your overall average and letter grade.")

number_of_subjects = st.number_input(
    "How many subjects do you have?",
    min_value=1,
    max_value=15,
    value=4,
    step=1
)

st.write("### Enter your grades")

total = 0

for i in range(number_of_subjects):
    grade = st.number_input(
        f"Subject {i + 1} grade",
        min_value=0.0,
        max_value=100.0,
        value=90.0,
        step=0.5
    )
    total += grade

if st.button("Calculate Grade"):
    average = total / number_of_subjects

    if average >= 98:
        letter = "A"
    elif average >= 88:
        letter = "B"
    elif average >= 77:
        letter = "C"
    elif average >= 66:
        letter = "D"
    else:
        letter = "F"

    st.success(f"Overall Average: {average:.2f}%")
    st.info(f"Letter Grade: {letter}")
        
