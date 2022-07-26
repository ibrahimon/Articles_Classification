#!/usr/bin/env python
# coding: utf-8

# In[252]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn


# In[253]:


data = pd.read_json('articles.json')


# In[254]:


data.head(20)


# In[255]:


data.shape


# In[256]:


data.info()


# In[257]:


articles = data.sample(frac=1).reset_index(drop = True)


# In[258]:


articles.head(10)


# In[259]:


train_data = articles.iloc[:1990,:]
test_data = articles.iloc[1901:,:]


# In[260]:


train_data


# In[261]:


test_data


# In[262]:


art_dic = {'Engineering':0, 'Product & Design':1,'Startups & Business':2}


# In[263]:


train = train_data.pop('body').values
train_target_art = train_data.pop('category').values


# In[264]:


train


# In[265]:


train_target_art


# In[266]:


test = test_data.pop('body').values
test_target_art = test_data.pop('category').values


# In[267]:


art_dic = {'Engineering':0, 'Product & Design':1,'Startups & Business':2}
train_target_art = train_data.pop('category').values
train_target = [art_dic[article] for article in train_target_art]
test_target = [art_dic[article] for article in test_target_art]


# In[268]:


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer(stop_words = 'english', min_df=5)
x_train_counts = count_vect.fit_transform(train)
x_train_counts.shape


# In[245]:


from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()
x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)
x_train_tfidf.shape


# In[246]:


from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
text_model_svm = Pipeline([('vect', CountVectorizer()),('tfidf',TfidfTransformer()),('class_svm',LinearSVC())])


# In[247]:


trained_model = text_model_svm.fit(train, train_target)
predic_svm =  text_model_svm.predict(test)
test_1 = ['Performance & Usage at Instagram']
red_svm = text_model_svm.predict(test_1)
print(red_svm)


# In[ ]:


np.mean(predic_svm == test_target)


# In[ ]:





# In[ ]:




