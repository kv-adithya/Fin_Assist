import streamlit as st
from chat_logic import get_response
from goal_planner import plan_goal
from recommender import recommend_products
from sip_calculator import show_sip_calculator

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="GenAI Financial Assistant", layout="centered")

# Dark Theme Styling
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #f5f5f5;
    }
    .stApp {
        background-color: #121212;
        font-family: 'Segoe UI', sans-serif;
        color: #f5f5f5;
    }
    section[data-testid="stSidebar"] {
        background-color: #1e1e1e;
        border-right: 1px solid #333;
    }
    .stButton > button {
        background-color: #00c29a;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        margin-top: 0.5rem;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #00a685;
        transform: scale(1.02);
    }
    h1, h2, h3, h4 {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------- 🏠 Home Page -----------------
if "entered_app" not in st.session_state:
    st.session_state.entered_app = False

if not st.session_state.entered_app:
    st.title("🤖 GenAI Financial Assistant")
    st.subheader("Your Personalized AI-Powered Investment Companion")
    
    st.markdown("""
    Welcome to **GenAI Financial Assistant** — a smart, conversational platform to guide you through:

    - 🎓 Learning investment basics  
    - 🎯 Goal planning  
    - 📊 SIP recommendations  
    - 💬 Financial advice via chat  

    ---
    """)
    if st.button("🚀 Enter Assistant"):
        st.session_state.entered_app = True
    st.stop()

# ----------------- 🧭 Navigation -----------------
st.sidebar.markdown("## Navigation")
if "nav" not in st.session_state:
    st.session_state.nav = "Chat"

if st.sidebar.button("💬 Chat"):
    st.session_state.nav = "Chat"
if st.sidebar.button("🎓 Learn Investing"):
    st.session_state.nav = "Learn Investing"
if st.sidebar.button("🎯 Goal Planning"):
    st.session_state.nav = "Goal Planning"
if st.sidebar.button("📊 Recommendations"):
    st.session_state.nav = "Recommendations"
if st.sidebar.button("📈 SIP Calculator"):
    st.session_state.nav = "SIP Calculator"

page = st.session_state.nav

# ---------------------------- 💬 Chat ----------------------------
if page == "Chat":
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask me anything about investing...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = get_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

# ---------------------------- 🎓 Learn Investing ----------------------------
elif page == "Learn Investing":
    st.title("📘 Learn Investing")
    st.subheader("Master the Basics of Investing")

    topics = [
        {"title": "Introduction to Investing", "content": "Investing is the process of putting money into financial instruments like stocks, mutual funds, or bonds to grow your wealth over time."},
        {"title": "Mutual Funds vs Stocks", "content": "Mutual funds pool money from multiple investors, while stocks represent ownership in a single company."},
        {"title": "Power of Compounding", "content": "Compounding is earning returns on both your principal and the accumulated interest over time."},
        {"title": "Types of Investment Accounts", "content": "Learn about different account types like DEMAT, savings, and retirement accounts."},
        {"title": "SIP & Lumpsum Explained", "content": "SIP is a disciplined way to invest regularly, while lumpsum investing involves a one-time investment."}
    ]

    for topic in topics:
        with st.expander(topic["title"]):
            st.write(topic["content"])

# ---------------------------- 🎯 Goal Planning ----------------------------
elif page == "Goal Planning":
    goal_plan = plan_goal()
    st.write(f"Goal Plan: {goal_plan}")

# ---------------------------- 📊 Recommendations ----------------------------
elif page == "Recommendations":
    recommendations = recommend_products()
    st.table(recommendations)

# ---------------------------- 📈 SIP Calculator ----------------------------
elif page == "SIP Calculator":
    show_sip_calculator()
