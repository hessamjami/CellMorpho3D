# General_Actin_Membrane_shared.py
# Created by Ali Farnudi on 11/10/2017.

# Define constants and include necessary modules
import math

# This is the number of actin nodes that are on the surface of the original membrane mesh (prior refinement).
# The membrane (refined mesh) also has these nodes as its elements.
Actin_Membrane_shared_num_of_Nodes = 381  # You can uncomment and set your desired value

k_actin_membrane = 1000
Actin_Membrane_Radius_of_Hard_Sphere_Interaction = 0.5
Nucleus_Membrane_Radius_of_Hard_Sphere_Interaction = 0.50
