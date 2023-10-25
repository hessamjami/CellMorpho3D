# General_Membrane.py

# Membrane_num_of_Nodes = 1678  # This is the number of nodes on the membrane (Both the outer membrane and the Nucleus). This is the first number that appears in the 'membrane' file (once opened with a text editor)
# Membrane_num_of_Triangles_temp = 3488  # This is the number of triangles on the membrane (Both the outer membrane and the Nucleus). This is the number that appears in the 'membrane' file after the node position list is finished and before Gmesh lists the nodes that make a triangle.
Membrane_Radius = 10.0  # Is the outer membrane radius. The radius of the membrane should be the same as the one used to generate the Gmesh membrane file; otherwise, the program crashes.
# Nucleus_Membrane_radius = 4.0  # Is the nucleus membrane radius. The radius of the nucleus should be the same as the one used to generate the Gmesh membrane file; otherwise, the program crashes.
kvolume = 0.0

# Membrane_spring_coefficient = 2.0  # 1.0  # stretching constant
# Membrane_bending_coefficient = 0.0  # 30.0  # 15.0  # bending constant
membrane_damping_coefficient = 0.0  # Viscosity of the Membrane. It is applied in Force calculation for the Membrane Node pairs. I have commented out these parts in the 'Membrane_Force_Calculator' because I think the current code does not need it (some energy-consuming array calculations were involved).
Membrane_Node_Mass = 1.0
K_surfaceConstant_local = 100
Membrane_spring_coefficient = 2.0  # 1.0  # stretching constant
Membrane_bending_coefficient = 2.0  # 30.0  # 15.0  # bending constant
Membrane_spring_force_cut_off = 10000.0
membrane_damping_coefficient = 0.0  # Viscosity of the Membrane. It is applied in Force calculation for the Membrane Node pairs. I have commented out these parts in the 'Membrane_Force_Calculator' because I think the current code does not need it (some energy-consuming array calculations were involved).
Membrane_barrier_calculation_rate = 5
Node_radius = 1.0  # Width of interaction range of nodes: used to be 1.0
