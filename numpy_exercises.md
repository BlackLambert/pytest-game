# The first 25 numpy exercises 
Source: https://www.machinelearningplus.com/python/101-numpy-exercises-python/


```python
#1. numpy exercise
#Import numpy as np and see the version

import numpy
print(numpy.__version__)
```

    1.18.1
    


```python
#2. numpy exercise
#How to create a 1D array?

result = []
for x in range(10):
    result.append(x)
print(result)

#Numpy variant
import numpy
result = numpy.arange(10)
result
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    




    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




```python
#3. numpy exercise
#How to create a boolean array?

import numpy
numpy.full((3, 3), True, dtype=bool)
```




    array([[ True,  True,  True],
           [ True,  True,  True],
           [ True,  True,  True]])




```python
#4. numpy exercise
#How to extract items that satisfy a given condition from 1D array?

import numpy
result = numpy.arange(10)
result[result % 2 == 1]
```




    array([1, 3, 5, 7, 9])




```python
#5. numpy exercise
#How to replace items that satisfy a condition with another value in numpy array?

import numpy
result = numpy.arange(10)
result[result % 2 == 1] = -1
result
```




    array([ 0, -1,  2, -3,  4, -5,  6, -7,  8, -9])




```python
#6. numpy exercise
#How to replace items that satisfy a condition without affecting the original array?

import numpy
input = numpy.arange(10)
result = numpy.where(input % 2 == 1, -1, input)
print(input)
print(result)
```

    [0 1 2 3 4 5 6 7 8 9]
    [ 0 -1  2 -1  4 -1  6 -1  8 -1]
    


```python
#7. numpy exercise
#How to reshape an array?

import numpy
input = numpy.arange(10)
result = input.reshape(2, -1)
print(result)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]]
    


```python
#8. numpy exercise
#How to stack two arrays vertically?

import numpy
array1 = numpy.arange(10).reshape(2,-1)
array2 = numpy.repeat(1,10).reshape(2,-1)
result = numpy.vstack([array1, array2])
print(result)
```

    [[0 1 2 3 4]
     [5 6 7 8 9]
     [1 1 1 1 1]
     [1 1 1 1 1]]
    


```python
#9. numpy exercise
#How to stack two arrays horizontally?

import numpy
array1 = numpy.arange(10).reshape(2,-1)
array2 = numpy.repeat(1,10).reshape(2,-1)
result = numpy.hstack([array1, array2])
print(result)
```

    [[0 1 2 3 4 1 1 1 1 1]
     [5 6 7 8 9 1 1 1 1 1]]
    


```python
#10. numpy exercise
#How to get the common items between two python numpy arrays?

import numpy
input = numpy.array([1,2,3])
numpy.r_[numpy.repeat(input, 3), numpy.tile(input, 3)]
```




    array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])




```python
#11. numpy exercise
#How to generate custom sequences in numpy without hardcoding?

import numpy
array1 = numpy.array([1,2,3,2,3,4,3,4,5,6])
array2 = numpy.array([7,2,10,2,7,4,9,4,9,8])
numpy.intersect1d(array1,array2)
```




    array([2, 4])




```python
#12. numpy exercise
#How to remove from one array those items that exist in another?

import numpy
array1 = numpy.array([1,2,3,4,5])
array2 = numpy.array([5,6,7,8,9])
numpy.setdiff1d(array1,array2)
```




    array([1, 2, 3, 4])




```python
#13. numpy exercise
#How to get the positions where elements of two arrays match?

import numpy
array1 = numpy.array([1,2,3,2,3,4,3,4,5,6])
array2 = numpy.array([7,2,10,2,7,4,9,4,9,8])
numpy.where(array1 == array2)
```




    (array([1, 3, 5, 7], dtype=int64),)




```python
#14. numpy exercise
#How to extract all numbers between a given range from a numpy array?

import numpy
input = numpy.array([2, 6, 1, 9, 10, 3, 27])
input[(input >= 5) & (input <= 10)]
```




    array([ 6,  9, 10])




