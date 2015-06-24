[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

Exercise 3.1   Something like the class size paradox appears if you survey children and ask how many children are in their family. Families with many children are more likely to appear in your sample, and families with no children have no chance to be in the sample.
Use the NSFG respondent variable NUMKDHH to construct the actual distribution for the number of children under 18 in the household.
Now compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Plot the actual and biased distributions, and compute their means. As a starting place, you can use chap03ex.ipynb.

Problem: Construct the actual distribution for the number of chidren under 18 in the household

Code:
```
import thinkstats2
pmf = thinkstats2.Pmf(resp.numkdhh)
import thinkplot
thinkplot.Hist(pmf, label = "PMF")
thinkplot.Config(xlabel = "# of kids in household", ylabel = 'probability', axis = [-0.5, 6, 0, 0.5])
```

Output/Solution:
```
Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})
```
[PMF graph](http://i.imgur.com/3rcvwLa.png)

Problem: Compute the biased distribution we would see if we surveyed the children and asked them how many children under 18 (including themselves) are in their household.

Code:
```
biaspmf = BiasPmf(pmf, label='Biased PMF')
thinkplot.Hist(biaspmf)
thinkplot.Config(xlabel = "# of kids in household", ylabel = 'probability', axis = [-0.5, 6, 0, 0.5])
```

Output/Solution:
```
Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})
```

[Biased PMF graph](http://i.imgur.com/lO6gxFa.png)

Problem: Plot the actual and biased distributions, and compute their means.

Code:
```
thinkplot.PrePlot(2, cols=2)
thinkplot.Hist(pmf, label = "PMF", align='right', width=width)
thinkplot.Hist(biaspmf, align='left', width=width)
thinkplot.Config(xlabel='# of kids in household',
                     ylabel='probability',
                     axis=[-0.5, 6, 0, 0.5])
print "PMF mean is: %f" % pmf.Mean()
print "Biased PMF mean is: %f" % biaspmf.Mean()
```
Output/Solution:
```
PMF mean is: 1.024205
Biased PMF mean is: 2.403679
```
[Actual vs. Biased Distribution](http://i.imgur.com/YbBiVEA.png)
