
# Maximum Likelihood Estimation

* Although it is not possible to get completely familiar with problem domain of continuous random variable due to infinite number of incidents, we can draw some
conclusions about the state of the domain by examining the observations concluded from it. These observations not only help to estimate the kind of probability 
distribution that they belong to, but also enable us to approximate the parameters of that distribution. While histogram or Kolmogorov-Smirnov test is quite 
sufficient to accomplish first one, approximation of distribution parameters like mean and variance in gaussian case is more chalenging part. In this point,
the algorithm called "Maximum Likelihood Estimation" is used. 

* Maximum Likelihood Estimation (MLE) approaches this problem as an optimization procedure in machine learning just like updating the model parameters with the help
of an optimization algorithm under the guidance of particular loss function. However, it is assumed that which sort of probability distribution the observations 
picked from problem domain refer to is already known, since what actually MLE does is to optimize the parameters of probability density function. If you don't know
the type of distribution, then you cannot know its density function either. Hence, this is also called as *density estimation*. 

* For example, we took record of precipitation of specific region on a monthly basis, and as a result, we constructed a dataset of 10 years, containing totally 120 
observations. Besides, we know distribution of annual precipitation clearly fits gaussian curve. The first thing that will do is to select random but senseful 
values for mean and variance (parameters) of gaussian distribution, just like the models in machine learning, and then set them to those values, denoted with θ. 
If we say that p(x) is the probability of facing a sample x, p(x|θ) is considered as the probability of facing the sample x drawn from gaussian distribution 
parametrized with θ. Since all collected observations are indipendent and identically distributed samples; hence, the probability that entire dataset was drawn 
from gaussian distribution parametrized with θ is equal to the product of their individual conditional probabilities. 

<p align="center">
  
</p>
