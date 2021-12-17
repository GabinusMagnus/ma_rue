#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipycanvas import Canvas


# In[2]:


rue = Canvas(width=800, height=400)


# In[3]:


rue


# In[29]:


rue.fill_style = 'rgb(240, 255, 255)'
rue.fill_rect(10, 10, 30, 30)


# In[30]:


rue.stroke_style = "black"
rue.stroke_rect(10, 10, 30, 30)
rue.line_width = 1


# In[28]:


rue.clear()

