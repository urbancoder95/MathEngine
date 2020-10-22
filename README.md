# MathEngine

## About
Developing a math based framework from scratch. Although I am a __beginner__ at this but I have been stoked by the ability of libraries like [`Tensorflow`](https://tensorflow.org) and [`Numpy`](https://www.numpy.org/) have the capability of representing and solving any form of equation, also the ability to perform autograd. So I thought I'll give it a shot at developing a framework like these from scratch. 

~~__NOTE:__ I am not concerned about the arrangements of struture of the files and classes as of yet, because developing the basic mth engine is a priority for now.~~


## Updates 

Dates are in DD-MM-YYYY format.

1. (15-08-2019) By the last comit I restructured the classes and changed certain code structures to their logic. `Node` is a better abstract class with just the name attribute. I still need to figure out a better representation for the classes to handle during printing and being used for operations.
2. (15-08-2019) Completed functionality of shape method in the `Tensor` class and created the `Constant` class. Started working on the op nodes. 
3. (21.10.2020) Changed the shape method to shapenew which computes the shape of the given tensor and throws appropriate DIMENSION MISMATCH error
                in case of any mismatch in any level.

__IMPROVEMENT NOTES:__ Change the inheritence from list to iterator. Define Tensor class from scratch with changes to value indexing. 
