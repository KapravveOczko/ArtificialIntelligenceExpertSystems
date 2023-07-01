# ArtificialIntelligenceExpertSystems  
  
  
# +------------------+| zadanie1 = task1 |+------------------+

"The Fifteen Puzzle" is a puzzle consisting of a frame and 15 elements embedded in it. These elements can be moved because there is free space in the frame corresponding to one element  (thus, the entire frame is 4x4 in size). The objective of the puzzle is to move the pieces in such a way that from a certain random initial arrangement, for example:  
  
1 2 7  
8 9 12 10  
13 3 6 4  
15 14 11 5  
  
the pattern corresponding to the following arrangement is obtained:  

1 2 3 4  
5 6 7 8  
9 10 11 12  
13 14 15  
  
# Objective of the Task  
The task consists of two parts: programming and research.

The goal of the programming part is to write a program that will solve the above puzzle using various methods of searching the state space:

-> Breadth-first strategy  
-> Depth-first strategy  
-> Best-first strategy: A* algorithm, with the following heuristics:  
---> The Hamming metric  
--->The Manhattan metric  

The aim of the research part is to investigate the behavior of the aforementioned state space search methods in the case of this problem.


# +------------------+| zadanie2 = task2 |+------------------+

# Task 1: Programming and Research - Neural Network for Error Correction

## Programming Part

**Requirements:**

Design and implement a neural network that can correct errors obtained from a location measurement system.

Design a neural network with the following specifications:
- Select an appropriate type of network.
- Determine the number of layers.
- Decide on the number of neurons in each layer.
- Choose activation functions for each layer.

Implement the neural network using any programming language. Using external libraries for neural network development (such as PyTorch or TensorFlow) will be rewarded with a maximum score of 3.

## Research Part

**Requirements for Maximum Score 4:**

Train the neural network to correct errors in the provided data using any learning method.

Verify the quality of the developed neural network by comparing the error cumulative distribution functions (CDFs) for the test dataset with the ones obtained after filtering using the neural network.

Prepare an XLS or XLSX file containing a single column with the CDF values obtained after filtering using the developed neural network.

Create a report that includes:
- A description of the neural network architecture, including:
  - Type of network.
  - Number of layers.
  - Number of neurons in each layer.
  - Activation functions used in each layer.
  - Weight initialization method in each layer.
  - Input data for the neural network.
- Information about the neural network training method and a summary of the learning process parameters.
- Comparison of the error CDFs for the test dataset with the ones obtained after filtering using the neural network.