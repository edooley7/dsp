[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

Exercise 5.1   In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters µ = 178 cm and σ = 7.7 cm for men, and µ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

Problem: What percent of the US male population is between 5'10" and 6'1"?

Code:
```
import thinkstats2
import thinkplot
import scipy.stats

%matplotlib inline

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale = sigma)

#5'10" = 70 inches = 177.8cm
#6'1" = 73 inches = 185.42
per_between = (dist.cdf(185.42)-dist.cdf(177.8))*100

print "%f percent of US men are eligible to join Blue Man Group" % per_between
```
Output/Solution:
```
34.274684 percent of US men are eligible to join Blue Man Group
```

