## Brownian Motion – Family of Random Variables Defined on a Common Probability Space

### Brownian motion ($W_t$) is a random process satisfying:

  1. $W_0$ = 0
  2. $W_t$ - $W_s$ ~ N(0, $t-s$) for s < t
     * note N(0, $t-s$) describes a normal random variable where mean = 0, var = $t-s$
  3. increments are independent
  4. $W_t$ is continuous

### Increments of Brownian Motion  
 $\Delta W = W_{t+\Delta t} - W_t$  
 $\Delta W \sim N(0, \Delta t)$  

 - The size of $\Delta W$ is on the order of its standard deviation  
 - Therefore, $\Delta W \sim \sqrt{\Delta t}$
        
from this we get $(\Delta W)^2$ ~ $\Delta t$, now we break $\Delta t$ into infinite small parts  
  - let $\Delta t = t/n $
  
then $\sum_{i=1}^n (\Delta W_i)^2$ ~ $n * t/n = t \to [W]_t = t$ 
