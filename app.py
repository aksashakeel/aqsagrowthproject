import streamlit as st

st.set_page_config(page_title="Growth Mindset Project ✨")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("A simple Streamlit app that encourages users to embrace a growth mindset through interactive challenges, motivational quotes, and progress tracking! 🌟")

# Quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("\"Challenges are what make life interesting; overcoming them is what makes life meaningful.\"")

# Challenge input section
st.header("What's Your Challenge Today?")
User_input = st.text_input("Describe a challenge you're facing:")

# Display message based on user input
if User_input:
    st.success(f"💪 You are facing: {User_input}. Keep pushing forward towards your goal!🚀")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection section
st.header("🧠 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"⭐ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past experience helps you grow! Share your difficulties")

# Achievements section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You Achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now!🤩")

# Footer
st.write("- - - ")
st.write("Keep believing in yourself. Growth is a journey, not a destination!")
st.write("©️ Created by Aqsa Shakeel")
