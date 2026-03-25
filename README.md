# Inverse-Problems: Stochastic Optimal Stopping &amp; Volatility Surface Calibration

## Brownian Motion
Brownian motion ($W_t$) is a random process satisfying:
  1. W<sub>0</sub> = 0
  2. W<sub>t</sub> - W<sub>s</sub> ~ N(0, t-s) for s < t
     * note N(0, t-s) describes a normal random variable where mean = 0, var = t-s
  3. increments are independent
  4. W<sub>t</sub> is continuous

Increment ΔW = W<sub>t+Δt</sub> - W<sub>t</sub> 
          ΔW ~ N(0, Δt) and the size of ΔW can be approximated to be the standard deviation, so ΔW ~ $\sqrt{Δt}$
          
