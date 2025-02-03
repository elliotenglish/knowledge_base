# Reinforcement Learning

## Bellman Equation

https://en.wikipedia.org/wiki/Bellman_equation

### Value function

We define the maximum possible discounted value achievable starting from some initial state as:

$$V(x_0)=\max_{\{a_t\}_{t=0}^\infty}\sum_{t=0}^\infty\beta^t F(x_t,a_t) \tag{1}$$

s.t.

$$a_t\in\Gamma(x_t)\tag{2}$$
$$x_{t+1}=T(x_t,a_t)\tag{3}$$

Where

- $x_t$ is the state at time $t$
- $a_t\in\Gamma(x_t)$ is the action taken at time $t$
- $\Gamma(x)$ is the possible actions at state $x$.
- $F(x,a)$ is the feedback/reward/payoff function for taking action $a$ in state $x$.
- $T(x,a)$ is the transition function giving the next state after taking action $a$ in state $x$.
- $\beta$ is the discount factor, used to reduce the value of feedback in the future.

### Recursive value function

We can rewrite the value function in recursive form:

$$V(x_0)=\max_{a_0}(F(x_0,a_0)+\beta V(x_1))\tag{4}$$

Or more compactly:

$$V(x)=\max_{a\in\Gamma(x)}(F(x,a)+\beta V(T(x,a)))\tag{5}$$

### Stochastic value function

If we assume that the state transitions (T) and feedback (F) are stochastic we define the value function instead using the expectation as follows:

$$V(x)=\max_{a\in\Gamma(x)}(\mathbb{E}(F(x,a)+\beta(V(T(x,a)))))\tag{6}$$

## Q-Learning

In this case we use a modified Bellman equation to take in both a state, an action, the current policy parameters and return the expected return.

$$\hat{Q}(x,a,\pi)=\mathbb{E}(F(x,a)+\beta\hat{Q}(T(x,\pi(x))))\tag{7}$$

Where

- $\pi$ is the policy.

In the case of reinforcement learning, we directly learn an approximation to the Q function,

$$Q(x,a,\theta)\tag{8}=\hat{Q}(x,a,\pi(\theta))$$

Where

- $\theta$ are the parameters that encode both the composite policy and value function.

In this case we take a step and then our objective is the Bellman Error as follows:

$$|Q(x_t,a_t,\theta)-F_t+\beta Q(T_t,\pi(T_t),\theta)|\tag{9}$$

Where

- $F_t=F(x_t,a_t)$ is the feedback we have observed.
- $T_t=T(x_t,a_t)$ is the transition we have observed.

Additionally while there are further steps to implement an exploit/explore execution algorithm, the above equation gives supervised learning approach for fitting $\tilde{Q}(\theta,\cdot)$.

References:
- https://en.wikipedia.org/wiki/Q-learning
- https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
- https://arxiv.org/abs/2410.21795

## Soft Actor-Critic (SAC)

## Group-Relative Policy Optimization (GRPO)

## Exploitation vs Exploration

### $\epsilon$-greedy Learning

In this strategy we simply take a random action at a fixed rate, which is defined as $\epsilon\in[0,1]$. So effectively we have:

$$a_t(x_t)=\left\{\begin{matrix}a \sim \mathbb{U}(\Gamma(x_t)), & P(\cdot)=\epsilon \\ \displaystyle\max_{a\in\Gamma(x_t)}V(x,a), & P(\cdot)=1-\epsilon\ \end{matrix}\right.$$

## Online vs Offline Operation

We use equation 9 as the objective when learning the parameters for Q. Generically we can structure our dataset as follows:

$$\{x_t^i,a_t^i,F_t^i,T_t^i\},i\in[1,N]\$$

With this definition we can utilize a normal training loop using pre-generated data, or by running simulation within the training loop at additional cost, but increased robustness.

```
class PrerecordedDataGenerator:
  det __init__(self,...):
    #Load from files
    self.data = [(...),
                 (...)]

  def Get(self,model):
    return random.choose(dataset)

class OnlineDataGenerator:
  def __init__(self,...):
    ...

  def Get(self,model):
    #

def train(data_generator):
  while True:
    sample=data_generator.Get(model)
    objective=model.Q(sample.x_t,sample.a_t)-(sample.F_t+model.beta*model.Q(sample.T_t,model.policy(sample.T_t)))

    parameter_derivatives=differentiate(objective,model.parameters())

    updater.update(model.parameters(),parameter_derivatives)
```
