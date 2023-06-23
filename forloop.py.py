#!/usr/bin/env python
# coding: utf-8

# In[1]:


price=int(input())
if price>1000:
    print('i will be purchese')
else:
    print('i will not purchese')


# In[5]:


price=int(input())
if price>1000:
    print('i will be purchese')
    if price>5000:
        print('this is too much')
    elif price<2000:
        print('its okk')
else:
    print('i will not purchese')


# In[6]:


l=[2,3,4,5,6,7,8,9]


# In[15]:


l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)


# l1

# In[16]:


l1


# In[17]:


l=['swaraj','katiyar','data science']


# In[20]:


l1=[]
for i in l:
    print(i)
    l1.append(i.upper())


# In[21]:


l1


# In[23]:


l=[2,3,4,5,'swaraj',3.4,'True',354.6]


# In[30]:


l1=[]
l2=[]
for i in l:
    print(i)
    if type(i)==int or type(i)==float:
        l1.append(i)
    else:
         l2.append(i)
  


# In[31]:


l1


# In[32]:


l2


# In[ ]:




