# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.NumPy stands for Numerical Python.

# to import our numpy library we have to use "import" key word

import numpy as np         # NumPy is usually imported under the np alias.alias: In Python alias are an alternate name for referring to the same thing.

arr = np.array([[1, 2, 3], [4, 5, 6]])  # Creating an array and giving values 1,2,3,4,5,6.

print(arr)

print(np.__version__)    # The version string is stored under __version__ attribute.

print(type(arr))         # type is build_in function which tells the type of array.


pk = np.array(43)        # 0 dimension array {"Array having only one value"}
print(pk)

d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])      # three dimension array
print(d.ndim)
print('2nd element on 1st row: ', arr[0, 1])   # this code will print 0,1 index value.