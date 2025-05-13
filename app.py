from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import datetime
import random

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-2.0-flash-lite")
chat = model.start_chat(history=[])

# Function to get Gemini response
def get_gemini_response(question):
    return chat.send_message(question, stream=True)

# EcoBuddy helper content
eco_tips = [
    "Turn off lights when not in use.",
    "Use reusable water bottles instead of plastic ones.",
    "Unplug electronics when you're not using them.",
    "Compost your food waste.",
    "Plant a tree or support reforestation projects.",
    "Switch to energy-efficient appliances.",
    "Reduce meat consumption to lower carbon emissions.",
    "Take public transportation or bike instead of driving."
]

inspiring_stories = [
    "A small village in India transformed its landscape by planting over 1 million trees!",
    "A 16-year-old in Sweden started a global youth movement to demand climate action!",
    "A city in Germany now runs on 100% renewable energy!"
]

myth_busters = {
    "Electric cars are worse for the environment than gas cars.": "Myth! While battery production emits CO2, EVs have a lower lifetime footprint.",
    "Climate change is just a natural cycle.": "False! Current changes are largely driven by human activity.",
    "One person can't make a difference.": "Wrong! Collective individual actions make a massive difference."
}

climate_news_samples = [
    "🌍 Scientists report April 2025 as one of the warmest months on record.",
    "🌀 Atlantic hurricane season expected to intensify due to warming oceans.",
    "🌱 A new law in the EU pushes for carbon-neutral buildings by 2030."
]

eco_missions = [
    "🌿 Challenge: Go plastic-free for one day!",
    "🚴 Eco Mission: Bike or walk instead of using a car for short trips today.",
    "🛒 Task: Buy local produce this week to cut carbon emissions from transport."
]

# Streamlit App Configuration
st.set_page_config(page_title="EcoBuddy", page_icon="🧚‍♀️")
st.title("🧚‍♀️ EcoBuddy: Your Climate Action Fairy")

# Sidebar with myth busters
st.sidebar.header("🌪️ Climate Myths Busted")
for myth, fact in myth_busters.items():
    with st.sidebar.expander(myth):
        st.write(f"✅ {fact}")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# User Input
user_input = st.text_input("Ask EcoBuddy anything about climate change, eco-tips, or carbon footprint:", key="user_input")
submit = st.button("🌎 Ask EcoBuddy")

# Handle user question
if submit and user_input:
    st.session_state['chat_history'].append(("You", user_input))
    response = get_gemini_response(user_input)

    full_response = ""
    for chunk in response:
        full_response += chunk.text
    st.subheader("🧚 EcoBuddy Says:")
    st.write(full_response)
    st.session_state['chat_history'].append(("EcoBuddy", full_response))

# Chat history display
st.subheader("📜 Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"**{role}:** {text}")

# Daily Tip
st.subheader("🌱 Daily Eco Tip")
st.info(random.choice(eco_tips))

# Inspiring Story
st.subheader("💡 Climate Hero Story")
st.success(random.choice(inspiring_stories))

# Carbon Footprint Prompt
st.subheader("📊 Track Your Carbon Footprint")
st.markdown("👉 *Estimate your daily carbon footprint using [this calculator](https://www.carbonfootprint.com/calculator.aspx) and try to reduce it step-by-step.*")

# Quiz / Challenge
st.subheader("🎯 Eco Mission of the Day")
st.warning(random.choice(eco_missions))

# Climate News
st.subheader("📰 Climate News")
for news in climate_news_samples:
    st.write(f"- {news}")
