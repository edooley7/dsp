# Learn Statistics

Read Allen Downey's [Think Stats (second edition)](http://greenteapress.com/thinkstats2/) and [Think Bayes](http://greenteapress.com/thinkbayes/) for getting up to speed with core ideas in statistics and how to approach them programmatically. Both books are completely available online, or you can buy physical copies if you would like.

[<img src="img/think_stats.jpg" title="Think Stats" width="250" style="float: left;" />](http://greenteapress.com/thinkstats2/)
[<img src="img/think_bayes.png" title="Think Bayes" style="float: left"; />](http://greenteapress.com/thinkbayes/)

Some people enjoy video content such as Khan Academy's [Probability and Statistics](https://www.khanacademy.org/math/probability) or the much longer and more in-depth Harvard [Statistics 110](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uwwH80KTQ6ht66KWxbzTIo). You might also be interested in the book [Statistics Done Wrong](http://www.statisticsdonewrong.com/) or a very short [overview](http://schoolofdata.org/handbook/courses/the-math-you-need-to-start/) from School of Data.


Complete the following exercises.

Communicate the problem, how you solved it, and the solution, within each of the following [markdown](https://guides.github.com/features/mastering-markdown/) files. (You can include code blocks and images within markdown.)

1. [Think Stats Chapter 2 Exercise 4](statistics/2-4-cohens_d.md) (Cohen's d)
2. [Think Stats Chapter 3 Exercise 1](statistics/3-1-actual_biased.md) (actual vs. biased)
3. [Think Stats Chapter 4 Exercise 2](statistics/4-2-random_dist.md) (a random distribution)
4. [Think Stats Chapter 5 Exercise 1](statistics/5-1-blue_men.md) (blue men)
5. [Think Stats Chapter 6 Exercise 1](statistics/6-1-household_income.md) (household income)
6. [Think Stats Chapter 7 Exercise 1](statistics/7-1-weight_vs_age.md) (weight vs. age)
7. [Think Stats Chapter 8 Exercise 2](statistics/8-2-sampling_dist.md) (sampling distribution)
8. [Think Stats Chapter 8 Exercise 3](statistics/8-3-scoring.md) (scoring)
9. [Think Stats Chapter 9 Exercise 2](statistics/9-2-resampling.md) (resampling)


---

Elvis Presley had a twin brother who died at birth.  What is the probability that Elvis was an identical twin?

From Wikipedia:
"The twin birth rate in the United States rose 76% from 1980 through 2009, from 18.9 to 33.3 per 1,000 births."
"Monozygotic twinning occurs in birthing at a rate of about three in every 1000 deliveries worldwide."

Assuming twin birth rate in the US was the same in 1935 as it was in 1980 (probably not a valid assumption, but may be close enough to use), and given the above information:

P(A|B) = Probability Elvis was an identical twin, given that he was a twin.
P(A) = probability Elivs was an identical twin = 0.3%
P(B) = probability Elvis was any type of twin = 1.89%
P(B|A) = probability Elvis was any type of twin, given that he was an identical twin = 100%


Using Bayes theorem:
p(A|B) = (p(A) p(B|A)) / p(B)

p(A|B) = (.003 * 1) / .0189
p(A|B) = 0.1587 = 15.87%

Code:
```
def Bayes(prob_a, prob_b, prob_bgivena):
    prob_agivenb = (prob_a * prob_bgivena)/prob_b
    print prob_agivenb
Bayes(.003, .0189, 1)
```
---


---

How do frequentist and Bayesian statistics compare?

REPLACE THIS TEXT WITH YOUR RESPONSE

---
