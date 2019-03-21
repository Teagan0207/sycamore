
# coding: utf-8

# In[59]:


import random

def some(x, n):
    a=random.sample(list(x.index),n)

    x.loc[a]=-x.loc[a]


# In[60]:


import pandas as pd
train=pd.read_csv(r'processed.csv')
#df=df.drop(['score'],axis=1)


# In[61]:



some(train,556)


# In[62]:


train['result']=train['result'].where(train['result']==1,0)
train['region']=train['region'].where(train['region']==0,1)
train['lat']=train['lat'].abs()
train['long']=train['long'].abs()
train['slot']=train['slot'].abs()
train['num_ot']=train['num_ot'].where(train['num_ot']==0,1)



# In[63]:


train=train.drop(['Unnamed: 0','region'],axis=1)


# In[64]:



train.to_csv('train_updated.csv')


# In[65]:


len(train.columns)


# In[66]:


train.columns


# In[ ]:





# In[ ]:




