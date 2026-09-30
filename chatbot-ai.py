"""import streamlit as st

st.header("welcome to chatbot application")
st.write("message")
st.write ("name:vivek kumar")
st.write ("roll no.- 106")
st.text("text here normal")
#button 
st.button("click me")
st.write("button clicked")
st.text_input("Enter your messege here")##"""
import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Select operation
operation = st.selectbox(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2

    elif operation == "Subtraction":
        result = num1 - num2

    elif operation == "Multiplication":
        result = num1 * num2

    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result = {result}")