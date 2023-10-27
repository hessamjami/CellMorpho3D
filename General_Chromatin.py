# General_Chromatin.py

Chromatin_num_of_Beads = 500  # number of beads per chromatin
Chromatin_num_of_chains = 10  # Chromatin_num_of_Beads should be divisible by Chromatin_num_of_chains!
Chromatin_Bead_Mass = 1.0  # mass of each bead
Chromatin_Scaling_Factor = 0.7  # This is the scaling length. It (usually) shrinks the chromatines that are the result of the chromatine confinement code, 'xvchromatin.txt'.
Chromatin_spring_coefficient = 400.0  # stretching constant of chromatin
Chromatin_bending_coefficient = 0.0
sigmachromatin = 1.0  # L-j parameter for FENE
Rmaxchromatin = 1.5  # FENE parameter
Chromatin_Membrane_Radius_of_Hard_Sphere_Interaction = 0.5
ThermostatOnChromatin = 100
chromatin_force_cut_off = 3000
