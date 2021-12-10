#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ipycanvas import Canvas


# In[3]:


rue = Canvas(width=800, height=400)


# In[4]:


rue


# In[35]:


rue.fill_style = 'rgb(240, 255, 255)'
rue.fill_rect(10, 10, 30, 30)


# In[36]:


rue.stroke_style = "black"
rue.stroke_rect(10, 10, 30, 30)
rue.line_width = 1


# In[34]:


rue.clear()

