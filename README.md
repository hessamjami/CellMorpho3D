# Mechanical-Signature-of-Red-Blood-Cells
Red blood cells (RBCs) have a special ability to undergo cellular deformation to travel through different human microcirculation arteries, allowing them to perform their function as gas carriers between blood and tissues by passing through capillaries with a diameter smaller than their own.
Many illnesses, including malaria, sickle cell anemia, diabetes, genetic disorders, myocardial infarction, and paroxysmal nocturnal hemoglobinuria, have been linked to pathological changes in RBC deformability (PNH).
Measurement of RBC deformability has been the subject of various investigations over the years due to its pathophysiological significance. 
Here, codes are related to the mathematical modeling of the cytoskeleton and morphology of red blood cells (RBCs) under linear tension.
## Virtual Cell Model

The Virtual Cell Model (VCM) software package is a Molecular Dynamics (MD) simulation software. The core concept of VCM is to get particle coordinates and the potentials between them and solve Newton's equations to calculate the dynamics of the system.

...

For more details, please visit the [Virtual Cell Model GitHub Repository](https://github.com/afarnudi/VirtualCellModel).
VCM is a software package written in C++. It currently runs on MacOS and Linux. To build it you need a c++ compiler (g++, llvm, etc). VCM uses OpenMM as its main engin. If you don't have OpenMM please read the next section. If you already have OpenMM installed, you need to:

STEP 1: Install the Boost library

STEP 2: Clone the VirtualCellModel project from our github page.

STEP 3: Change directory to VirtualCellModel.

STEP 4: Run makefile by typing 'make'. You may need to modify the make file depending on the openmm installation directory on your machine if OpenMM is installed in a differnet directory than /usr/local/openmm/.

STEP 5: Run ./VCM -h for help.

Update VCM
To update VCM:

STEP 1: Delete the binary output file

STEP 2: Enter:
make clean;make -j4
OpenMM
The Vertual Cell Model package takes advantage of OpenMM as its main molecular dynamics engine. Please use the instructions on the OpenMM webpage to install OpenMM.

Note: Please install the C++ API. If you have already installed OpenMM with 'Conda' on your system you still need to install the C++ API from the source code (more information on OpenMM website). You may need to install additional software packages (OpenCL, FFTW,SWIG, etc) depending on your choice of platforms (GPU, CPU).
