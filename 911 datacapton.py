#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df= pd.read_csv(r"C:\Users\suhai\Downloads\archive (1)\911.csv",encoding = "unicode_escape")


# In[3]:


df.info()


# In[4]:


df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[5]:


df['zip'].value_counts().head(5)


# In[6]:


df['twp'].value_counts().head(5)


# In[7]:


df['title'].unique()


# In[8]:


x= df['title'].iloc[0]
x


# In[9]:


x.split(':')


# In[10]:


x.split(':')[0]


# In[11]:


df['reason']=df['title'].apply(lambda title: title.split(':')[0])


# In[12]:


df['reason']


# In[13]:


df['reason'].value_counts()


# In[14]:


sns.countplot(x='reason',data=df)


# In[15]:


type(df['timeStamp'].iloc[0])


# In[16]:


df['timeStamp'] = pd.to_datetime(df['timeStamp'])


# In[17]:


type(df['timeStamp'].iloc[0])


# In[18]:


time=df['timeStamp'].iloc[0]
time.hour


# In[19]:


time.date


# In[20]:


df['hour']= df['timeStamp'].apply(lambda time:time.hour)


# In[21]:


df['Month']= df['timeStamp'].apply(lambda time:time.month)


# In[22]:


df['Day Of Week']= df['timeStamp'].apply(lambda time: time.dayofweek)


# In[23]:


time.dayofweek


# In[24]:


df['hour'].head(-20)


# In[25]:


dmap ={0:'mon',1:'tue',2:'wed',3:'thurs',4:'fri',5:'sat',6:'sun'}


# In[26]:


df['Day Of Week'] = df['Day Of Week'].map(dmap)


# In[27]:


df


# In[28]:


sns.countplot(x='Day Of Week',data=df,hue="reason")


# In[29]:


sns.countplot(x='Month',data=df,hue='reason')


# In[30]:


bymonth= df.groupby('Month').count()


# In[31]:


bymonth


# In[32]:


bymonth['lat'].plot()


# In[33]:


sns.countplot(x='Month',data=df)


# In[34]:


bymonth.reset_index()


# In[35]:


sns.lmplot(x='Month',y="twp",data=bymonth.reset_index())


# In[36]:


t= df['timeStamp'].iloc[1]


# In[37]:


df['Date'] =df['timeStamp'].apply(lambda t:t.date())


# In[38]:


df.head()


# In[ ]:





# In[39]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout()


# In[40]:


df[df['reason']=='Traffic'].groupby('Date').count()["lat"].plot()
plt.title('Traffic')
plt.tight_layout()


# In[44]:


sns.heatmap(hour)


# In[ ]:




