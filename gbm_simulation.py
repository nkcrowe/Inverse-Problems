import numpy as np
import matplotlib.pyplot as plt

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

def plot_paths(S_t, T, S0, mu, sigma):
    time = np.linspace(0, T, S_t.shape[1])
    fig, ax = plt.subplots()
    for path in S_t[:50]:
        ax.plot(time, path, color='steelblue', alpha=0.2)

    analytic_mean = analy_mean(S0, mu, time)
    std = sigma_band(S0, mu, sigma, time)

    add = analytic_mean + std
    sub = analytic_mean - std

    ax.plot(time, analytic_mean, color='red', linewidth=2, label = "analytic mean")
    ax.plot(time, add, color='red', linewidth=1, linestyle='--', label = "±1σ band")
    ax.plot(time, sub, color='red', linewidth=1, linestyle='--')

    ax.set_xlabel("Time (Years)")
    ax.set_ylabel("Price")
    ax.legend()
    return fig