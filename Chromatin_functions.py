//
// Chromatin_functions.cpp
// Cell - Durotaxis
//


# include "Chromatin_functions.hpp"

using
namespace
std;

void
Chromatin_constructor(double
Chromatin_Bead_Position[Chromatin_num_of_Beads][3], double
Chromatin_Bead_Velocity[Chromatin_num_of_Beads][3], double
Chromatin_Bead_Force[Chromatin_num_of_Beads][3], bool
chromatin_contant_matrix_calculation_flag, float
CmLaststeps[Chromatin_num_of_Beads][Chromatin_num_of_Beads])
{
    ifstream
read;
read.open("xvchromatin.txt");

for (int j=0;j < Chromatin_num_of_Beads; j++) // all
beads
interaction
whit
the
next
one
{
    read >> Chromatin_Bead_Position[j][0];
read >> Chromatin_Bead_Position[j][1];
read >> Chromatin_Bead_Position[j][2];

Chromatin_Bead_Position[j][0] *= Chromatin_Scaling_Factor;
Chromatin_Bead_Position[j][1] *= Chromatin_Scaling_Factor;
Chromatin_Bead_Position[j][2] *= Chromatin_Scaling_Factor;

}

for (int j=0;j < Chromatin_num_of_Beads; j++) // all beads interaction whit the next one
{
read >> Chromatin_Bead_Velocity[j][0];
read >> Chromatin_Bead_Velocity[j][1];
read >> Chromatin_Bead_Velocity[j][2];
}

if (chromatin_contant_matrix_calculation_flag == true) {
for (int i=0;i < Chromatin_num_of_Beads;i++)
{
for (int j=0;j < Chromatin_num_of_Beads;j++)
{
CmLaststeps[i][j]=0.0;
}

}
}

}
