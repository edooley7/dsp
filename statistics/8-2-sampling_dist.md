[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

Exercise 8.2  
Suppose you draw a sample with size n=10 from an exponential distribution with λ=2. Simulate this experiment 1000 times and plot the sampling distribution of the estimate L. Compute the standard error of the estimate and the 90% confidence interval.
Repeat the experiment with a few different values of n and make a plot of standard error versus n.

```
import math
import numpy as np
import thinkstats2

def RMSE(estimates, actual):
    e2 = [(estimate - actual) ** 2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def SimulateSample(lam=2, n=10, m=1000):
    """Sampling distribution of L as an estimator of exponential parameter.
    lam: parameter of an exponential distribution
    n: sample size
    m: number of iterations
    """
    estimates = []
    # For each simulation m,
    for j in range(m):
        # Creates a random set of values along a standard exponential distribution with shape lam and size n
        xs = np.random.exponential(1.0 / lam, n)
        # Calculates the mean of the xs and returns
        L = 1.0 / np.mean(xs)
        # For each simulation, adds the estimates of lam to estimates[]
        # Now estimates has 1000 estimations of lam
        estimates.append(L)

    # Computes the root mean squared error of a sequence of estimates.
    stderr = RMSE(estimates, lam)
    print'standard error = ', stderr

    cdf = thinkstats2.Cdf(estimates)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print 'confidence interval = ', ci

    #plot the CDF
    thinkplot.Cdf(cdf)
    thinkplot.Show(xlabel='estimate', ylabel='CDF')

SimulateSample(n=10)
SimulateSample(n=100)
SimulateSample(n=1000)
```

Output:
[Sampling distribution](http://i.imgur.com/5EWFb6S.png)
```
standard error =  0.767715467686
confidence interval =  (1.248324829910848, 3.6692273553960324)
standard error =  0.204736336711
confidence interval =  (1.7287862810313355, 2.3820651404115574)
standard error =  0.0604594080569
confidence interval =  (1.9068922563569453, 2.1002749345071843)

n     stderr
10    0.77
100   0.20
1000  0.06
```

