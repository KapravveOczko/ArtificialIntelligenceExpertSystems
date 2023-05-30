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
