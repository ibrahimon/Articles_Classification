#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn


# In[2]:


data = pd.read_json('articles.json')


# In[3]:


data.head(20)


# In[4]:


data.shape


# In[5]:


data.info()


# In[6]:


data.describe().T


# In[9]:


articles = data.sample(frac=1).reset_index(drop = True)


# In[10]:


articles.head(10)


# In[15]:


train_data = articles.iloc[:1990,:]
test_data = articles.iloc[1901:,:]


# In[16]:


train_data


# In[17]:


test_data


# In[13]:


art_dic = {'Engineering':0, 'Product & Design':1,'Startups & Business':2}


# In[14]:


train = train_data.pop('body').values
train_target_art = train_data.pop('category').values


# In[18]:


train


# In[19]:


train_target_art


# In[21]:


test = test_data.pop('body').values
test_target_art = test_data.pop('category').values


# In[22]:


art_dic = {'Engineering':0, 'Product & Design':1,'Startups & Business':2}
train_target_art = train_data.pop('category').values
train_target = [art_dic[article]for article in train_target_art]
test_target = [art_dic[article]for article in test_target_art]


# In[23]:


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(stop_words = 'english', min_df=5)
x_train_counts = count_vect.fit_transform(train)
x_train_counts.shape


# In[24]:


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
x_train_tfidf.shape


# In[25]:


from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB().fit(x_train_tfidf, train_target)


# In[28]:


from sklearn.pipeline import Pipeline
text_model_nb = Pipeline([('vect', CountVectorizer()),('tfidf',TfidfTransformer()),('class_nb',MultinomialNB())])


# In[29]:


trained_model = text_model_nb.fit(train, train_target)


# In[30]:


predic_nb = text_model_nb.predict(test)


# In[31]:


np.mean(predic_nb == test_target)


# In[44]:


from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
text_model_svm = Pipeline([('vect', CountVectorizer()),('tfidf',TfidfTransformer()),('class_svm',LinearSVC())])


# In[45]:


trained_model = text_model_svm.fit(train, train_target)


# In[46]:


trained_model = text_model_svm.fit(train, train_target)
predic_svm =  text_model_svm.predict(test)
test_1 = ['Performance & Usage at Instagram']
red_svm = text_model_svm.predict(test_1)
print(red_svm)


# In[48]:


np.mean(predic_svm == test_target)


# In[ ]:




