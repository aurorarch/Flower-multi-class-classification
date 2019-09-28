# Multi Class Flower Classification

This project is one of my first projects after diving into Computer Vision.

### Dataset:
The dataset I used can be downloaded from [this link](https://www.kaggle.com/alxmamaev/flowers-recognition).
This dataset contains 4242 images of flowers divided into 5 classes, namely - Daisy, Dandelion, Rose, Sunflower and Tulip.
 
### Model Architecture:

- Model Used : [**VGG16**](https://www.mathworks.com/help/deeplearning/ref/vgg16.html;jsessionid=2ac869a30e2fb3236dbaeee06301)
- Input Data Shape : 200x200x3 <br />

#### Classification:
- Flatten
- Dense: 4096
- Activation Function: ReLU
- Dense: 4096
- Activation Function: ReLU
- Dense: 5
- Activation: Softmax

Optimizer: SGD<br/>
Loss: Categorical Crossentropy

## Accuracy 
Almost 90%, but trying to improve more.
