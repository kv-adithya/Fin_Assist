import pandas as pd

def recommend_products():
    # Example data
    data = {
        "Product Name": ["SBI Bluechip Fund", "HDFC Midcap Opportunities", "ICICI Prudential Debt Fund"],
        "Type": ["Equity (Large Cap)", "Equity (Mid Cap)", "Debt"],
        "Risk Level": ["Moderate", "High", "Low"],
        "1-Year Return (%)": [12.5, 15.8, 6.2]
    }
    return pd.DataFrame(data)
