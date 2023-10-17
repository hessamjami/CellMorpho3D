# Mechanical-Signature-of-Red-Blood-Cells
Red blood cells (RBCs) have a special ability to undergo cellular deformation to travel through different human microcirculation arteries, allowing them to perform their function as gas carriers between blood and tissues by passing through capillaries with a diameter smaller than their own.
Many illnesses, including malaria, sickle cell anemia, diabetes, genetic disorders, myocardial infarction, and paroxysmal nocturnal hemoglobinuria, have been linked to pathological changes in RBC deformability (PNH).
Measurement of RBC deformability has been the subject of various investigations over the years due to its pathophysiological significance. 
Here, codes are related to the mathematical modeling of the cytoskeleton and morphology of red blood cells (RBCs) under linear tension.
# Landscape Analysis
In the landscape of biomedical research simulations, our proposal interfaces with two primary software tools: VCM and RedTell. VCM is a well-established open-source software package that relies on the OpenMM Molecular Dynamics (MD) engine for high-performance calculations in parallel on GPU and CPU platforms. It facilitates the reproduction of simulations and makes configuration files available in the Supplemental Material.
## Virtual Cell Model
VCM and RedTell. VCM is a well-established open-source software package that relies on the OpenMM Molecular Dynamics (MD) engine for high-performance calculations in parallel on GPU and CPU platforms. It facilitates the reproduction of simulations and makes configuration files available in the Supplemental Material.
The Virtual Cell Model (VCM) software package is a Molecular Dynamics (MD) simulation software. The core concept of VCM is to get particle coordinates and the potentials between them and solve Newton's equations to calculate the dynamics of the system.

For more details, please visit the [Virtual Cell Model GitHub Repository](https://github.com/afarnudi/VirtualCellModel).
VCM is a software package written in C++. It currently runs on MacOS and Linux. To build it you need a c++ compiler (g++, llvm, etc). VCM uses OpenMM as its main engin. If you don't have OpenMM please read the next section. If you already have OpenMM installed, you need to:
# Usage
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
# The RedTell software 
[RedTell](https://github.com/marrlab/RedTell) is implemented in Python and can be accessed through the command line on any operating system.
Here are the steps to use RedTell:
Navigate to the RedTell code directory to execute the tool.
Place the data directory inside the RedTell directory, containing an images subdirectory with images in formats .tif, .png, and .jpg to be processed.
To perform segmentation using RedTell's native Mask R-CNN model:

shell

Copy code

$ python redtell.py --funct segment --data <data_dir> --model <model_name>

The --data variable denotes the path to the data directory, which should contain the images subdirectory.
If a model name is specified, <model_name>.model from the model directory is used for segmentation.
Running the command without specifying a model (without --model <model_name>) uses RedTell's default segmentation model.

This command creates two new directories in the data folder: masks with segmentation masks and segmentation_results with segmentation masks overlaid on the original images and containing unique cell identifiers.

To train a new segmentation model adjusted to a custom dataset:

Create a Training directory with Images and Ground-Truth subdirectories containing raw images and segmentation masks.
Every segmentation mask must have distinct integer values for regions corresponding to different cells and 0 for the background.
RedTell requires at least 25 annotated images for training.
To perform training:

shell
Copy code
$ python redtell.py --funct train_segmentation --data <data_dir> --model <model_name>
This command trains a new segmentation model and saves it as <model_name>.model in the model directory.
To apply the new model to images, use the segmentation command again with the new model as --model <model_name>.
To extract features:

shell
Copy code
$ python redtell.py --funct feature_extraction --data <data_dir> --channel <channel>
The <channel> variable defines what channels the features are extracted from.
It can have multiple values, such as mask, bf, and fluo-4.
The extracted features are saved in a features.csv table in the directory containing the data.
In case of cell classification:

Run the annotation command to create annotated cell images:
shell
Copy code
$ python redtell.py --funct annotate --data <data_dir> --num_cells <num_cells>
The <num_cells> parameter denotes the number of cells to annotate.
The command creates an annotation directory in the data directory with saved single-cell images.
To perform classification:

shell
Copy code
$ python redtell.py --funct classify --data <data_dir>
This command trains a classification model and extends the features.csv table with a label column.
It outputs evaluation.csv, a table of metric values for cross-validation, and feature_importance.csv, a table providing the importance of every feature for the classifier.
The features.csv table can be used for downstream analysis to support the research objective.

For detailed instructions and more information, please refer to the [RedTell GitHub Repository](https://github.com/marrlab/RedTell).


