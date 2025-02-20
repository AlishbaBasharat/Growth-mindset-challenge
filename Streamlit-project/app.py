import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", page_icons= "★")

st.title("Growth MindSet Ai Project With Streamlit")

st.header("✈️Welcome to the growth journey!")
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. This Ai-powered app helps you build a grwth mindset with reflection, challenges, and achievements!☆")

#quote section 
st.header("✨ Today's Growth Mindset Quote")
st.write("Believe in yourself, stay consistent, and the world will open doors you never imagined.🚀")

#user input section
st.header("🔧 What's Your challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#Condition
If user_input:
     st.success(f" You're facing: {user_input}. Keep pushing forward towards your goal 💪")
else:
      st.warning("Tell us about your challenge")

#Reflexing
st.header("Reflect on your challenge")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨Great Insights! you're reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! share your difficulties")

#achievements
st.header("🏆 Celebrate you're wins")
achivements = st.text_input("Share something you're recently accomplished:")

if achivements:
    st.success(f"�� Congratulations! You've achieved: {achivements}")
else:
    st.info("Celebrating your achievements can boost your confidence and motivation 🎉")

#footer
st.write("- - -")
st.write("Keep beliving in yourself. Growth is a journey, not a destination! 🤩")
st.write("© Created by Alishba Basharat Ali 🎓")


