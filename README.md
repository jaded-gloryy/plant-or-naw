# plant-or-naw

An image classification machine learning model. It has been trained on images from https://plantnet.org/. The model reads images of plants and predicts whether the image contains a leaf, flower, or the entire plant.

aggregate_xml_data.py builds a single xml file (plant_labels.xml) from the source data.

xmltoplantdb.ipynb is a script that takes plant label data (plant_labels.xml) and adds it to a database (MongoDB). 
