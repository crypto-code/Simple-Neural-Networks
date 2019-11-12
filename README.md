# Simple-Neural-Network

Simple Neural Networks of different types written in Keras.

## 1) Multi-Layer Preceptron
A Multilayer Perceptron (MLP) is the simplest type of feedforward Neural Network. It refers to networks composed of multiple layers of neurons, with neurons in each layer fully connected to the previous layer.

The model used in this example will be as follows:
<p align="center">
<img src="https://github.com/crypto-code/Simple-Neural-Network/blob/master/assets/MLP.jpg" align="middle" />   </p>

The code for the model is present in the MLP folder, the model can be run from network.py
```
python network.py
```

## 2) Convolutional Neural Network
A convolutional neural network consists of an input and an output layer, as well as multiple hidden layers. The hidden layers of a CNN typically consist of a series of convolutional layers that convolve with a multiplication or other dot product. The activation function is commonly a RELU layer, and is subsequently followed by additional convolutions such as pooling layers, fully connected layers and normalization layers, referred to as hidden layers because their inputs and outputs are masked by the activation function and final convolution. The final convolution, in turn, often involves backpropagation in order to more accurately weight the end product.

The model used in this example will be as follows:
<p align="center">
<img src="https://github.com/crypto-code/Simple-Neural-Network/blob/master/assets/CNN.jpg" width="350" align="middle" />   </p>

The code for the model is present in the CNN folder, the model can be trained on the CIFAR-10 Dataset using network_train.py and then tested using network_test.py
```
python network_train.py
python network_test.py --input=[image file]
```

## 2) Long-Short Term Memory Recurrent Neural Network
It is a neural network unlike standard feedforward neural networks, LSTM has feedback connections. It can not only process single data points (such as images), but also entire sequences of data (such as speech or video). For example, LSTM is applicable to tasks such as unsegmented, connected handwriting recognition or speech recognition.

<p align="center">
<img src="https://github.com/crypto-code/Simple-Neural-Network/blob/master/assets/LSTM.png" align="middle" />   </p>

The code for the model is present in the LSTM folder, the model can be run from network.py
```
python network.py
```

# G00D LUCK

For doubts email me at:
atinsaki@gmail.com
