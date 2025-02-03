# Machine Learning

## Overview

### Linear Algebra

Linear algebra, in particular matrix-matrix and matrix-vector products, is a prerequisite for understanding Machine Learning. The Matrix Cookbook is an excellent resource for identities and various calculations.

https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf

### Calculus

In general, only differentiation is needed to compute partial derivatives used in gradient descent updates.

https://en.wikipedia.org/wiki/Derivative

### Machine Learning

Machine learning is a numerical technique where data is sampled from a system of interested and then a parameterized computational model is fit to that data. This computational model system is then used to make predictions give new data. The most basic task is to take a data point and classify it as one of a number of classes. Historically, machine learning used models relied upon very shallow but well understood architectures to model data. For example, linear regression and logistic regression which rely upon form $\sigma(Ax+b)$, where the model parameters are the matrix $A$ and vector $b$ in the matrix-vector multiplication form, to correlate different input values with an output value. Other examples include support vector machines (SVM) and polynomial regression. In order to handle more complex systems, generally either feature engineering was required, or higher order terms were added.

### Deep Learning

Deep learning, instead of relying upon more complex building blocks to model data with more intricate patterns, relies upon composing simple models. Typically this takes the form of a series of linear and nonlinear layers. For example.

$y=\mathbf{b}_2+\mathbf{A}_2\sigma(\mathbf{b}_1+\mathbf{A}_1\mathbf{x})$ in the case of 2 layers.

or 

$y=\mathbf{b}_3+\mathbf{A}_3\sigma(\mathbf{b}_2+\mathbf{A}_2\sigma(\mathbf{b}_1+\mathbf{A}_1\mathbf{x}))$ in the case of 3 layers.

Note that without the nonlinear stages, additional linear stages have no impact and are equivalent to a single stage, except in the case of a low rank architecture.

Deep models are typically represented as a graphical model. In addition, operations can have multiple inputs.

$$z_1=\sigma(A_1 x+b_1)$$

$$z_2=\sigma(A_2\begin{pmatrix}x^T \\ z_1^T\end{pmatrix}^T)$$

As a graphical model: (TODO)

### Supervised Learning vs Unsupervised Learning

Supervised learning is the fiting of a model to explicit input/output (a.k.a. annotations, labels) pairs. This is typically stated as ${\mathbf{x}_i,y_i}$ where $y_i=f(\mathbf{x}_i)$.

Unsupervised learning is the process of finding patterns in data without having explicit labels i.e. ${\mathbf{x}_i}$. Typically only clustering is considered unsupervised learning, often only relying upon a metric comparing points such as a P-norm (e.g. L1, L2).

Semi-supervised learning generally doesn't have annotated input/output pairs. Instead the output value is generated using some heuristics, such as predicting a value based upon its spatial context.

### Discriminative vs Generative Models

### Classification vs Regression

**Multi-class classification** is the task of assigning 1 of N classes to a data point. In this case the output values are typically normalized and sum to one, often performed using a softmax function, $f(\mathbf{x})_i=\frac{e^{x_i}}{\sum_j e^{x_j}}$.

**Binary classification** the task of assigning any number of N classes to a data point. In this case each value is compressed to the range [0,1], often perfomed using a sigmoid function, $f(\mathbf{x})_i=\frac{1}{1-e^{-x_i}}$.

In both of these cases, the values can be interpreted as probabilities. However, from a computational perspective they don't necessarily have any significance as a probability and are more a result of the engineered properties of the computational architecture and training process. This is further reinforced by the fact that probability is ill-defined in most real world cases, relying upon a prior assumption of the underlying distribution and parameter estimates. There is other literature that further discusses the definition of probability. That said, it is a useful interpretation.

**Regression** is the task of outputting real numbers that predict a value in a finite or infinite range.

## Applications

### Tabular Data

Tabular data means data that comes in the form of a table where each row represents a different data point. Each data point is a vector that concatenates a number of values representing specific fields/columns. In this case models are generally used to predict a specific field from the other fields. This is a form of supervised learning.

Given pairs ${\mathbf{x}_i,y_i}$ where they are sampled from a function $f(\cdot)$:

