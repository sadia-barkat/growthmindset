import streamlit as st
import datetime
import random

# Title of the Web App
st.title("🧠 Mindset Goals App!!")

# Sidebar with Name and Qualification Inputs
st.sidebar.header("👤 User Information")
name = st.sidebar.text_input("✍️ Enter your name:", "")
qualification = st.sidebar.selectbox("🎓 Select your qualification:", ["Matriculation", "Bachelors", "Masters"])

time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
st.sidebar.write(f"📅 Current Date & Time: {time}")

# Main Page Content
st.header("🏆 Set Your Mindset Goals")
st.subheader("💡 Daily Habits")

# Checkboxes for goals
goal1 = st.checkbox("🙏 Practice Gratitude")
goal2 = st.checkbox("🏋️‍♂️ Exercise Regularly")
goal3 = st.checkbox("📖 Read a Book")
goal4 = st.checkbox("🧘 Meditate for 10 Minutes")
goal5 = st.checkbox("📝 Plan the Day Ahead")

# Study & Behavior Goals
st.subheader("📚 Study & Behavior Goals")
study1 = st.checkbox("✅ Complete Homework/Assignments")
study2 = st.checkbox("📑 Revise Notes Daily")
study3 = st.checkbox("🎯 Learn a New Skill")
study4 = st.checkbox("📵 Limit Screen Time")
study5 = st.checkbox("💬 Practice Effective Communication")

# Progress Bar based on completed goals
completed_goals = sum([goal1, goal2, goal3, goal4, goal5, study1, study2, study3, study4, study5])
st.progress(completed_goals / 10)
st.write(f"🎯 You've completed {completed_goals} out of 10 goals today! Keep it up! 🚀")


# Motivational Quote Section
st.markdown("---")
st.subheader("🌟 Motivational Quote")
quotes = [
    "💡 *The only way to do great work is to love what you do.* - Steve Jobs",
    "🔥 *Believe you can and you're halfway there.* - Theodore Roosevelt",
    "🏅 *Success is not final, failure is not fatal: It is the courage to continue that counts.* - Winston Churchill",
    "⏳ *Don't watch the clock; do what it does. Keep going.* - Sam Levenson",
    "🌍 *Act as if what you do makes a difference. It does.* - William James",
    "📖 *Education is the most powerful weapon which you can use to change the world.* - Nelson Mandela",
    "💪 *Discipline is the bridge between goals and accomplishment.* - Jim Rohn"
]
st.write(random.choice(quotes))

# Footer
st.sidebar.text("Stay Motivated! 🚀")