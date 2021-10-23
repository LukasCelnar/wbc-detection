import tensorflow as tf
import numpy as np
IMG_HEIGHT = 224
IMG_WIDTH = 224
print(tf.__version__)
class_names = ['EOSINOPHIL', 'LYMPHOCYTE', 'MONOCYTE', 'NEUTROPHIL']
model = tf.keras.models.load_model('test_model.h5')

def prediction_from_path(model, path):
  img = tf.keras.utils.load_img(
      path, target_size=(IMG_HEIGHT, IMG_WIDTH)
  )

  img_array = tf.keras.utils.img_to_array(img)
  img_array = tf.expand_dims(img_array, 0) # Create a batch

  predictions = model.predict(img_array)
  max_index = np.argmax(predictions[0])
  print(class_names[max_index], predictions[0][max_index] * 100)

prediction_from_path(model, 'manual_test\LYMPHOCYTE\_2_6981.jpeg')