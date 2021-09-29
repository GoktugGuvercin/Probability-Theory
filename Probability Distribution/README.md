# Random Variables and Probability Distribution

## Random Variables

* Random variables are used to denote possible incidents that can happen under specific problem domain. A random variable is responsible for storing next random
  event that will happen. However, which one of the events in problem domain will take place is completely uncertain. Probability theory tries to examine the
  probability of their occurence. 
  
* Random variables are classified under two different categories, which are *discrete* and *continuous random variable*. If there exists finite number of events in
  problem domain like rolling a dice, discrete random variable is used. However, when we try to measure and take a record of amount of rainfalls in specific region
  we face infinite number of cases. Hence, such problems are represented by continuous random variable. 
  
<p align="center">
  <img src="https://github.com/GoktugGuvercin/Probability-Theory/blob/main/Probability%20Distribution/rolling%20a%20dice.png" width="700" height="316" />
</p>

## Probability Distribution

* If we determine all possible events in problem domain, and compute the probability of occurrence of all those events, we become capable of creating probability
  distribution of this domain. In other words, probability distribution is nothing but a map that illustrates what events can take place and what chance of their
  occurrence is. This is quite easy process for discrete random variables due to the limited number of cases in the domain, but not possible for continuous random
  variables. However, by collecting so many number of observations from problem domain and then examining their frequency of distribution on value range, we can
  approximate its probability distribution. 

* Probability distribution can be denoted with a curve or a function. Distribution functions can be of two different types, which are probability mass and
  probability density function for discrete and continuous random variables respectively. In the figure below, probability distribution of total amount of rainfalls
  in terms of mm for specific region is illustrated. It behaves like typical gaussian distribution. 
  
<p align="center">
  <img src="https://github.com/GoktugGuvercin/Probability-Theory/blob/main/Probability%20Distribution/rainfalls.png" width="700" height="486" />
</p>
  
## Random Number Generator 
  
* Random number generators generally benefit from well-known probability distributions like gaussian, chi-square, or uniform. In that way, probability distributions
  are actually not only the output of random events in problem domains, but they can be also used as input for a particular purpose. What is confusing in this point
  is how they can be deployed for the generation of random numbers. In fact, each probability distribution has special parameters characterizing its density
  function. Depending on the arguments passed to those parameters, a problem domain (value range) is defined for that distribution, and random numbers are sampled
  from that value range. Hence, we are unable to determine the boundaries between which random numbers will be dispersed except for uniform distribution, since its
  parameters are that boundaries themselves. There exists infinite number of primitive sections on that value range, and each of them, denoted with dx, corresponds
  to particular probability value. These probability values actually decides the frequency of sampled numbers. The ones with higher probability have higher chance
  to be sampled. In the figure below, some well-known distributions are illustrated. **Their plot can be also obtained by source code distributions.py**
  
<p align="center">
  <img src="https://github.com/GoktugGuvercin/Probability-Theory/blob/main/Probability%20Distribution/distributions.png" width="1000" height="370" />
</p>
  

### Parameters of Well-Known Distributions

Name | Parameters
--------- | -------------
Gaussian | Mean and Variance
Uniform | Low and Hight
Chi-Square | Degree of Freedom

