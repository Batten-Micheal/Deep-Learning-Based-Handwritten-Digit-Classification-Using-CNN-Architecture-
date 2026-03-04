import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Load trained model
model = tf.keras.models.load_model("model.h5")

# Load MNIST test sample
(_, _), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Pick one image
image = x_test[0]

plt.imshow(image, cmap='gray')
plt.title("Actual Label: " + str(y_test[0]))
plt.show()

# Preprocess
image = image / 255.0
image = image.reshape(1, 28, 28, 1)

# Predict
prediction = model.predict(image)
print("Predicted Digit:", np.argmax(prediction))