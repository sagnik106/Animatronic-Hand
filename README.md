# Animatronic-Hand
A bot which plays rock-paper-scissors by using computer vision to detect what the player had played.

## Requirements/Libraries:
* Python 3.6.9
* Tensorflow 2.0
* Keras 2.2.4
* Numpy 1.15.4
* Matplotlib 3.0.2
* OpenCV 4.2.0

## File organization:
1. [datagen.py](https://github.com/sagnik106/Animatronic-Hand/blob/master/datagen.py) - Uses data augmentation to get a proper training on the data
1. [eyes.py](https://github.com/sagnik106/Animatronic-Hand/blob/master/eyes.py) - A program to predict the state of the player's hand
1. [player.py](https://github.com/sagnik106/Animatronic-Hand/blob/master/player.py) - A game interface (CLI)
1. [Trainer.ipynb](https://github.com/sagnik106/Animatronic-Hand/blob/master/Trainer.ipynb) - A Jupyter Notebook to train the model of Resnet 152 on the augmented data
