import streamlit as st
import yfinance as yf
import gbm_simulation

st.set_page_config(page_title = "Geometric Brownian Motion", page_icon = "📈", layout = "wide")
st.title("Geometric Brownian Motion Simulator")

with st.sidebar:
    st.header("Parameters")
    S0 = st.slider("Starting Price", 50, 250, 100)
    mu = st.slider("Drift", 0.0,1.0,0.1)
    sigma = st.slider("Volatility", 0.0,1,0,0.2)
    T = st.slider("Total Time (years)",1,25,10)
    M = st.slider("Paths",1000,10000,5000)

    update = st.button("Update", type="primary", use_container_width=True)

if update:
    st.spinner("Simulating...")
    S_t = gbm_simulation.simulate_gbm(S0 = S0, mu = mu, sigma = sigma, T = T, N = 252, M = M)
    fig = gbm_simulation.plot_paths(S_t, T, S0, mu, sigma)
    st.pyplot(fig)