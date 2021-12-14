#!/usr/bin/env python
# coding: utf-8

# In[2]:


from ipycanvas import Canvas


# In[43]:


rue = Canvas(width=800, height=400)


# In[44]:


rue


# In[179]:


rue.fill_rect(400, 355, 30, 45)
rue.fill_style= "white"


# In[180]:


rue.stroke_style = "black"
rue.stroke_rect(400, 355, 30, 45)
rue.line_width = 1


# In[178]:


rue.clear()

