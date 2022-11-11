#helper functions for building and training a ml
from torchvision.transforms import Compose, Resize, CenterCrop, Grayscale, ToTensor
from classes.data import CustomImageDataset
from torch.utils.data import DataLoader
import torch
# from torch.autograd import Variable

def dataloader(dataset, batch_size):
    """
    Load data
    dataset = training, test, or validation subsets

    Returns batched data as an iterable
    """
    batched_data = DataLoader(dataset=dataset, batch_size=batch_size, shuffle=True)
    return batched_data

def downloadData():
    """
    Download daat from databases.
    Return: Images and labels?
    """

def trainModel(learning_rate, batch_size, epochs):
    """
    Used to train a model
    """


    return


def saveModel(model):
    """
    Save a trained model. Stores model weights.
    TODO: See if it's better to save the model with it's shape instead of just the state_dict. Note: Before loading
    the saved model (with state_dict), you need to create an instance of the same model first, 
    and then load the parameters using load_state_dict() method.
    """
    path = "./myFirstModel.pth"
    torch.save(model.state_dict(), path)

def testBatch():
    """
    Function to test the model with a batch of images and show the label predictions
    """
    # get batch of images from the test DataLoader  
    # images, labels = next(iter(test_loader))

    # # show all images as one image grid
    # imageshow(torchvision.utils.make_grid(images))
   
    # # Show the real labels on the screen 
    # print('Real labels: ', ' '.join('%5s' % classes[labels[j]] 
    #                            for j in range(batch_size)))
  
    # # Let's see what if the model identifiers the  labels of those example
    # outputs = model(images)
    
    # # We got the probability for every 10 labels. The highest (max) probability should be correct label
    # _, predicted = torch.max(outputs, 1)
    
    # # Let's show the predicted labels on the screen to compare with the real ones
    # print('Predicted: ', ' '.join('%5s' % classes[predicted[j]] 
    #                           for j in range(batch_size)))

def constructImageTransform(number_output_channels, desired_size):
    """
    Function to transform images to grayscale, resize, and center crop.
    """
    train_transform = Compose([Grayscale(num_output_channels=number_output_channels),Resize(desired_size), CenterCrop(desired_size), ToTensor()]) 

    return train_transform 

def transformDataset(transforms):
    """
    Function to transform and build a dataset.
    TODO: Build this function on the CustomImageDataset class. kwargs = whatever we need 
    to download images and labels
    """
    transformed_dataset= CustomImageDataset(transform=transforms)
    return transformed_dataset