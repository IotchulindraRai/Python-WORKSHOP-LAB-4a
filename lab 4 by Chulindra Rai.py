#!/usr/bin/env python
# coding: utf-8

# In[1]:


#a.String declaration, traversing, slicing, concatenating, and sorting in a list.
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


# In[2]:


str = 'Python programing'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])


# In[3]:


str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)


# In[4]:


a = ("b", "g", "a", "d", "f", "c", "h", "e")
print(a)
x = sorted(a)
print(x)


# In[5]:


a = ("b", "g", "a", "d", "f", "c", "h", "e")
print(a)
x = sorted(a,reverse=True)
print(x)


# In[6]:


str="def abcd"
print(str)
print(len(str))

x=sorted(str)
print(x)

x=sorted(str,reverse=True)
print(x)


# In[7]:


my_str = "data science Data Science"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()
print(words)
# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)


# In[11]:


my_str = "data science Data Science"
my_str=my_str.casefold()
# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = my_str.split()

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)


# In[9]:


#sort(): It is used to sort the elements in a list.
#It is a destructive process that sort the original list in place.
#By default, the list is sorted in ascending order. 
#If you want to sort in descending order, set the parameter reverse to True.
a=[5,4,2,6,1]
print("Before sorting:",a)
print(id(a))
b=a.sort(reverse=True)
print("After sorting:",a)
print(id(a))
print("After sorting:",b)
print(id(b))


# In[12]:


a=[5,4,2,6,1]
print("Before sorting:",a)
a.sort(reverse=True)
print("After sorting:",a)


# In[13]:


#sorted() returns a sorted list. The original list remains unchanged.
a=[5,4,2,6,1]
print("Before sorting:",a)
b=sorted(a)
print("After sorting:",b)
print(id(a))
print(id(b))


# In[14]:


my_str=input("Enter the string:")
# make it suitable for caseless comparison
my_str = my_str.casefold()
# reverse the string
rev_str = reversed(my_str)
# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print(my_str," is palindrome")
else:
    print(my_str," is not palindrome")


# In[16]:


# define punctuation
punctuations = '''!()`-[]{};:'"\,<>./?@#$%^&*_~'''

# To take input from the user
my_str = input("Enter a string: ")
# remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# In[ ]:




