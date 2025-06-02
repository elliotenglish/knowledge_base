# Fusion Engineering

## Topics

- Plasma physics
  - Alfven waves: https://en.wikipedia.org/wiki/Alfv%C3%A9n_wave
  - Coordinate systems
    - Magnetic coordinates
      - Coordinates in basis of magnetic field
    - Boozer coordinates
      - http://fusionwiki.ciemat.es/wiki/Boozer_coordinates
- Reactor types
  - Tokamak
  - Compact Tokamak
  - Advanced Tokamak
  - Spherical Tokamak
  - Stellarator
  - Polywell
    - https://www.reddit.com/r/fusion/comments/16cmcsr/polywell_fusion_with_planar_accelerators/
  - Mirror Machine
  - Direct Drive Inertial Confinement
  - Indirect Drive Inertial Confinement
  - Reversed Field Pinch
  - Z-Pinch
- Stellarators
  - Design classifications
    - Quasi-isodynamic
      - Omnigeneity
      - Particular paths do not move radially on average
      - No bootstrap current
      - No neoclassical transport in collisionless regime
    - Quasi-symmetric
    - Quasi-helical
  - Coil-winding surface (CWS)
    - Surface around twisted plasma on which magnets are placed
    - Typically offset from plasma last surface by fixed distance along surface normal
  - Ripple
    - Imperfections due to the discrete placement of magnets
- Plasma facing component (PFC)
  - Heating
    - Neutral beam injection (NBI)
      - Ion heating mechanism
      - Source of fast ions
    - Electron cyclotron resonance heating (ECRH)
    - Ion cyclotron resonance heating (ICRH)
    - Lower hybrid resonance heating (LH)
- Fuel cycles
  - D+T=
  - D+D=
  - D+He3=
  - P+B11
- Liquid lithium pressure vessel lining
  - Prevent heat loss due to inward hydrogen flux
  - Breed tritium given Li6
  - Molten lithium flows along walls using electric current through fluid
  - 99% of neutrons captured
- High temperature superconductor
  - Chemical: Niobium Oxide Nb…
  - Manufacturing
    - Superconducting tape wrapped into coils
    - Superconducting cylinders laser etched into strips
  - Cooling systems
  - Mathematical models
    - Brandt, Ernst Helmut, and Mikhail Indenbom. "Type-II-superconductor strip with current in a perpendicular magnetic field." Physical review B 48.17 (1993): 12893.
    - Brandt, Ernst Helmut. "The flux-line lattice in superconductors." Reports on Progress in Physics 58.11 (1995): 1465.
    - Brandt, Ernst Helmut. "Superconductors of finite thickness in a perpendicular magnetic field: Strips and slabs." Physical review B 54.6 (1996): 4246.
    - Grilli, Francesco, et al. "Computation of losses in HTS under the action of varying magnetic fields and currents." IEEE Transactions on Applied Superconductivity 24.1 (2013): 78-110.
  - Theory
    - https://www.youtube.com/watch?v=iln3bsJE7o4
    - https://en.wikipedia.org/wiki/Density_of_states
    - https://en.wikipedia.org/wiki/Phonon
    - https://en.wikipedia.org/wiki/Fermi_level
    - https://en.wikipedia.org/wiki/Fermi_energy
    - https://en.wikipedia.org/wiki/Fermi_surface
    - https://en.wikipedia.org/wiki/BCS_theory
    - https://en.wikipedia.org/wiki/Condensed_matter_physics
    - https://en.wikipedia.org/wiki/Propagator
- Diverters
How is fuel added?
How is exhaust removed?
Energy generation
Heat exchanger embedded in lithium lining
Water
- Structure
  - https://www.hpalloy.com/Alloys/descriptions/HASTELLOYC_276.aspx
  - Radioactivation
    - nickel + neutrons = radioactive cobalt isotope
    - Neutron activation analysis (NAA)
      - Analysis of the reaction of materials being bombarded with neutrons
- Magnet Structures
  - Curved coils
  - Etch drums
  - Planar elements
- Software
  - https://github.com/fusion-energy
  - https://github.com/PrincetonUniversity/STELLOPT
  - https://github.com/openmc-dev
- Courses
  - https://suli.pppl.gov/2023/course/

## Plasma Representations

- Continuum Quantum mechanical
  - Only feasible for localized (to calculate reaction rates)
- Classical particles/molecular dynamics
  - Only feasible for localized (to calculate reaction rates)
- Continuum Kinetic
  - Superparticles or cells with densities of species / momentums
- Continuum gyrokinetic
- Continuum gyrofluid
- Continuum MHD (magneto-hydrodynamics)
  - Many variants

## Reactor Components

In order to build a digital twin we need to model each of the following components. It must be represented with a consistent geometric representation with appropriate interfaces or coupling equations if interacting.
- Electromagnetic fields
- Plasma (ions, electrons)
- Inner wall (Plasma facing component)
- Neutron flux (ignore in aneutronic case)
- Magnets
- Mechanical support/load structure
- Heating systems
- Fuel injection
- Exhaust removal/diverter
- Diagnostics
- Heat exchanger

## Reaction Rate

Reaction rate increases with temperature to a degree due to particle overcoming coulomb forces holding apart the nuclei. However, after a certain temperature reaction rates decreases as nuclei simply pass one another by even at near proximity. Without this you would have runaway reactions. Generally these are experimentally determined.

- $<\sigma v>$ - Reactivity.
- $v$ - The mean velocity in a Maxwell–Boltzmann distribution.
- $\sigma$ - The collision cross-section.

## Lawson Criterion

Used to understand the concept of "ignition", or otherwise the moment at which a reaction becomes self-sustaining.

$$nT\tau_E$$

- $n$ - The mass density.
- $T$ - The temperature.
- $\tau_E$ - The energy half life assuming no energy is generated or added to the system. There are many forms of energy loss, but you can mostly think of them behaving like thermal conduction.

Note that $\tau_E\sim\frac{1}{n}$ and consequently $n\tau_E\sim T$, meaning that largely the criteria is density independent.

## Energy Gain

$$Q=\frac{P_\text{out}}{P_\text{in}}$$

- $P_\text{out}$ - The energy produced by the fusion reaction, or produced by energy capture systems.
- $P_\text{in}$ - The energy used for heating and other systems.

There are many forms of $Q$:

- $Q_\text{fuel}$ - $P_\text{in}$ is the energy absorbed by the fuels, $P_\text{out}$ the energy released by the reaction.
- $Q_\text{sci}$ - $P_\text{in}$ is the energy added by heating systems, $P_\text{out}$ is the energy released by the reaction.
- $Q_\text{eng}$ - $P_\text{in}$ is the energy added by reactor systems, $P_\text{out}$ is the energy sent to the grid.

These are a progression of including more system factors into the total energy calculation.

## Plasma configuration solution

Force balance equation:

$\textbf{J}\times\textbf{B}-\nabla p=0$
