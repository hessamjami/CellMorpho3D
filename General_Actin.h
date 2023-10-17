# General_Actin.py

Actin_num_of_Nodes = 579  # 566
Actin_num_of_triangles = 872
Actin_spring_coefficient = 5.0  # 10.0  # 5.0  # 0.3  # force constant of springs
Actin_kelvin_damping_coefficient = 100.0  # viscous constant for actin Maxwell fluids: maxwell model >> IT RESISTS AGAINST CHANGING BOND LENGTHS
CytoskeletonNetworkType = 0  # 0=normal hookian network    1=passive cable network  2=active cable network
Actin_viscosity = 3.0

# In case: CytoskeletonNetworkType=1
Actin_Passive_Cable_Network_Coefficient = 2.0  # more detail in the paper: Contractile network models for adherent cells

# In case: CytoskeletonNetworkType=2
KActinACN_EA = 2.0
ACN_TL0 = 0.50
ACN_LC = 0.1

Actin_damping_Coefficient = 0.1  # viscous constant for actin Maxwell fluids: voijdt model >> IT RESISTS AGAINST MOVING BEADS
Actin_Node_Mass = 1.0  # 0.30
minimumlengthActin = 1.5
maximumlengthActin = 2.5
