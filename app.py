import streamlit as st
import numpy as np
import gbm_simulation
from gbm_simulation import analy_mean

st.set_page_config(page_title="Geometric Brownian Motion", page_icon="📈", layout="wide")
st.title("Geometric Brownian Motion Simulator")

with st.sidebar:
    st.header("Parameters")
    S0 = st.slider("Starting Price", 50, 250, 100)
    mu = st.slider("Drift", 0.0, 1.0, 0.1)
    sigma = st.slider("Volatility", 0.0, 1.0, 0.2)
    T = st.slider("Total Time (years)", 1, 25, 10)
    M = st.slider("Paths", 1000, 10000, 5000)

    update = st.button("Update", type="primary", use_container_width=True)

if update:
    with st.spinner("Simulating..."):
        S_t = gbm_simulation.simulate_gbm(S0=S0, mu=mu, sigma=sigma, T=T, N=252, M=M)

    time = np.linspace(0, T, S_t.shape[1])
    st.session_state.fig = gbm_simulation.plot_paths(S_t, T, S0, mu, sigma, M)
    st.session_state.S_t = S_t
    st.session_state.analytic_mean = analy_mean(S0, mu, time)

if st.session_state.get('fig') is not None:
    st.subheader("Summary")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Max Simulated Price", f"${st.session_state.S_t[:(int(M/100)), -1].max():,.2f}")
    c2.metric("Min Simulated Price", f"${st.session_state.S_t[:(int(M/100)), -1].min():,.2f}")
    c3.metric("Mean Simulated Price", f"${st.session_state.S_t[:, -1].mean():,.2f}")
    c4.metric("Analytical E[Sₜ]", f"${st.session_state.analytic_mean[-1]:,.2f}")

    st.plotly_chart(st.session_state.fig, use_container_width=True)
else:
    st.info("Set parameters in the sidebar and click Update to run the simulation.")