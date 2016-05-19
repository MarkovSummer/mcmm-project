
# coding: utf-8

# Look Python PEP for information about how to properly (and beautifully) code in Python.
# Look at google: numpy + "term" (svd for example) for information about numpy functions.

# Numpy array:
# np.array([[0,1,2,3],[4,5,6,7]]) creates a matrix 2x4.

# In[ ]:

import numpy as np


# In[ ]:

M1=np.array([[0.5,0.5],[0.1,0.9]])
M1


# In[ ]:

M2=np.random.rand(3,3)
M2


# In[ ]:

M3=np.array([[0,1,2,3],[4,5,6,7]])
len(M3)


# In[ ]:

[i for i in range(len(M2[0]))]


# In[ ]:

m1=M1.sum(axis=1)
m3=M3.sum(axis=1)
m3


# In[ ]:

M3[1,:]


# In[ ]:

m1[:,np.newaxis]


# In[ ]:

d=np.array([[2,2],[2,4]])


# In[ ]:

dd=np.array([[1,4],[4,1]])


# In[ ]:

M1=np.array([[0.5,0.5],[0.1,0.9]])
M1/=d
M1


# In[ ]:

M1=np.array([[0.5,0.5],[0.1,0.9]])
M1/=dd
M1


# In[ ]:

M1/=m1[:,np.newaxis]
M1


# In[ ]:

def normalize(T):
    """
    Given a matrix T, returns another one, T0, with rows that add to 1
    """
    T0=np.array(T)
    s=T0.sum(axis=1)
    print(s)
    T0/=s[:,np.newaxis]
    return T0


# In[ ]:

normalize(M2)


# In[ ]:

def stationary_sol(T):
    """
    Given a random matrix T, returns a stationary sol a, s.t. aT=a
    """
    T0=normalize(T)
    eig=np.linalg.eig(T0)
    for i in range(len(eig)):
        if eig[0][i]==1:
            return eig[1][i]


# In[ ]:

stationary_sol(M2)


# In[ ]:

stationary_sol(M1)


# In[ ]:

eig=np.linalg.eig(M1)
eig


# In[ ]:

eig[0][1]


# In[ ]:



