#!/usr/bin/env python
# coding: utf-8

# # Linear Regression with Gradient Descent (HW 2 Part 4/4)
# 
# The code below contains the required `import` statements, and generates data for this HW. 
# 
# **(Copy in your solutions to the last HW, run the code below)**
# 
# **Note:** if you are unsure of your solutions, contact me and I'll provide them to you. (I'll just need to verify that you've turned in the last HW already). 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
get_ipython().run_line_magic('matplotlib', 'inline')

rng = np.random.RandomState(1234)

vec_len = 50
X = np.linspace(0, 1, vec_len)
dy = 0
Y = 3.1 * X + 4.3 + dy * rng.randn(vec_len)

def error_fx(x, y, m, b):
    #Copy your solution here

def partial_error_fx(X, Y, m, b, i, delta):
    #Copy your solution here

def grad_error_fx(X, Y, m, b, delta):
    #Copy your solution here


# **Problem**
# 
# We will now iteratively change ``m`` and ``b`` to try to find the optimal values for each.
# 
# Let the amount we're changing ``m`` and ``b`` be called ``step`` (a `float`)
# 
# We will move `m` and `b` in the **opposite** direction of the gradient to determine their optimal values.
# 
# Write a function ``grad_step(X, Y, m, b, delta, step)`` to update the ```m``` and ```b``` values after moving them by `step`
# 
# **Note:** although it is possible to solve for the gradient of the error function analytically, here I'm asking you to use the partial difference quotient (i.e. use `grad_error_fx`) to estimate the partial derivatives.
# 
# **Function name:** 
# 
# * ```grad_step```
# 
# **Input arguments:** 
# 
# * ```X```: `Numpy array` of x values of the data
# * ```Y```: `Numpy array` of y values of the data
# * ```m```: slope, `float`
# * ```b```: *y*-intercept, `float`
# * ```delta```: `float` (representing $\Delta$ in the above equations)
# * ```step```: `float` the step size used to update both ```m``` and ```b``` during the gradient descent learning process
# 
# **Output:** 
# 
# * ```new_m, new_b```, both `float`
# 
# **Hints:**
# 
# * Start by estimating the gradient of the error function using `grad_error_fx()`
# 
# * Then, update the values of `m` and `b` by taking a step in the direction opposite to the gradient.

# In[ ]:


def grad_step(X, Y, m, b, delta, step):
    # YOUR CODE HERE
    raise NotImplementedError()
    return (new_m, new_b)


# In[ ]:





# **Problem**
# 
# * Write a `for` loop that uses `grad_step()` to find the optimal ```m``` and ```b``` values. 
# 
# * Save the ```m``` and ```b``` values at each step in arrays called ```m_vec``` and ```b_vec```, respectively. 
# 
# * Choose starting values ```m, b = 0, 0```
# 
# * Run the for loop 1500 times
# 
# **Function name:** 
# 
# (none-don't create a function)
# 
# **Input arguments:** 
# 
# (n/a)
# 
# **Output:** 
# 
# * ```m_vec``` containing the `list` of ```m``` values
# * ```b_vec``` containing the `list` of ```b``` values
# 
# **Hints:**
# 
# * Use the `grad_step()` function to update the values of `m` and `b` and use the `append()` method to include all of the `m` and `b` values in the respective `lists`: `m_vec` and `b_vec`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:





# Now, we will repeat the problem with noisy data.
# 
# **(Run this code)**

# In[ ]:


rng = np.random.RandomState(1234)

vec_len = 50
X_noisy = np.linspace(0, 1, vec_len)
dy = 1
Y_noisy = 3.1 * X + 4.3 + dy * rng.randn(vec_len)

plt.scatter(X_noisy, Y_noisy, marker='.', color='b')
plt.show()


# **Problem**
# 
# * Create new variables `m_noisy` and `b_noisy` for the slope and intercept fit to this noisy data. 
# 
# * Again , write a `for` loop that uses `grad_step()` to  update the ```m_noisy``` and ```b_noisy``` values at the end of each step. 
# 
# * Save the ```m_noisy``` and ```b_noisy``` values in arrays called ```m_vec_noisy``` and ```b_vec_noisy```, respectively. 
# 
# * Choose starting values ```m_noisy, b_noisy = 0, 0```
# 
# * Run the for loop 1500 times (or 'epochs')
# 
# **Function name:** 
# 
# (none-don't create a function)
# 
# **Input arguments:** 
# 
# (n/a)
# 
# **Output:** 
# 
# * ```m_vec_noisy``` containing the `list` of ```m_noisy``` values
# * ```b_vec_noisy``` containing the `list` of ```b_noisy``` values
# 
# **Hints:**
# 
# * Use the `grad_step()` function on `X_noisy` and `Y_noisy` to update the values of `m_noisy` and `b_noisy` and use the `append()` method to include all of the `m_noisy` and `b_noisy` values in the respective `lists`: `m_vec_noisy` and `b_vec_noisy`.

# In[ ]:


# YOUR CODE HERE
raise NotImplementedError()


# In[ ]:




