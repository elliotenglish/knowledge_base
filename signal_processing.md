# Signal Processing

## Digital to Analog Conversion

This is the process of converting a discrete set of samples to a continuous function.

$$x(t)=f({x_i},t)$$

Where

- $x_i$ are the samples
- $f({\cdot},t)$ computes the value at time $t$ using the discrete samples

### Zero-Order Hold

This is the most basic constant interpolation scheme, where the value at any specific time is equal to the most recent discrete value.

$$\Large x(t)=x_{\lfloor\frac{t}{\Delta t}\rfloor}$$

Where

- $\Delta t$ is the time between samples

This is a simplified formula assuming fixed spacing of samples and an origin time of 0.
