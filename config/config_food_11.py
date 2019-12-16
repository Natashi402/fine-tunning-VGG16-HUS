# import the necessary packages
import os

# initialize the path to the *original* input directory of images
ORIG_INPUT_DATASET = "Food-11"

# initialize the base path to the *new* directory that will contain
# our images after computing the training and testing split
BASE_PATH = "dataset"

# define the names of the training, testing, and validation
# directories
TRAIN = "training"
TEST = "evaluation"
VAL = "validation"

# initialize the list of class label names
CLASSES = ["Bread", "Dairy product", "Dessert", "Egg", "Fried food",
	"Meat", "Noodles/Pasta", "Rice", "Seafood", "Soup",
	"Vegetable/Fruit"]

# set the batch size when fine-tuning
BATCH_SIZE = 40

# initialize the label encoder file path and the output directory to
# where the extracted features (in CSV file format) will be stored
LE_PATH = os.path.sep.join(["output", "le.cpickle"])
BASE_CSV_PATH = "Result"

# set the path to the serialized model after training
MODEL_PATH = os.path.sep.join([BASE_CSV_PATH, "result_model.h5"])
MODEL_PATH_HEAD = os.path.sep.join([BASE_CSV_PATH, "result_model_head.h5"])

# define the path to the output training history plots
UNFROZEN_PLOT_PATH = os.path.sep.join([BASE_CSV_PATH, "unfrozen.png"])
WARMUP_PLOT_PATH = os.path.sep.join([BASE_CSV_PATH, "warmup.png"])

# target_size
TARGET_SIZE = (224,224)

#EPOCH
EPOCH_HEAD = 80
EPOCH_ALL = 25