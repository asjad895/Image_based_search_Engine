import keras.backend as K
import tensorflow as tf
import numpy as np
import pandas as pd
import keras
from keras.models import Model
from keras.models import load_model
from keras.utils import load_img,img_to_array

def euclidean_distance(vectors):
    # unpack the vectors into separate lists
    (featsA, featsB) = vectors

    # compute the sum of squared distances between the vectors
    sumSquared = K.sum(K.square(featsA - featsB), axis=1, keepdims=True)

    # return the euclidean distance between the vectors
    return K.sqrt(K.maximum(sumSquared, K.epsilon()))


def contrastive_loss(y, preds, margin=1):
    # explicitly cast the true class label data type to the predicted
    # class label data type (otherwise we run the risk of having two
    # separate data types, causing TensorFlow to error out)
    y = tf.cast(y, preds.dtype)

    # calculate the contrastive loss between the true labels and
    # the predicted labels
    squaredPreds = K.square(preds)
    squaredMargin = K.square(K.maximum(margin - preds, 0))
    loss = K.mean(y * squaredPreds + (1 - y) * squaredMargin)

    # return the computed contrastive loss to the calling function
    return loss

embedding_model=2
retrieval_set_embeddings = 3
train=4

def euclidean_distance1(a, b):
    return np.linalg.norm(a - b)

def retrived(query):
    print(query)
    img = load_img(query, color_mode='rgb', target_size=(224, 224))
    img = img_to_array(img)
    query_img = img / 255.0
    query_emb = embedding_model.predict(np.expand_dims(query_img, axis=0))[0]

    # Compute the distances between the query embedding and all the retrieval set embeddings
    retrieval_set_embs = retrieval_set_embeddings["embeddings"]
    retrieval_set_filenames = retrieval_set_embeddings["filenames"]
    distances = [euclidean_distance1(query_emb, emb) for emb in retrieval_set_embs]
    sorted_indexes = np.argsort(distances)

    # print the top-k images with their corresponding distances
    k = 10
    d = []
    img = []
    cap = []
    for i in range(k):
        image_index = sorted_indexes[i]
        image_path = retrieval_set_filenames[image_index]
        p = image_path.split('train_images/')[1]
        # filter the rows containing the path
        filtered_df = train[train["path"] == p]

        # get the indices of the filtered rows
        indices = filtered_df.index.tolist()
        cap.append(indices)
        image_distance = distances[image_index]
        d.append(image_distance)
        img.append(image_path)
        print(f"Image {i + 1}: {image_path} - Distance: {image_distance}-caption:{indices}")
    return d, img, cap
