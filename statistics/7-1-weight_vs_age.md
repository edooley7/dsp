[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

Exercise 7.1 Using data from the NSFG, make a scatter plot of birth weight versus mother’s age. Plot percentiles of birth weight versus mother’s age. Compute Pearson’s and Spearman’s correlations. How would you characterize the relationship between these variables?

**Scatter plot of birth weight vs. mother's age:**

Code:
```
import thinkstats2
import thinkplot
import nsfg
import numpy as np
import math
% matplotlib inline

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
df = live.dropna(subset=['agepreg', 'totalwgt_lb'])

weights = df.totalwgt_lb
ages = df.agepreg
thinkplot.Scatter(ages, weights)
thinkplot.Show(xlabel = "Age of mother in years", ylabel = "Birthweight in pounds")
```

Output:
[Scatter Plot](http://i.imgur.com/xOxqBtP.png)

**Plot percentiles of birth weight vs. mother’s age:**

Code:
```
#arange makes an array of bins from first # up to but not including
#the second number, with increments of third number
bins = np.arange(5, 50, 5)

#digitize gives the index of the bin that contains each value
indices = np.digitize(df.agepreg, bins)

#groupby creates groups based on indices
groups = df.groupby(indices)

#computes mean age of each bin
age_group = []
for i, group in groups:
    age_mean = group.agepreg.mean()
    age_group.append(age_mean)
    
#computes Cdf for each bin
cdf_group = []
for i, group in groups:
    cdfs = thinkstats2.Cdf(group.totalwgt_lb)
    cdf_group.append(cdfs)

#Sets up graph to take three plots
thinkplot.PrePlot(3)

#For each percentile:
for percent in [75, 50, 25]:
    #Calculates value at each percentile for each bin
    weight_values = [cdf.Percentile(percent) for cdf in cdf_group[1:-1]]
    label = "%dth" % percent
    thinkplot.Plot(age_group[1:-1], weight_values, label = label)

thinkplot.Config(legend=label, loc = "lower right")
thinkplot.Show(xlabel = "Age of mother in years", ylabel = "Birth weight in pounds")
```

Output:
[Percentiles of birth weight vs mother's age](http://i.imgur.com/LcW1oZd.png)

**Compute Pearson's and Spearman's correlations:**

Code:
```
print "Pearson's correlation is: %f" % thinkstats2.Corr(ages, weights)
print "Spearman's correlation is: %f" % thinkstats2.SpearmanCorr(ages, weights)
```

Output:
Pearson's correlation is: 0.068834
Spearman's correlation is: 0.094610

**How can you characterize the relationship between age of the mother and birth weight of the baby?**

Looking at the scatter plot, there seems to be little relationship between age of the mother and birth weight of the baby. Most babies are in a narrow range of weights regardless of how old the mother is.

Looking at the percentile plot, there again seems to be little relationship apparent.  All three percentiles have a similar slope.  That slope is almost a straight line across - maybe there is a chance that older mothers have heavier babies, but it's very small.  This is evident from the very small values of Pearson's and Spearman's correlations.

