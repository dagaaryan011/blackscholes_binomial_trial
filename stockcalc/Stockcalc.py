# main_app.py
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from Blackcholes import calculate_option_price as black_scholes_price
from binomial import calculate_binomial_option_price as binomial_price

st.set_page_config(page_title="Option Pricing Calculator", layout="centered")

st.title(" Option Pricing Calculator")

# Tabs for each pricing model
tab1, tab2 = st.tabs(["Black-Scholes", "Binomial Tree"])




with tab1:
    
    S = st.number_input(" Deal Price for Stock", min_value=1.0, value=100.0, key="bs_S")
    C = st.number_input("Current  Price of Stock", min_value=1.0, value=100.0, key="bs_K")
    T = st.slider("Time to Expiry (years)", 0.01, 3.0, 1.0, step=0.01, key="bs_T")
    r_percent = st.slider("Risk-Free Rate (%)", 0.0, 15.0, 5.0, step=0.1, key="bs_r")
    r = r_percent / 100
    v = st.slider("Volatility (σ)", 0.01, 1.0, 0.2, step=0.01, key="bs_sigma")
    option_type = st.selectbox("Option Type", ["call", "put"], key="bs_type")

    if st.button("Calculate with Black-Scholes"):
        price = black_scholes_price(S, C, T, r, v, option_type)
        if (option_type=='call'):
           st.success(f"Do not pay more than ₹{price:.2f} for this call option")
        elif (option_type=='put'):
           st.success(f"The fair value of this put option is ₹{price:.2f}. Avoid selling it for less.")
with tab2:
    st.subheader("Binomial Tree Method")
    S2 = st.number_input("Deal Price for Stock", min_value=1.0, value=100.0, key="bt_S")
    K2 = st.number_input("Current  Price of Stock", min_value=1.0, value=100.0, key="bt_K")
    T2 = st.slider("Time to Expiry (years)", 0.01, 3.0, 1.0, step=0.01, key="bt_T")
    r_percent2 = st.slider("Risk-Free Rate (%)", 0.0, 15.0, 5.0, step=0.1, key="bt_r")
    r2 = r_percent2 / 100
    sigma2 = st.slider("Volatility (σ)", 0.01, 1.0, 0.2, step=0.01, key="bt_sigma")
    steps = st.slider("Time Intervals", 1, 500, 100, step=1, key="bt_steps")
    option_type2 = st.selectbox("Option Type", ["call", "put"], key="bt_type")

    if st.button("Calculate with Binomial Tree"):
        price2 = binomial_price(S2, K2, T2, r2, sigma2, steps, option_type2)
        if (option_type=='call'):
           st.success(f"Do not pay more than ₹{price2:.2f} for this call option")
        elif (option_type=='put'):
           st.success(f"The fair value of this put option is ₹{price2:.2f}. Avoid selling it for less.")

            





