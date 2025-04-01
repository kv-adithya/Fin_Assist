# sip_calculator.py

import streamlit as st
import plotly.graph_objects as go

def show_sip_calculator():
    st.header("📊 SIP Calculator & Compound Interest Visualizer")

    monthly_investment = st.number_input("Monthly Investment (₹)", min_value=100, value=1000, step=100)
    annual_return = st.slider("Expected Annual Return (%)", min_value=1, max_value=30, value=12)
    investment_duration = st.slider("Investment Duration (Years)", min_value=1, max_value=40, value=10)

    # Calculations
    months = investment_duration * 12
    monthly_rate = annual_return / 12 / 100
    total_invested = monthly_investment * months
    future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate) * (1 + monthly_rate)
    wealth_gained = future_value - total_invested

    # Results
    st.subheader("💰 Results")
    st.markdown(f"**Total Invested:** ₹{total_invested:,.0f}")
    st.markdown(f"**Total Wealth Gained:** ₹{wealth_gained:,.0f}")
    st.markdown(f"**Maturity Amount:** ₹{future_value:,.0f}")

    # Growth Chart
    years = list(range(1, investment_duration + 1))
    invested = [monthly_investment * 12 * y for y in years]
    value = [
        monthly_investment * (((1 + monthly_rate) ** (12 * y) - 1) / monthly_rate) * (1 + monthly_rate)
        for y in years
    ]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=invested, mode='lines+markers', name='Invested Amount', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=years, y=value, mode='lines+markers', name='Total Value', line=dict(color='green')))

    fig.update_layout(
        title="SIP Growth Over Time",
        xaxis_title="Years",
        yaxis_title="Amount (₹)",
        hovermode="x unified",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)
