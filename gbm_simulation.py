import numpy as np
import plotly.graph_objects as go

def simulate_gbm(S0, mu, sigma, T, N, M):
    N = int(N * T) #N = trading days * years
    dt = T / N #step size

    Z = np.random.standard_normal((M, N)) #M×N matrix of independent draws from N(0,1)
    log_increments = (mu - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z #Itô lemma, log(S{n+1}/S{n})
    update = np.insert(log_increments, 0, np.zeros(M), axis = 1) #Prepends a column of zeros to the left of the matrix
    cum_log_return = np.cumsum(update, axis = 1)  #Takes the running sum along the time axis (axis=1) for each row
    S_t = S0 * np.exp(cum_log_return) #Converts the entire matrix of cumulative log-returns into actual prices in one operation

    return S_t

def analy_mean(S0, mu, time):
    analytic_mean = np.array([S0 * np.exp(mu * t) for t in time])

    return analytic_mean

def sigma_band(S0, mu, sigma, time):
    var = np.array([S0**2 * np.exp(2 * mu * t) * (np.exp(sigma**2 * t) - 1) for t in time])
    std = np.sqrt(var)

    return std

def plot_paths(S_t, T, S0, mu, sigma, M):
    time = np.linspace(0, T, S_t.shape[1])
    analytic_mean = analy_mean(S0, mu, time)
    std = sigma_band(S0, mu, sigma, time)

    upper = analytic_mean + std
    lower = analytic_mean - std

    fig = go.Figure()

    for path in S_t[:(int(M/100))]:
        fig.add_trace(go.Scatter(
            x=time, y=path,
            mode='lines',
            line=dict(color='steelblue', width=0.5),
            opacity=0.25,
            showlegend=False,
            hoverinfo='skip'
        ))

    fig.add_trace(go.Scatter(
        x=time, y=lower,
        mode='lines',
        line=dict(color='rgba(255,165,0,0)'),
        showlegend=False,
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=time, y=upper,
        mode='lines',
        fill='tonexty',
        fillcolor='rgba(255,165,0,0.15)',
        line=dict(color='rgba(255,165,0,0)'),
        name='±1σ band',
        hoverinfo='skip'
    ))

    fig.add_trace(go.Scatter(
        x=time, y=analytic_mean,
        mode='lines',
        line=dict(color='red', width=2),
        name='E[Sₜ] = S₀e^μt'
    ))

    fig.update_layout(
        title='Geometric Brownian Motion Simulation',
        xaxis_title='Time (years)',
        yaxis_title='Price',
        yaxis_tickprefix='$',
        yaxis_tickformat=',.0f',
        template='plotly_dark',
        height=550,
        legend=dict(x=0.01, y=0.99),
        hovermode='x unified',
        margin=dict(l=60, r=40, t=60, b=60)
    )

    return fig