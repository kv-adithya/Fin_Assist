import streamlit as st

def plan_goal():
    st.header("Goal Planning")
    goal = st.text_input("What is your investment goal? (e.g., Buy a house, Education)")
    years = st.number_input("Target years to achieve the goal", min_value=1, max_value=30, value=5)
    monthly_savings = st.number_input("How much can you save per month? (in INR)", min_value=1000, value=5000)

    total_savings = monthly_savings * 12 * years
    return {
        "Goal": goal,
        "Time Horizon (years)": years,
        "Estimated Savings (INR)": total_savings
    }
