# Artificial General Intelligence (AGI)

## Goal of AGI

The ultimate goal of development efforts within artifical intelligence/machine learning is to create an system/agent/entity capable of the following:
- Solving complex tasks at minimum at a human level.
- Adapting to new complex tasks that it has not seen before.

As for what is a complex task that can be solved at a human level, we can define this as the set of tasks that can be solved by some large percentile of the population given a moderate amount of education.

Also note that most models have moved beyond just being (large) language models, where they process multimodal data (text, images, audio), both as part of the input and the output. Although one can argue that these are all forms of language.

## Measuring Intelligence

- The classical test is the [Turing Test](https://en.wikipedia.org/wiki/Turing_test) in which you have a human subject lingually interacting with a hidden agent. The goal is for the agent to respond such that the human can not determine that the agent is a non-human.
- Standardized testing sets/benchmarks (e.g. MMLU, ImageNet) are also available to test models. These test a broad set of tasks from comprehension to mathematical proofs. There are leaderboards showing the performance of models on these benchmarks, such as the [Hugging Face LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard). 
- Objective functions (e.g. perplexity for LLMs) are typically one of the metrics used to gauge the fit of a model to both training and testing data as long as annotations or self-annotations (as in the case of LLMs) are available. This is an important way to measure accuracy as it helps align the training process and real world applications.

## Progression of Model Architectures

- Multilayer perceptrons (MLP)
- Convolutional neural networks (CNN)
- Recurrent neural networks (RNN)
- Transformer architectures

Currently the majority of the SOTA models use a transformer architecture. However, it also appears that the majority of the accuracy improvements are due to having bigger models and proportionately more data. However, generally as models grow they become harder to train due to the instability of stochastic gradient based methods (e.g. SGD, Momentum, Adam). So while one architecture might be a better architecture for a given problem by having better basis functions/nonlinearities, they may instead be easier to train. Transformers and other attention mechanisms can help short circuit models, making them less "nonlinear" for any given example. For example a transformer allows a nonlinear multiplicative relationship in a single layer, while an MLP needs many layers to approximate these even for moderately simple datasets.

## Scaling Laws

- OpenAI [analysis](https://arxiv.org/abs/2001.08361)
- Google [analysis](https://research.google/pubs/explaining-neural-scaling-laws/)

## Supervised vs Unsupervised Learning

## Confidence in Output

## Arbitrary Function Approximation

## Feature Engineering

## Memorization vs Reasoning

## Pattern Matching vs Reasoning

## References

## The Age of Spiritual Machines and the Singularity

Ray Kurzweil wrote a book entitled [The Age of Spiritual Machines](https://en.wikipedia.org/wiki/The_Age_of_Spiritual_Machines) in which he discussed many concepts related to AGI, and the progression of humans, predicting that we would create AGI and then merge with that AGI in an attempt at immortality.

## Scaling Laws

https://arxiv.org/pdf/2203.15556
- N - model parameters across all parts of model
- D - training tokens, equal to the average sequence length x total sequences
  - How is this optimized for as we can take longer sequences but this will reduce the number of tokens due to the quadratic compute as a function of sequence length
- C - flops total during training, equal to the number of steps taken by the FLOPs per step
- L - final pretraining loss
- N_opt(C),D_opt(C) = argmin(L(N,D),FLOPs(N,D)=C) - For a given count of flops, this gives the optimal model size and training tokens

https://arxiv.org/abs/2402.14746
- $s=w_1 w_2..w_l$ - The sequence and words of sequence
- $S$ - set of sequences length $l$ or less as a subset of the full set $T$
- $p_s=P(w_1 w_2..w_{l-1})P(w_l|w_1 w_2..w_{l-1})$ - The probability of the sequence s in the data
- $q_s=P(w_1 w_2..w_{l-1})Q(w_l|w_1 w_2..w_{l-1})$ - The probability of the sequence s in the model
- $f(s)=Q(w_l|w_1 w_2..w_l-1)$
- $L_k(f,T)=\sum_{p_s\neq q_s}p_s$ or more precisely $L_k(f,T)=\displaystyle\sum_{s\in T,dist(p_s,q_s(f))>k}p_s$ - This is a discrete
- $L_k(f,T)=min_{h\in F}[L_k(h,T)]+\epsilon$ - Just saying we end up with a close to optimal f. The "dimension" is the complexity of the space of functions that bound $\epsilon$. TODO: Figure out what this means.
- $D$ is the size of the training corpus
- $F$ is a family of functions. It seems that this is a set of architectures with an equal number of parameters, or similar definition.
- $d$ is the dimension of $F$ (see shattering definition).

## Set shattering
Given $C$, a set (or class) of sets, and $A$ a set, then $C$ shatters $A$ if

- $\forall c\subset C$ (all subsets of $C$)
  - $\exists h\in H$ s.t.
    - $h\bigcap C=c$

https://en.wikipedia.org/wiki/Shattered_set

## Generalized set shattering
A set $X$ is shattered by the set of functions $F$ if the following conditions are satisfied:
- $\exists f,g\in F$ s.t.
  - $\forall x\in X,f(x)\neq g(x)$
  - $\forall Y\subset X$
    - $\exists h\in F$ s.t.
      - $\forall x\in Y$,$h(x)=f(x)$
      - $\forall x\in(X-Y),h(x)=g(x)$

The implication is that $F$ contains 2 functions, $f$, $g$, that have completely disjoint ranges on the domain $X$, and that for any division of $X$, there exists another function that matches the $f$ when evaluated on $X$ and matches $g$ on the complement of $X$.

The **dimension** of a set of functions $F$ is the size of the largest set shattered by it.

$d(F)=argmax_{d}(max_{T\in T(d) s.t. shatters(F,T)}(|T|))$

## Cosine Learning Rate Decay

$LR = initial_LR × ( 1 + cos(π × epoch/epochs) ) / 2$

## Vapnik-Chervonenkis Theory

https://en.wikipedia.org/wiki/Vapnik%E2%80%93Chervonenkis_theory

## Information Entropy

- https://en.wikipedia.org/wiki/Entropy_(information_theory)#Characterization

Information entropy captures how the likelihood of an event corresponds to the information it encodes. In particular, given the option of a variable length encoding, it tells us what the optimal average number of bits is required to encode each element in a distribution.

TODO: Figure out derivation/proof of optimal encoding size.

## Cross entropy

$$H(p,q)=\sum_{x\in \Omega} -p(x) log(q(x))=E_p(log(q))$$

Where $p(\cdot)$ is the known probability distribution of points $x$ in the set $\Omega$, $q(\cdot)$ is the predicted probability distribution, and $E_p(\cdot)$ is the expected value operator.

When used as part of the objective of a learning algorithm the known probability distribution is typically a 1-hot vector ($p(x)=\delta(t,x)$), so the formula reduces to the following:

$$H(p,q)=-log(q(t))$$

## Perplexity

$$\overline{H}=\overline{H}(\{P_i^j\},\{t^j\})=\frac{1}{N_j}\sum_j H(\{P_i^j\},t^j)$$

Where $j$ indexes tokens in a sequence. Then we define perlexity as follows:

$$ppl=e^{\overline{H}}$$

## bits-per-byte

$bpb(L)=L\times log_2(e)$

https://skeptric.com/perplexity/

$$\text{characters\_per\_token} = len(text) / len(tokens[0])$$

## Superposition

When a neuron can represent multiple features.

## Current progress 2025/2/2

- DeepSeek
- New Google Gemini variants
- New OpenAI ChatGPT variants Strawberry (Q*)

## Current progress 2024/11/15

There are a broad set of AI systems available that provide state of the art results. Some examples below:

Closed source models available through web APIs:
- OpenAI ChatGPT
- Google Gemini
- Anthropic Claude
- Wolfram Alpha

Open Source models available for download:
- Meta LLaMa

Note that open source is also under debate as most models are at least trained on proprietary data. And regardless of the data being available, the compute and hardware required is not feasible for most people.

Some points/references:
- For the vast majority of people we may already be [beyond the Turing Test](https://dl.acm.org/doi/10.1145/3673427).
- LLM benchmarks show that these models have very limited ability to do general symbolic reasoning, and what currently works is likely due to large amounts of training data with templates that have been "memorized" by these models. See Apple's recent [investigation](https://arxiv.org/pdf/2410.05229) for detailed examples.
- [AGI survery](https://github.com/ulab-uiuc/AGI-survey) [open review notes](https://openreview.net/forum?id=H2ZKqfNd0U)
- An [analysis](https://arxiv.org/abs/2406.03689) of the ability of LLMs to build complex world models.
- (https://www.freethink.com/robots-ai/arc-prize-agi)

There is also a big gap in between performance of closed source and open source models. This is probably due to manually engineered features being added to closed source models. By these I mean adding functions embedded within the model that call into numeric processing systems, [computer algebra systems (CAS)](https://en.wikipedia.org/wiki/Computer_algebra_system), and [retrieval augmented generation (RAG)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation). Probably the most transparent case of this is Wolfram Alpha, which can solve a very broad range of problems and greatly predates ChatGPT. Note that these are essentially forms of feature engineering.
