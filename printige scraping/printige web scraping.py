#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup


# In[3]:


import requests


# In[4]:


pages = []
for i in range(1,8):
    pages.append(f'https://printige.net/product-category/ai-data-science/data-science/page/{i}/')
    
pages    


# In[19]:


book_name = soup.find_all('p',{"class":"name product-title woocommerce-loop-product__title"})
book_price = soup.find_all('span',{'class':'price'})

book_names = []
book_prices = []
for url in pages:
    client = requests.get(url)
    html = client.text
    soup = BeautifulSoup(html,'html.parser')
    
    for i in range(len(book_name)):
        book_names.append(book_name[i].text)
    for i in range(len(book_price)):
        book_prices.append(book_price[i].text)
    
    


# In[13]:


import pandas as pd


# In[21]:


df = pd.DataFrame({'book name ': book_names , 'book price' : book_prices})
print(df)



# In[ ]:




