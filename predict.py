from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg19 import preprocess_input

loaded_model = tf.keras.models.load_model('model.h5')

image = load_img('image_file', target_size=(200, 200))
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)
yhat = model.predict(image)

class_labels = ['sunflower', 'rose', 'tulip', 'dandelion', 'daisy']
pred = np.argmax(yhat, axis=-1)
print(class_labels[pred[0]])
