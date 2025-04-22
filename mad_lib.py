import streamlit as st
import random

st.title("Mad Libs Fun 🎉")
st.sidebar.header("Fill in the blanks ✍️")

adjective = st.sidebar.text_input("Enter an adjective", "fantastic")
action1 = st.sidebar.text_input("Enter a Verb:", "program")
action2 = st.sidebar.text_input("Enter another Verb:", "build")
celebrity = st.sidebar.text_input("Enter a Famous Person:", "Elon Musk")

# Fun Sentences to Make it More Interesting
madlib_templates = [
    f"Computer programming is so {adjective}! It makes me so excited all the time because I love to {action1}. Stay hydrated and {action2} like you are {celebrity}!",
    f"The world of AI is {adjective}! Every day, I wake up and {action1}, hoping to {action2} like {celebrity}.",
    f"Success is {adjective}. If you want to be like {celebrity}, you must {action1} every day and never forget to {action2}!"
]

# Button to Generate Mad Libs
if st.button("Generate Mad Lib 🥳"):
    selected_madlib = random.choice(madlib_templates)
    st.subheader("Here's Your Mad Lib! 🎊")
    st.write(selected_madlib)

# Footer
st.markdown("Made by Hamza Syed~")
