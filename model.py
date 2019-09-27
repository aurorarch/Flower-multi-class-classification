from keras.applications.vgg16 import VGG16
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
from keras.layers import Input, Flatten, Dense
from keras.models import Model
import numpy as np

def vgg16():
  model_vgg16_conv = VGG16(weights='imagenet', include_top=False)
  model_vgg16_conv.summary()
  
  input = Input(shape=(200, 200, 3),name = 'image_input')

  output_vgg16_conv = model_vgg16_conv(input)
  
  x = Flatten(name='flatten')(output_vgg16_conv)
  x = Dense(4096, activation='relu', name='fc1')(x)
  x = Dense(4096, activation='relu', name='fc2')(x)
  x = Dense(5, activation='softmax', name='predictions')(x)
  
  model = Model(input=input, output=x)
  
  opt = SGD(lr=0.001, momentum=0.9)

  model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
  
  return model

def run_test_harness():
    # define model
    model = vgg16()
    # create data generator
    datagen = ImageDataGenerator(rescale=1.0/255.0)
    # prepare iterators
    train_it = datagen.flow_from_directory('flowers/train/',
        class_mode='categorical', batch_size=64, target_size=(200, 200))
    test_it = datagen.flow_from_directory('flowers/test/',
        class_mode='categorical', batch_size=64, target_size=(200, 200))
    # fit model
    history = model.fit_generator(train_it, steps_per_epoch=len(train_it),
        validation_data=test_it, validation_steps=len(test_it), epochs=8, verbose=1)
    # evaluate model
    _, acc = model.evaluate_generator(test_it, steps=len(test_it), verbose=1)
    print('> %.3f' % (acc * 100.0))
    
run_test_harness()    
