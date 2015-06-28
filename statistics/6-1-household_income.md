[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

***InterpolateSample generates a pseudo-sample; that is, a sample of household incomes that yields the same number of respondents in each range as the actual data. It assumes that incomes in each range are equally spaced on a log10 scale.***

***Compute the median, mean, skewness and Pearson’s skewness of the resulting sample. What fraction of households reports a taxable income below the mean? How do the results depend on the assumed upper bound?***

Code:
```
import numpy as np
import density
import hinc
import thinkplot
import thinkstats2

def InterpolateSample(df, log_upper):
    df['log_upper'] = np.log10(df.income)
    df['log_lower'] = df.log_upper.shift(1)
    df.log_lower[0] = 3.0
    df.log_upper[41] = log_upper
    arrays = []
    for _, row in df.iterrows():
        vals = np.linspace(row.log_lower, row.log_upper, row.freq)
        arrays.append(vals)
    log_sample = np.concatenate(arrays)
    return log_sample
    
def ComputeStats(log_upper):
    # Reads data from file and returns highest income in range, frequency of incomes in that range,
    # cumulative sum of frequencies of income, and percent of total values
    # under given income
    # Incomes are listed as logs ex: income of 3 = 10^3 = 1000
    df = hinc.ReadData()

    # Creates sample of fake incomes that could be in each bracket, with
    # upper limit of $1 mil
    log_sample = InterpolateSample(df, log_upper)

    # Raises 10 to the x power from the values in log_sample to create a linear scale
    sample = np.power(10, log_sample)

    # Prints CDF of linear sample
    cdf = thinkstats2.Cdf(sample)

    # Prints summary stats for the linear sample
    print"With max income 10^%f:" % log_upper
    print'mean =', sample.mean()
    print'median =', thinkstats2.Median(sample)
    print'skewness =', thinkstats2.Skewness(sample)
    print'pearson skewness =', thinkstats2.PearsonMedianSkewness(sample)
    print'fraction of households with income below the mean = ', cdf[sample.mean()]

# Calls function with upper limit of income as $1 million
ComputeStats(6.0)

# Calls function with upper limit of income as $10 million
ComputeStats(7.0)
```

Output:
```

With max income 10^6.000000:
mean = 74278.7075312
median = 51226.4544789
skewness = 4.94992024443
pearson skewness = 0.736125801914
fraction of households with income below the mean =  0.660005879567

With max income 10^7.000000:
mean = 124267.397222
median = 51226.4544789
skewness = 11.6036902675
pearson skewness = 0.391564509277
fraction of households with income below the mean =  0.856563066521
```

Solution:
When the highest income is assumed to be $1 million, 66% of households have income below the mean.
When the highest income is assumed to be $10 million, 86% of households have income below the mean.

Increasing the highest assumed income drastically shifts the mean higher because it creates higher values at the upper end of the distribution. The skew also increases drastically because of the higher incomes act as outliers.  The Pearson's skew goes down, because while the increased high income values drag the mean up, the median stays the same because there are the same number of high values.  Pearson't isn't really a good indicator of skew in this case.

Making an assumption for the upper bound in this case isn't really effective at evaluating the degree of income skew, but even assuming $250,000 is the upper limit, looking at a PMF of the income shows the majority of respondents have a low income compared to the highest income levels.
