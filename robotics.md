# Robotics

## Terminology

- Maximal coordinates: Parameterizing a system using physical space coordinates. e.g. for each body in a robot the rigid transformation of each of the components described as a position vector $\vec{x}$ and a quaternion rotation vector $\textbf{R}$.
- Generalized coordinates: Parameterizing a system with a set of degrees of freedom that more intuitively describe the system, often taking into account the constraints on the maximal coordinates. A function is then defined to compute the maximal coordinates from the generalized coordinates $\{\vec{x}_i,\textbf{R}_i\}=f(\textbf{q})$ e.g. $q$ could be joint angles so that the hierarchy and joint limits of the bodies is implicitly respected.
- Operational space: Using coordinates to describe the task to be performed. e.g. XYZ of an end effector and target location.
- Joint space: Using generalized coordinates to describe the task to be performed.
- Proprioception: The ability of your body to determine it's current state in terms of internal senses: e.g. joint positions, muscle applied force, balance, and acceleration. These are high speed senses and used for very short term motion component planning such as balancing.

## Software

- https://github.com/google-deepmind/acme
- https://github.com/google-deepmind/dm_control/
- https://github.com/google-deepmind/mujoco

## Research groups

- Sergey Levine research group: https://github.com/rail-berkeley
- FAIR PEARL: https://github.com/facebookresearch/Pearl

## Automatically configuring models

For the purposes of learning a robust controller, even a for specific end use case, it's important to train the controller on a wide variety of model variants in order to account for sources of error such as noise in the environment and manufacturing tolerances. One of the challenges here is to automatically construct these variants. Various aspects need to be sized in reasonable ways, so that goals can be achieved, but without over provisioning (and creating instability, or overly large quantization).

A simple heuristic to compute approximate force range for the joint/DoF $q_i$ is as below:

Compute a maximum effective mass for joint:

$$\hat{m}_i=\max_q m_i(q)$$

This can be done by sampling various $q$ configurations.

Then given a target maximum acceleration $a_t$ we can compute the maximum force as:

$$\hat{f}_i=a_t\hat{m}_i$$
