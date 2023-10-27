# General_constants.py

MD_num_of_steps = 1000000  # number of MD steps
savingstep = 1000  # The step on which the trajectory of the membrane is saved.
MD_Time_Step = 0.001  # time length of steps in MD
KT = 1.0  # KT the quanta of energy
pi = 3.141592  # clear!
RunThermostatePerstep = 100
Node_radius = 1.0  # Interaction range of the nodes: use to be 1.0!
mcstep = 1

mcstep = 1
fluidity = 0.002  # Used in the MC step

Lbox = 1000.0  # (size of square periodic box-1)
Periodic_condtion_status = 0.0  # status 0.0 = off (The Periodic update will not be executed in the 'Main MD' loop). status = 1.0 = on
