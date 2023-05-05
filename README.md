 # ContentCompanion-An Ai Powered content based Search Engine

Function Name: create_custom_df

Input:

data: Pandas DataFrame object containing image paths and their corresponding captions and labels.
min_crop_size: Minimum size of the cropped image (default value: 224).
num_images: Number of images to select from the input DataFrame (default value: 100).
Output:

df: Pandas DataFrame object containing new image paths, their corresponding captions, and labels, which are the output of the image augmentation process. The updated DataFrame is also saved to the train.csv file.
Algorithm:

Get the unique image paths and their descriptions from the input DataFrame and store them in the image_paths_and_desc variable.
Shuffle the image_paths_and_desc and select the first num_images images, store the selected images in the selected_images variable.
Create the output directory output_dir if it doesn't exist.
Copy the selected images to the output_dir and save their descriptions.
Initialize empty lists p, d, and l.
Initialize a variable i to 0.
Initialize an empty list new_rows.
Loop through each row of the selected_images DataFrame:
Get the image path, description, and label from the current row.
Append the image path, description, and label to the p, d, and l lists, respectively.
Get the filename of the image.
Load the image using the Image module.
Get the width and height of the image.
Generate new images by cropping and rotating the original image.
Save the new images to disk.
Add the new images to the new_rows list.
Increment the i variable.
Create a dictionary da with keys path, caption, and label and values p, d, and l, respectively.
Create a Pandas DataFrame df from the da dictionary.
Append the new rows in the new_rows list to the df.
Save the updated DataFrame to the train.csv file.
Return the updated df.

input:

path (str): path to the image file
img_size (int): size to which the image should be resized, default is 224
output:

img (numpy.ndarray): array representation of the image
algorithm:

load the image from the specified path using the load_img function of keras.preprocessing.image module
convert the loaded image to a numpy array using the img_to_array function of keras.preprocessing.image module
normalize the pixel values in the range of 0 to 1 by dividing the array by 255
return the resulting numpy array

input:

temp_df (pandas.DataFrame): a dataframe containing image path, caption and label
output:

None, it displays the images in a 5x5 grid with caption and label
algorithm:

reset the index of the temp_df to start from 0 using the reset_index method
create a figure of size 20x20 using plt.figure method
initialize a counter n to 0
iterate over the first 15 images of temp_df in multiples of 5 using range(15) to display a 5x5 grid
increment the counter n by 1
create a subplot for each image using plt.subplot method with position (i+1) in a 5x5 grid
adjust the spacing between subplots using plt.subplots_adjust method
load the image using the readImage function and the image path from temp_df
display the image using plt.imshow method
create a string a with the label followed by a new line character "\n" and join it with the caption using the join method and textwrap.wrap function to wrap the caption into multiple lines of length 20
set the title of the subplot using plt.title method with the created string
turn off the axis of the subplot using plt.axis("off")

Input:

csv_path: a string indicating the path to a CSV file containing the image data and labels.
img_size (optional): an integer indicating the desired size of the images after preprocessing. Default is 224.
Output:

X: a numpy array containing the preprocessed image data.
y: a numpy array containing the labels.
Algorithm:

Read in the CSV file containing the image data and labels.
Extract the image paths and labels from the CSV file.
Initialize empty arrays to hold the preprocessed image data and labels.
Loop over the image paths and load in the images.
Preprocess the images by resizing and normalizing them.
Add the preprocessed image and label to the arrays.
Return the preprocessed image data and labels as numpy arrays.

The function make_pairs(images, labels) takes in a set of images and their corresponding labels and returns pairs of images along with their labels. The pairs are generated such that one image in the pair is from the same class as the other image (positive pair) and the other image is from a different class (negative pair). This is useful for training a Siamese network, which learns to compare and classify pairs of images.

