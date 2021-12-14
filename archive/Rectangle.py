#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Dépendances
from ma_rue import rue, affiche
from random import randint

from random import randint
def rectangle(x, y):
    rue.fill_style = "yellow"
    rue.fill_rect(x, y, 140, 60)
    rue.fill_style = "black"
    rue.stroke_rect(x, y, 140, 60)

affiche(rue)

x = 0
for loop in range(4):
    y = 340
    for loop in range(randint(1, 5)):
        rectangle(x, y)
        y = y - 60
    x = x + 200

