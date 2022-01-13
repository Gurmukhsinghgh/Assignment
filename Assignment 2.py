#!/usr/bin/env python
# coding: utf-8
Problem:-  Create the below pattern using nested for loop in Python.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
# In[21]:


n = 5
for i in range(1,n):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

for i in range(n, 0,-1):
    for j in range (i):
        print("*",end=" ")
    print()
    
    

Problem 2. Write a Python program to reverse a word after accepting the input from the user.
Sample output:
Input word: ineuron
Output: norueni
# In[27]:


word = input('Enter a word "ineuron"')

for char in range (len(word) -1, -1,-1):
    print(word[char], end= "")
print()   


# In[28]:


word = 'ineuron' #Indexing method to rever a string
print(word[-1::-1])


# In[ ]:




