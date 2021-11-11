import tensorflow as tf
import numpy as np
from tensorflow import keras

#display the image
import matplotlib.pyplot as plt

#load a pre defined dataset(70k of 28X28) it load the data from that website
fashion_mnist = keras.datasets.fashion_mnist

#pull out data from dataset
(train_image, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# it show image which load
print(train_labels[0])
plt.imshow(train_image[0], camp = 'gray', vmin = 0, vmax= 255)
plt.show()