Simple Neural Network for Classification

This project implements a simple neural network with a backpropagation algorithm for binary classification. It uses two weights and a bias to classify data into two classes: blue and red.
Description

The model takes two inputs, x and y, and predicts an output value that represents a class (0 or 1). The network uses the sigmoid activation function to determine the output and applies gradient descent to update the weights during training.

The training data is divided into two classes:

    Blue (class 0)
    Red (class 1)

Features

    Learning: The model is trained using the gradient descent loop with a learning rate of 0.9.
    Classification: The network can predict the class of new data points after training.
    Weights and Bias: The weights and bias are updated iteratively to minimize the prediction error.

Technologies

    Python 3.x
    math and random for mathematical calculations and random number generation.

How to Run

    Clone the repository:

git clone https://github.com/<your_name>/<repository_name>.git

Run the Python script:

    python3 neural_network.py

Results

At the end of training, the program will print the final error and the updated weights. It will also provide predictions for two test points.
Example Output:

P1 0.72165
P2 0.34512
B 0.98743

Err: 0.00512
P1 0.81265
P2 0.45123
B 0.89034

Prediction [2, 2, 1]:
Value: 1 - Predict: 0.98423

Prediction [0.5, 0.5, 0]:
Value: 0 - Predict: 0.11234

Contributions

If you would like to contribute to this project, please fork the repository and submit a pull request. Any improvements to the code or suggestions are welcome!
