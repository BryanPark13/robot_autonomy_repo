#!/usr/bin/env python3
import numpy as np
if __name__ == "__main__":
   #Matrix Multiplication
    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))
    C = A @ B
    print(C)

    #Slicing and Broadcasting
    np.random.seed(42)
    x = np.random.normal(size=(4, 10)) #creating 4 vectors of size 10, random input 

    x_i = x[:,None,:] #creates 4x1x10 3D array
    x_j = x[None,:,:] #creates 1x4x10 3D array
    
    int = np.square(x_i - x_j) #squares the difference between the x_i and x_j broadcasts to 4x4x10
    D = np.sum(int,axis = 2) #sums the 10 difference values

    print(D)


    