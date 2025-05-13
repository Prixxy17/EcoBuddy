
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import datetime
import random


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


model = genai.GenerativeModel("gemini-2.0-flash-lite")
chat = model.start_chat(history=[])


def get_gemini_response(question):
    return chat.send_message(question, stream=True)


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

SUSTAINABLE_DEVELOPMENT_GOALS = [
"1) No Poverty",
"2) Zero Hunger",
"3) Good Health and Well-being",
"4) Quality Education",
"5) Gender Equality",
"6) Clean Water and Sanitation",
"7) Affordable and Clean Energy",

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




st.set_page_config(page_title="EcoBuddy", page_icon="🧚‍♀️")

st.markdown("""
    <style>
            .stApp {
    background: url("https://plus.unsplash.com/premium_photo-1673292293042-cafd9c8a3ab3?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    color: #e8f5e9;
    font-family: 'Segoe UI', sans-serif;
            .stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(10, 20, 10, 0.6);
    z-index: -1;


}

}

        }

        .stSidebar {
            background-color: #142f22 !important;
            color: #ffffff;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .stTextInput > div > input {
            background-color: #1f3d2c;
            color: #ffffff;
            border: 1px solid #4caf50;
        }

        .stButton > button {
    background-color: #4CAF50;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    transition: all 0.3s ease-in-out;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    padding: 0.6rem 1.2rem;
}

.stButton > button:hover {
    background-color: #66BB6A;
    transform: translateY(-4px) scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
}

        }

        .stInfo, .stSuccess, .stWarning, .stError {
            border-radius: 10px;
            padding: 10px;
        }

        h1, h2, h3, h4 {
            color: #a5d6a7;
        }

        .css-1v3fvcr {
            color: #e0f2f1;
        }

        a {
            color: #81d4fa;
        }
    </style>
""", unsafe_allow_html=True)
st.title("🧚‍♀️ EcoBuddy: Your Climate Action Fairy")


import streamlit as st

st.markdown(
    "<p style='font-size:24px; white-space:nowrap;'>Set the tone for your EcoBuddy journey! </p>",
    unsafe_allow_html=True
)


import streamlit as st


audio_file_path = 'C:/Users/Prixxy/Desktop/python/EcoBuddy/nature_sound.mp3'


st.audio(audio_file_path, format='audio/mp3')



st.sidebar.header("🌪️ Climate Myths Busted")
for myth, fact in myth_busters.items():
    with st.sidebar.expander(myth):
        st.write(f"✅ {fact}")


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


user_input = st.text_input("Ask EcoBuddy anything about climate change, eco-tips, or carbon footprint:", key="user_input")
submit = st.button("🌎 Ask EcoBuddy")


if submit and user_input:
    st.session_state['chat_history'].append(("You", user_input))
    response = get_gemini_response(user_input)

    full_response = ""
    for chunk in response:
        full_response += chunk.text
    st.subheader("🧚 EcoBuddy Says:")
    st.write(full_response)
    st.session_state['chat_history'].append(("EcoBuddy", full_response))


st.subheader("📜 Chat History")
for role, text in st.session_state['chat_history']:
    st.write(f"**{role}:** {text}")

import random
import streamlit as st


nature_quiz = {
    "What is the largest rainforest in the world?": ["Amazon Rainforest", "Congo Rainforest", "Sundarbans", "Valdivian Temperate Rainforest"],
    "Which of the following animals is known as the 'King of the Jungle'?": ["Lion", "Tiger", "Elephant", "Giraffe"],
    "What is the tallest tree species in the world?": ["Coast Redwood", "Sequoia", "Douglas Fir", "Blue Spruce"],
    "Which country is home to the Great Barrier Reef?": ["Australia", "Brazil", "Philippines", "South Africa"],
    "What percentage of the Earth's surface is covered by oceans?": ["71%", "50%", "80%", "64%"]
}


if 'question' not in st.session_state:
    st.session_state['question'], st.session_state['options'] = random.choice(list(nature_quiz.items()))
    st.session_state['submitted'] = False
    st.session_state['selected_answer'] = None
    st.session_state['quiz_done'] = False  


st.subheader("🌳 Nature Quiz")
st.write(f"**Question:** {st.session_state['question']}")


answer = st.radio("Choose your answer:", st.session_state['options'], key="answer")


submit_answer = st.button("Submit Answer")


if submit_answer and not st.session_state['submitted']:
    st.session_state['selected_answer'] = answer
    st.session_state['submitted'] = True

    
    if answer == st.session_state['options'][0]:  
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect! The correct answer is: {st.session_state['options'][0]}")


if st.session_state['submitted'] and not st.session_state['quiz_done']:
    next_button = st.button("Next Question")
    
   
    if next_button:
        
        st.session_state['question'], st.session_state['options'] = random.choice(list(nature_quiz.items()))
        st.session_state['submitted'] = False 
        st.session_state['selected_answer'] = None  



st.subheader("🌱 Daily Eco Tip")
st.info(random.choice(eco_tips))

st.subheader("🌍 UN Sustainable Development Goals")
for goal in SUSTAINABLE_DEVELOPMENT_GOALS:
    st.write(f"✅ {goal}")



st.subheader("💡 Climate Hero Story")
st.success(random.choice(inspiring_stories))


st.subheader("📊 Track Your Carbon Footprint")
st.markdown("👉 *Estimate your daily carbon footprint using [this calculator](https://www.carbonfootprint.com/calculator.aspx) and try to reduce it step-by-step.*")
st.subheader("🎯 Eco Mission of the Day")
st.warning(random.choice(eco_missions))


st.subheader("📰 Climate News")
for news in climate_news_samples:
    st.write(f"- {news}")
