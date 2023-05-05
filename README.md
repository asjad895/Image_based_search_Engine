# Image_based_search_Engine
 Built An Search Engine Using siamese network

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

###DEMO:



https://user-images.githubusercontent.com/109430048/235300404-fd10a82a-a1b1-4b13-8951-38180eed90a5.mp4

