from torch.utils.data import random_split
import torch.cuda
from build_helpers import constructImageTransform, transformDataset, dataloader
from classes.model import NeuralNetwork
# DEFINE how to transform the images
transforms = constructImageTransform(1,224)

# DEFINE dataset using custom class
# TODO: pass the rest of what CustomImageDataset class requires
transformed_dataset = transformDataset(transforms)
print('This is the length of the full data set:', len(transformed_dataset))

#SPLIT INTO TEST AND TRAIN SUBSETS
train_set_size = int(len(transformed_dataset) * 0.8)
test_set_size = int(len(transformed_dataset) * 0.1)
validation_set_size = int(len(transformed_dataset))-train_set_size-test_set_size

train_set, test_set, validation_set = random_split(transformed_dataset, [train_set_size, test_set_size, validation_set_size])
print('The number of images in the Training data set:', len(train_set))
print('The number of images in the Test data set:', len(test_set))
print('The number of images in the Validation data set:', len(validation_set))


# load dataset in data loader
train_dataloader = dataloader(dataset=train_set, batch_size=100, shuffle=True)
test_dataloader = dataloader(dataset=test_set, batch_size=100, shuffle=True)

# serve images with their labels
#TODO: check how the labels look
features, label_names = next(iter(train_dataloader))

# define device to train on
device = "cuda" if torch.cuda.is_available() else "cpu"

#Instantiate a neuralnet model
model = NeuralNetwork().to(device)

#parameterize the model
for name, param in model.named_parameters():
    print(f"Layer: {name} | Size: {param.size()} | Values : {param[:2]} \n")