```python
#15. numpy exercise
#How to make a python function that handles scalars to work on numpy arrays?

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
    
import numpy
array1 = numpy.array([5, 7, 9, 8, 6, 4, 5])
array2 = numpy.array([6, 3, 4, 8, 9, 7, 1])
pair_max = numpy.vectorize(maxx, otypes=[int])
pair_max(array1, array2)
```




    array([6, 7, 9, 8, 9, 7, 5])




```python
#16. numpy exercise
#How to swap two columns in a 2d numpy array?

import numpy
input = numpy.arange(9).reshape(3,3)
print(input)
input[:, [1,0,2]]
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    




    array([[1, 0, 2],
           [4, 3, 5],
           [7, 6, 8]])




```python
#17. numpy exercise
#How to swap two rows in a 2d numpy array?

import numpy
input = numpy.arange(9).reshape(3,3)
print(input)
input[[1,0,2], :]
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    




    array([[3, 4, 5],
           [0, 1, 2],
           [6, 7, 8]])




```python
#18. numpy exercise
#How to reverse the rows of a 2D array?

import numpy
input = numpy.arange(9).reshape(3,3)
print(input)
input[::-1]
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    




    array([[6, 7, 8],
           [3, 4, 5],
           [0, 1, 2]])




```python
#19. numpy exercise
#How to reverse the columns of a 2D array?

import numpy
input = numpy.arange(9).reshape(3,3)
print(input)
input[:, ::-1]
```

    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    




    array([[2, 1, 0],
           [5, 4, 3],
           [8, 7, 6]])




```python
#20. numpy exercise
#How to create a 2D array containing random floats between 5 and 10?

import numpy
result = numpy.random.uniform(5,10, size=(5,3))
print(result)
```

    [[6.14482025 8.68671572 5.86708083]
     [9.11359812 5.52489847 7.86029302]
     [5.4051009  8.93031969 8.35757468]
     [8.79025095 7.24520674 6.54119855]
     [8.01656464 8.31842135 5.19769185]]
    


```python
#21. numpy exercise
#How to print only 3 decimal places in python numpy array?

import numpy
input = numpy.random.uniform(5,10, size=(5,3))
numpy.set_printoptions(precision=3)
input[:4]
```




    array([[6.136, 6.951, 8.093],
           [8.704, 7.933, 7.431],
           [7.291, 9.601, 6.319],
           [7.67 , 5.611, 5.824]])




```python
#22. numpy exercise
#How to pretty print a numpy array by suppressing the scientific notation (like 1e10)?

import numpy
numpy.set_printoptions(suppress=False)
numpy.random.seed(100)
input = numpy.random.random([3,3])/1e3
print(input)
numpy.set_printoptions(suppress=True, precision=6)
input 
```

    [[5.434e-04 2.784e-04 4.245e-04]
     [8.448e-04 4.719e-06 1.216e-04]
     [6.707e-04 8.259e-04 1.367e-04]]
    




    array([[0.000543, 0.000278, 0.000425],
           [0.000845, 0.000005, 0.000122],
           [0.000671, 0.000826, 0.000137]])




```python
#23. numpy exercise
#How to limit the number of items printed in output of numpy array?

import numpy
numpy.set_printoptions(threshold=6)
result = numpy.arange(15)
result
```




    array([ 0,  1,  2, ..., 12, 13, 14])




```python
#24. numpy exercise
#How to print the full numpy array without truncating?

import numpy
import sys
numpy.set_printoptions(threshold=6)
result = numpy.arange(15)
numpy.set_printoptions(threshold=sys.maxsize)
result
```




    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])




```python
#25. numpy exercise
How to import a dataset with numbers and texts keeping the text intact in python numpy?

import numpy
import sys
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = numpy.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris[:3]
```




    array([[b'5.1', b'3.5', b'1.4', b'0.2', b'Iris-setosa'],
           [b'4.9', b'3.0', b'1.4', b'0.2', b'Iris-setosa'],
           [b'4.7', b'3.2', b'1.3', b'0.2', b'Iris-setosa']], dtype=object)




```python

```
