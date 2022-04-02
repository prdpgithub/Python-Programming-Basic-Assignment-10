#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to find sum of elements in list?


total = 0

l = [11, 5, 17, 18, 23]

for i in range(0, len(l)):
    total = total + l[i]

print("Sum of all elements in given list: ", total)


# In[2]:


#2.	Write a Python program to  Multiply all numbers in the list?

total = 1

l = [11, 5, 17, 18, 23]

for i in range(0, len(l)):
    total = total * l[i]

print("Multiply of all elements in given list: ", total)


# In[3]:


#3.	Write a Python program to find smallest number in a list?

list1=[2,5,4,3,1]
list1.sort()

print("Smallest element is:",list1[:1])


# In[4]:


#4.	Write a Python program to find largest number in a list?

l1=[2,5,4,3,1]

for i in range(0, len(l1)):
    if l1[i]> max(l1):
        l1[i]= max(l1)
print("largest element is:",max(l1))


# In[5]:


#5.	Write a Python program to find second largest number in a list?

l1=[2,5,4,3,1]
secondLargest = l1[0]
largest = l1[0]
for i in range(0,len(l1)):
        if l1[i] > largest:
            largest = l1[i]
for i in range(0,len(l1)):
        if l1[i] > secondLargest and l1[i] != largest:
            secondLargest = l1[i]
            print("secondLargest",l1[i])


# In[6]:


# 6.	Write a Python program to find N largest elements from a list?

l = [1000,298,3579,100,200,-45,900]
n = 4
  
l.sort()
print(l[-n:])


# In[7]:


# 7.	Write a Python program to print even numbers in a list?

l = [1,2,3,4,5,6,7,8]
for i in range(0, len(l)):
    if i%2==0:
        print(i)


# In[8]:


# 8.	Write a Python program to print odd numbers in a List?

l = [1,2,3,4,5,6,7,8]
for i in range(0, len(l)):
    if i%2!=0:
        print(i)


# In[9]:


# 9.	Write a Python program to Remove empty List from List?


l = [5, 6, [], 3, [], [], 9]

l = [i for i in l if i != []]

print ("List after empty list removal : ", l)


# In[10]:


# 10.	Write a Python program to Cloning or Copying a list?

l1 = [1, 2,3,4,5,6]
l2=[]
l2= [i for i in l1]
print(l2)


# In[11]:


# 11.	Write a Python program to Count occurrences of an element in a list?

l = [ 2,3,4,5,6,3,5,6]
l.count(6)


# In[ ]:




