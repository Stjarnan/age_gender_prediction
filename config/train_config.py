from os import path

# define the type of dataset we are training ( Age or gender)
DATASET_TYPE = "age"

# define the base paths to the dataset and output path
BASE_PATH = path.sep.join(["dataset"])
OUTPUT_BASE = path.sep.join(["output"])
MX_OUTPUT = BASE_PATH

# derive the images path and texts path
IMAGES_PATH = path.sep.join([BASE_PATH, "aligned"])
LABELS_PATH = path.sep.join([BASE_PATH, "texts"])

# define the percentage of validation and testing images  (relative to training)
NUM_VAL_IMAGES = 0.15
NUM_TEST_IMAGES = 0.15

# define the batch size
BATCH_SIZE = 128
NUM_DEVICES = 1

# check to see if we are working with age or gender
if DATASET_TYPE == "gender":
	# define the number of labels for the age dataset
	# define the path to the label encoder
	NUM_CLASSES = 8
	LABEL_ENCODER_PATH = path.sep.join([OUTPUT_BASE,
		"age_le.cpickle"])

	# define the path to the output training, validation, and testing lists
	TRAIN_MX_LIST = path.sep.join([MX_OUTPUT, "lists/age_train.lst"])
	VAL_MX_LIST = path.sep.join([MX_OUTPUT, "lists/age_val.lst"])
	TEST_MX_LIST = path.sep.join([MX_OUTPUT, "lists/age_test.lst"])

	# define the path to the output training, validation, and testing recs
	TRAIN_MX_REC = path.sep.join([MX_OUTPUT, "rec/age_train.rec"])
	VAL_MX_REC = path.sep.join([MX_OUTPUT, "rec/age_val.rec"])
	TEST_MX_REC = path.sep.join([MX_OUTPUT, "rec/age_test.rec"])

	# path to the means
	DATASET_MEAN = path.sep.join([OUTPUT_BASE,
		"age_adience_mean.json"])

elif DATASET_TYPE == "gender":
	# define the number of labels for the gender dataset
	# define the path to the label encoder
	NUM_CLASSES = 2
	LABEL_ENCODER_PATH = path.sep.join([OUTPUT_BASE,
		"gender_le.cpickle"])

	# define the path to the output training, validation, and testing lists
	TRAIN_MX_LIST = path.sep.join([MX_OUTPUT,
		"lists/gender_train.lst"])
	VAL_MX_LIST = path.sep.join([MX_OUTPUT,
		"lists/gender_val.lst"])
	TEST_MX_LIST = path.sep.join([MX_OUTPUT,
		"lists/gender_test.lst"])

	# define the path to the output training, validation, and testing recs
	TRAIN_MX_REC = path.sep.join([MX_OUTPUT, "rec/gender_train.rec"])
	VAL_MX_REC = path.sep.join([MX_OUTPUT, "rec/gender_val.rec"])
	TEST_MX_REC = path.sep.join([MX_OUTPUT, "rec/gender_test.rec"])

	# path to the means
	DATASET_MEAN = path.sep.join([OUTPUT_BASE,
		"gender_adience_mean.json"])