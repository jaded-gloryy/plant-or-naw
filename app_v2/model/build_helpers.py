#helper functions for building and training a ml

# from torch.autograd import Variable

def trainModel():
    """
    Used to train a model
    """
    return

def dataloader():
    """
    Load data
    """
    return

def saveModel():
    """
    Save a trained model. Stores model weights.
    """
    # path = "./myFirstModel.pth"
    # torch.save(model.state_dict(), path)
    return

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