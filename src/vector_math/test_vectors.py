#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2020-03-23 12:58:52 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#

import numpy as np
import scipy as sc
import sys

sys.path.insert(0,'/home/trottar/Programs/my_programs/physics_engine/vector_math/physics_vectormath')
import physics_vectormath as vmath

# Single Vectors
v = vmath.Vector3(5, 0, 0)
v.normalize()
print(v)                          # >> [1, 0, 0]
print(v.x)                        # >> 1.0

# VectorArrays are much faster than a for loop over Vectors
v_array = vmath.Vector3Array([[4, 0, 0], [0, 2, 0], [0, 0, 3]])
print(v_array.x)                  # >> [4, 0, 0]
print(v_array.length)             # >> [4, 2, 3]
print(v_array.normalize())        # >> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# VectorArrays are much faster than a for loop over Vectors
v4_array = vmath.Vector4Array([[4, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 1]])
print(v4_array.x)                  # >> [4, 0, 0, 0]
print(v4_array.length)             # >> [4, 2, 3, 1]
print("Metric: ")
print(v4_array.metric)             # >> Metric
print("Normalize:")
print(v4_array.normalize())        # >> [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

# Vectors can be accessed individually or in slices
print(type(v_array[1:]))          # >> vectormath.Vector3Array
print(type(v_array[2]))           # >> vectormath.Vector3

# Vectors can be accessed individually or in slices
print(type(v4_array[1:]))          # >> vectormath.Vector4Array
print(type(v4_array[2]))           # >> vectormath.Vector4

# All these classes are just numpy arrays
print(isinstance(v, np.ndarray))  # >> True
print(type(v_array[1:, 1:]))      # >> numpy.ndarray
print(type(v4_array[1:, 1:]))      # >> numpy.ndarray