$f(\mathbf{x}_i)=y_i$

We want to fit an additional function $\hat{f}(\mathbf{x})$.

### Signal/Audio Processing

In signal processing we aim to make predictions given a sequence of data. The input data can be either a finite window of historical data, or all previous data. But no future data.

$y^t=f(\{\mathbf{x}^{T<=t}\})=f({\mathbf{x}^0,\mathbf{x}^1,...,\mathbf{x}^{t-1},\mathbf{x}^t})$

Often these are solved by using a *sliding window* of values in order to fix the number of inputs:

$f(\{\mathbf{x}^{T-w < t <= T}_i\})$, where $w$ is the window size.

Or by using a state variable in a *recurrent* model:

$h^t=f(h^{t-1},x^t)$

$y^t=g(h^t)$

$h^{-1}$ or $h^0$ is initialized to some initial state.

### Computer Vision

In computer vision we make predictions typically given either a single image, a temporal sequence of images, or some sort of image array. The main difference is that at each time you have a 2D array of data. This includes tasks such as image classification, object detection, object identification, segmentation. object tracking. 3D perception is also often performed on 2D data to extract 3D structure, such as in multiview reconstruction (an extension of stereovision).

- https://github.com/jbhuang0604/awesome-computer-vision

### Natural Language Processing

In natural language processing, strings are processed similarly to signal processing. The most basic being classifying an input sequence.

In the case of a *language model*, the task is to classify the next word after a given sequence. The most prolific example of such a system is autocomplete. It is true that the large language models today, despite their impressive capabilities, are still trained to perform the same task, only with a much higher capacity architecture.

- https://github.com/keon/awesome-nlp

### Multimodel Models

- https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models
- https://github.com/pliang279/awesome-multimodal-ml

## Important Model Architectures

### Multilayer Perceptrons (MLP)

### Convolutional Neural Networks (CNN)

### Recurrent Neural Networks (RNN)

### Transformers

### Mixture of Experts

## Pre/post processing

### Feature Engineering

### Hysteresis

### Sparse Models

Sparsity is not merely a way to accelerate neural networks, it is integral to designing scalable architectures.

References:
- https://dynamic-sparsity.github.io/

## Numerical Methods and Algorithms

### (Stochastic) Gradient Descent

### Gradient Calculation (Backpropagation)

## Software Tools

- https://github.com/josephmisiti/awesome-machine-learning/blob/master/README.md

Essentially all modern tools work by allowing the user to construct a computational graph of operations that contains undefined parameters which are learned via some gradient descent optimization approach. Each framework has their own flavor. For specific applications it is always worth searching for an open source software (OSS) repository where someone else has wired together a more task specific implementation with input/output encoding/decoding and a reasonable model architecture.

### Tensorflow

[Homepage](https://www.tensorflow.org/)

This was the original major framework for graphical ML, built by Google. It is still widely deployed, but new developments are largely done in JAX and PyTorch. Of those, the Keras frontend/syntax for building models is preferred by most users, but limited in terms of what you can build.

### PyTorch

This is a framework built by Facebook/Meta that is nearly identical to Tensorflow but with many of syntax oddities fixed.

[Homepage](https://pytorch.org/)
[Tutorial](https://pytorch.org/tutorials/beginner/basics/intro.html)

### JAX

*Recommended toolkit for future development*

This is the successor to Tensorflow from Google. It is heavily used by machine learning researchers today.

Main benefits:
- Differential numpy interface (see jax.numpy)
- Arbitrarity order derivatives, via expression rewriting into the same language
- Highly optimized for a wide variety of platforms (e.g. CPU, Nvidia, AMD, Google TPU)
- Highly distributed processing (e.g. FSDP)

[Homepage](https://jax.readthedocs.io/en/latest/index.html)
[Tutorial](https://jax.readthedocs.io/en/latest/notebooks/quickstart.html)

## Books/Courses

- https://github.com/josephmisiti/awesome-machine-learning/blob/master/books.md
- https://github.com/josephmisiti/awesome-machine-learning/blob/master/courses.md
