def chromatin_constructor(Chromatin_Bead_Position, Chromatin_Bead_Velocity, Chromatin_Bead_Force, chromatin_contant_matrix_calculation_flag, CmLaststeps):
    file_name = "xvchromatin.txt"
    
    with open(file_name, "r") as read:
        for j in range(Chromatin_num_of_Beads):
            line = read.readline().split()
            Chromatin_Bead_Position[j][0] = float(line[0])
            Chromatin_Bead_Position[j][1] = float(line[1])
            Chromatin_Bead_Position[j][2] = float(line[2])

            Chromatin_Bead_Position[j][0] *= Chromatin_Scaling_Factor
            Chromatin_Bead_Position[j][1] *= Chromatin_Scaling_Factor
            Chromatin_Bead_Position[j][2] *= Chromatin_Scaling_Factor

        for j in range(Chromatin_num_of_Beads):
            line = read.readline().split()
            Chromatin_Bead_Velocity[j][0] = float(line[0])
            Chromatin_Bead_Velocity[j][1] = float(line[1])
            Chromatin_Bead_Velocity[j][2] = float(line[2])

    if chromatin_contant_matrix_calculation_flag:
        for i in range(Chromatin_num_of_Beads):
            for j in range(Chromatin_num_of_Beads):
                CmLaststeps[i][j] = 0.0

# Define Chromatin_num_of_Beads and Chromatin_Scaling_Factor here
Chromatin_num_of_Beads =  # Your value
Chromatin_Scaling_Factor =  # Your value

# Initialize your arrays
Chromatin_Bead_Position = [[0.0] * 3 for _ in range(Chromatin_num_of_Beads)]
Chromatin_Bead_Velocity = [[0.0] * 3 for _ in range(Chromatin_num_of_Beads)]
Chromatin_Bead_Force = [[0.0] * 3 for _ in range(Chromatin_num_of_Beads)]
CmLaststeps = [[0.0] * Chromatin_num_of_Beads for _ in range(Chromatin_num_of_Beads)]

chromatin_contant_matrix_calculation_flag = True

chromatin_constructor(Chromatin_Bead_Position, Chromatin_Bead_Velocity, Chromatin_Bead_Force, chromatin_contant_matrix_calculation_flag, CmLaststeps)
