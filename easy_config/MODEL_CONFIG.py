"""
Config file for specific models.
"""
model_config = {
  
    "DATA_LABEL_FILENAME": None,
    "LABEL_COL_NAME": None,
    "LEARNING_RATE": None,
    "BATCH_SIZE": None,
    "EPOCHS": None,
    "SAVED_MODEL_FILENAME": None,
    # "": None,
    # "": None,
    # "": None,
}

# label params
# data_label_filename = "species_labels.csv"
data_label_filename = "test_labels.csv"
label_col_name = "Species"

# model hyperparams
learning_rate = 0.001
batch_size = 50
epochs = 5

# desired model filename
# saved_model_filename = "species_predictor.rtf"
saved_model_filename = "test_mod.rtf"






# Make all updates
model_config["SAVED_MODEL_FILENAME"] = saved_model_filename
model_config["LEARNING_RATE"] = learning_rate
model_config["BATCH_SIZE"] = batch_size
model_config["EPOCHS"] = epochs
model_config["DATA_LABEL_FILENAME"] = data_label_filename
model_config["LABEL_COL_NAME"] = label_col_name
