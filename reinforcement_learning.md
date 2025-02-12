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

$$|Q(x_t,a_t,\theta)-(F_t+\beta Q(T_t,\pi(T_t),\theta))|\tag{9}$$

Where

- $F_t=F(x_t,a_t)$ is the feedback we have observed.
- $T_t=T(x_t,a_t)$ is the transition we have observed.

Additionally, while there are further steps to implement an exploit/explore execution algorithm, the above equation gives supervised learning approach for fitting $\tilde{Q}(\theta,\cdot)$.

References:
- https://en.wikipedia.org/wiki/Q-learning
- https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf
- https://arxiv.org/abs/2410.21795

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

## Implicit vs explicit models (sampling optimal policies)

Implicit:

From a theoretical perspective, and as listed above, Q functions typically both the state and action as arguments, and then return the value. However, this can be expensive if you want to find the optimal policy as you need to solve an optimization problem:

$$Q(x,a)\in\real$$

$$\pi_\text{opt}(x)=\text{argmax}_a Q(x,a)$$

This can require a non-trivial optimizer such as gradient descent that may require many function/gradient evaluations and get stuck in local minima.

Explicit:

Alternatively for discrete action spaces, you can simply return a vector containing the value for each possible action:

$$Q(x)=\begin{pmatrix}Q(x,a_1) \\ \vdots \\ Q(x,a_n)\end{pmatrix}$$

## Continuous/discontinuous/composite action spaces (actor-critic)

One of the challenges with Q/Value learning is how to represent the action space. For simple systems, the action may simply be a choice from $N$ options at each step. However, for most real world systems there are a number of issues:

- Actions are typically a composite of a number of sub-actions (e.g. $a=(a0,a1)$). This can be resolved by representing the action as indexing into the Cartesian product of the sub-actions.
- Actions can have real-valued sub-actions. This can be resolved by either using an implicit value representation or by quantizing the action space.

When the above 2 issues are combined we can have very large action spaces. For example if we 4 sub-actions each with 5 options, then the action space will be $5^4=625$. This can negatively impact the learning process as it takes a very long time to explore the action space, even when most of the actions are highly correlated (as in the real-valued case).

Alternatively you can use an implicit Q model (the critic), and to overcome the issue of finding the optimal action, use an explicit policy (the actor).

So we end up with the following optimization problem:

$$\min_{Q,\pi} \sum_{(x_i,a_i,F_i,x'_i)} (Q(x_i,a_i)-(F_i+\beta Q(x'_i,\pi(x'_i)))) - Q(x_i,\pi(x_i))$$

Where the first term is the Bellman Error and the second term optimizes the policy. Once we have a solution to this minimization, we can simply use the policy $\pi(x)$ to one-shot generate optimal actions.

## Soft Actor-Critic (SAC)

https://arxiv.org/abs/1801.01290

## Group-Relative Policy Optimization (GRPO)

## Deep Deterministic Policy Gradient (DDPG)

https://arxiv.org/abs/1509.02971
