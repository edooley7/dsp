# 4) Think Stats Exercise 8.3

Problem: [Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

Exercise 8.3  
In games like hockey and soccer, the time between goals is roughly exponential. So you could estimate a team’s goal-scoring rate by observing the number of goals they score in a game. This estimation process is a little different from sampling the time between goals, so let’s see how it works.
Write a function that takes a goal-scoring rate, lam, in goals per game, and simulates a game by generating the time between goals until the total time exceeds 1 game, then returns the number of goals scored.

Write another function that simulates many games, stores the estimates of lam, then computes their mean error and RMSE.

Is this way of making an estimate biased? Plot the sampling distribution of the estimates and the 90% confidence interval. What is the standard error? What happens to sampling error for increasing values of lam?

Code:
```
import thinkstats2
import thinkplot
import math
import random
import numpy as np

def SimulateGame(lam):
    # lam = goals per game
    # start game
    goals = 0
    time = 0
    while True:
        # generate time between goals
        time_between_goals = random.expovariate(lam)
        time = time + time_between_goals
        # until total time > 1 game
        if time > 1:
            break
        goals = goals + 1
    # return number of goals scored in game
    return goals

def MeanError(estimates, actual):
    errors = [estimate - actual for estimate in estimates]
    return np.mean(errors)

def RMSE(estimates, actual):
    e2 = [(estimate - actual) ** 2 for estimate in estimates]
    mse = np.mean(e2)
    return math.sqrt(mse)

def SimulateManyGames(lam, trials):
    estimates = []
    # simulate many games
    for i in range(0, trials):
        result = SimulateGame(lam)
        # store estimates of lam
        estimates.append(result)

    pmf = thinkstats2.Pmf(estimates)
    
    # compute mean error and RMSE
    print "RMSE:", RMSE(estimates, lam)
    print "Mean error:", MeanError(estimates, lam)
    ci = pmf.Percentile(5), pmf.Percentile(95)
    print "90% confidence interval: ", ci

    thinkplot.Pmf(pmf)
    thinkplot.Show(xlabel = "goals per game", ylabel = "PMF")

SimulateManyGames(2, 1000)
```

Output:
```
RMSE: 1.37549990912
Mean error: 0.004
90% confidence interval:  (0, 5)
[PMF of goal scoring rate](http://i.imgur.com/zkcoQrF.png)
```

Solution:
Standard error when lam = 2 with 1000 trials is 1.38 and sampling error is 0.004.  When trials are increased to 10000, mean error is below 0, meaning that this sample is unbiased.

