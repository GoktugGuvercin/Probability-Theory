
# Maximum Likelihood Estimation

* Although it is not possible to get completely familiar with problem domain of continuous random variable due to infinite number of incidents, we can draw some
conclusions about the state of that domain by examining the observations collected from it. These observations not only help to estimate the kind of probability 
distribution that they belong to, but also enable us to approximate the parameters of that distribution. While histogram or Kolmogorov-Smirnov test is quite 
sufficient to accomplish first one, approximation of distribution parameters, like mean and variance in gaussian case, is more chalenging part. In this point,
the algorithm called "Maximum Likelihood Estimation" is used. 

* Maximum Likelihood Estimation (MLE) approaches this problem as an optimization procedure in machine learning just like updating the model parameters with the help
of an optimization algorithm under the guidance of particular loss function. However, it is assumed by MLE which sort of probability distribution the observations refer to is already known, since what actually MLE does is to optimize the parameters of probability density function. If you don't know the type of distribution, then you cannot know its density function either. As a result, it becomes impossible to optimize parameters of that density function. Hence, this process is also called as *density estimation*. 

* Let's see how it works with concrete case; we took a record of precipitation in specific region on a monthly basis, and as a result, we constructed a dataset of 10 years, containing totally 120 observations. Besides, we know that distribution of annual precipitation clearly fits gaussian curve. The first thing that will do is to select random but senseful initialization values for mean and variance (parameters) of gaussian distribution, just like the models in machine learning, and then set them to those values, denoted with θ. If we say that p(x) is the probability of facing observation x, p(x|θ) is considered as the probability of facing the sample x drawn from gaussian distribution parametrized with θ. Since all collected observations are indipendent and identically distributed samples, the probability that entire dataset was drawn from gaussian distribution parametrized with θ is equal to the product of their individual conditional probabilities. 

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Probability-Theory/blob/main/Maximum%20Likelihood%20Estimation/product%20of%20sample%20probabilities.png" width="400" height="223" />
</p>

* In fact, there exist numerous values which distribution parameters θ can take; however, this set of observations were sampled from problem domain with particular gaussian distribution, and what we are looking for is the parameters of that distribution. Hence, we aim to find the one with highest sampling probability. In accordance with this purpose, a process of searching parameter space is conducted, and the one which maximizes the result of the probability formula illustrated above tries to be discovered. However, ene of the problems encountered in this point is that the product of many conditional probabilities can result in numerical underflow; thus, by taking the logarithm of both side of the equation, we can put it into more convenient and durable form. In addition to this, since maximization applications are not completely supported in terms of ML optimization procedure, we multiply new logarithmic equality by -1 in order to convert it into a loss function that can be minimized over a convex curve. This laid the foundations of *Negative Log-Likelihood Loss* function commonly used with classification models. After this point, applying gradient descent is enough to obtain correct distribution parameters.

<p align="center">
  <img src="https://github.com/GoktugGuvercin/Probability-Theory/blob/main/Maximum%20Likelihood%20Estimation/MLE%20equation.png" width="402" height="211" />
</p>
