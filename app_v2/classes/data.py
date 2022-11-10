from torch.utils.data import Dataset

class CustomImageDataset(Dataset):

    """
    Define dataset
    TODO: Modify to get images and labels from a database
    """
    def __init__(self, data_dir, data_label_filepath, transform=None, target_transform=None):
        self.img_labels = read_xml(data_label_filepath, xpath="//Data//Image")
        self.data_dir = data_dir
        self.transform = transform
        self.target_transform = target_transform


    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        
        # label = {
        #     "filename": self.img_labels.iloc[idx, 0],
        #     "name": self.img_labels.iloc[idx, 1],
        #     "author": self.img_labels.iloc[idx, 3]
        # }

        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        
        return image, label
