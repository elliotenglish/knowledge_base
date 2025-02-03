# Robotics

## Terminology

- Maximal coordinates: Parameterizing a system using physical space coordinates. e.g. for each body in a robot the rigid transformation of each of the components described as a position vector $\vec{x}$ and a quaternion rotation vector $\textbf{R}$.
- Generalized coordinates: Parameterizing a system with a set of degrees of freedom that more intuitively describe the system, often taking into account the constraints on the maximal coordinates. A function is then defined to compute the maximal coordinates from the generalized coordinates $\{\vec{x}_i,\textbf{R}_i\}=f(\textbf{q})$ e.g. $q$ could be joint angles so that the hierarchy and joint limits of the bodies is implicitly respected.
- Operational space: Using coordinates to describe the task to be performed. e.g. XYZ of an end effector and target location.
- Joint space: Using generalized coordinates to describe the task to be performed.

## Software

- https://github.com/google-deepmind/acme
- https://github.com/google-deepmind/dm_control/
- https://github.com/google-deepmind/mujoco