In a Siamese network, pairs of images are passed through two identical neural networks and the outputs of the networks are compared to determine if the pair of images belong to the same class or not. This approach is useful when we don't have enough labeled data for each class or when we want to learn similarity between two images rather than classify them directly. By training on pairs of images, the network learns to distinguish between different classes and generalize to unseen images.

Input:

images: a numpy array of preprocessed images
labels: a numpy array of corresponding labels for each image
Output:

a tuple of numpy arrays consisting of pairs of images and their corresponding labels, where one image in the pair is similar to the other, and one image in the pair is dissimilar
Steps:

Initialize an empty list to hold the pairs of images and their corresponding labels.
Get the number of unique labels in the dataset.
Loop over each image in the dataset:
a. Get the current image and its corresponding label.
b. Create a boolean mask that indicates which elements in the labels array are equal to the current label.
c. Get the indices of the images that have the same label as the current image.
d. Randomly select an index from the list of indices.
e. Get the image at the selected index and add it as a positive pair to the list of pairImages.
f. Add the label 1 to the list of pairLabels to indicate that the pair of images is similar.
g. Get the indices of the images that have a different label than the current image.
h. Randomly select an index from the list of indices.
i. Get the image at the selected index and add it as a negative pair to the list of pairImages.
j. Add the label 0 to the list of pairLabels to indicate that the pair of images is dissimilar.
Convert the list of pairs of images and their corresponding labels to numpy arrays.
Return the tuple of numpy arrays.
Explain that pairs of images are needed for training a Siamese network, which learns to compare two images and determine if they are similar or dissimilar. By generating pairs of images with known labels, we can train the Siamese network to learn these relationships and make accurate predictions on new image pairs.


Documentation for Siamese function
This function defines a Siamese neural network architecture that takes as input images of shape (inputShape) and produces embeddings of size embeddingDim.

Input parameters
inputShape: tuple representing the shape of the input images to the network.
embeddingDim: integer representing the size of the output embeddings (default is 300).
Output
Returns a Siamese neural network model with two identical subnetworks, each of which processes one of the two input images and returns its embedding.
Documentation for contrastive_loss function
This function defines a contrastive loss function that is used to train the Siamese neural network. It takes as input the true labels (y), predicted distances between image embeddings (preds), and a margin value margin that determines the minimum distance between embeddings of the same class.

Input parameters
y: tensor representing the true labels of the input images.
preds: tensor representing the predicted distances between embeddings.
margin: float representing the margin value that determines the minimum distance between embeddings of the same class (default is 1).
Output
Returns a tensor representing the contrastive loss.
Documentation for euclidean_distance function
This function computes the Euclidean distance between a pair of input embeddings.

Input parameters
vectors: a list of two tensors representing the input embeddings.
Output
Returns a tensor representing the Euclidean distance between the input embeddings.

Function Name: retrived(query)

Input:

query: string, path to the query image file.
Output:

d: list of float, the distances between the query image and the top-k retrieved images.
img: list of string, the file paths of the top-k retrieved images.
cap: list of list of integer, the indices of the training set captions that describe the top-k retrieved images.
Functionality:

This function retrieves the top-k similar images to a query image using the Euclidean distance between their embeddings.
The function loads the pre-trained embedding model, and the embedding vectors of all the training images.
It then computes the Euclidean distance between the query image embedding and all the embeddings of the training images.
The function sorts the distances in ascending order, and retrieves the file paths of the top-k images.
For each top-k image, the function retrieves the corresponding captions from the training set.

Function: show_retrieved_images(query, retrieved_images, distances, k)

Description: This function displays the query image and top-k retrieved images with their corresponding distances.

Input:

query: The path of the query image.
retrieved_images: A list of paths of the retrieved images.
distances: A list of distances between the query image and the retrieved images.
k: An integer indicating the number of retrieved images to be displayed.
Output: None (Displays the images using matplotlib.pyplot)
###DEMO:



https://user-images.githubusercontent.com/109430048/235300404-fd10a82a-a1b1-4b13-8951-38180eed90a5.mp4

