#!/usr/bin/env python
# coding: utf-8

# In[5]:



"""
Check number is prime or not
"""
num=int(input("Enter the number : "))
if num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            print("Numer is not prime")
            break
        else:
            print("number is prime")
else:
    print("Number is prime")


# In[ ]:




