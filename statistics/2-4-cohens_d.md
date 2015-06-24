[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

Exercise 2.4   Using the variable `totalwgt_lb`, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?

Problem: Are first babies lighter or heavier than others?

Code:

```
import nsfg
import math

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

totalwgt_lb = live.birthwgt_lb + (live.birthwgt_oz / 16)

first_wgt = firsts.totalwgt_lb
other_wgt = others.totalwgt_lb

first_prglngth = firsts.prglngth
other_prglngth = others.prglngth

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d

def SummaryStats(group1, group2, value):
    difference = group1.mean() - group2.mean()
    
    print "Firsts average %s is: %f" % (value, group1.mean())
    print "Others average %s is: %f" % (value, group2.mean())

    print "Firsts %s standard dev is: %f" % (value, group1.std())
    print "Others %s standard dev is: %f" % (value, group2.std())

    if group1.mean() < group2.mean():
        print "Firsts %s is on average %f less than others" % (value, abs(difference))
    else:
        print "Firsts %s is on average %f more than others" % (value, abs(difference))
    print "Cohen's d is: %f standard deviations" % CohenEffectSize(group1, group2)
    
SummaryStats(first_wgt, other_wgt, "weight")
```

Output:
```
Firsts average weight is: 7.201094
Others average weight is: 7.325856
Firsts weight standard dev is: 1.420573
Others weight standard dev is: 1.394195
Firsts weight is on average 0.124761 less than others
Cohen's d is: -0.088673 standard deviations
```

Solution: On average, first babies are 0.125 pounds lighter than other babies. The effect size, using Cohen's d, is -0.089 standard deviations.  For comparison, the Cohen's d for pregnancy length is 0.029 standard deviations and pregnancy length for first babies is on average 0.078 weeks longer than other babies .  The difference in Cohen's d between weight and pregnancy length means that the difference in weight between first and other babies is more significant than the difference in pregnancy length between the two groups.  
