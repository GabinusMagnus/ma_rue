#!/usr/bin/env python
# coding: utf-8

# In[20]:


from ipycanvas import Canvas

rue = Canvas(width=800, height=400)

rue

def sol():
    rue.fill_style = "black"

    rue.fill_rect(0, 397, 760, 3)
    
    y_sol = rue.height-1
    
sol()

