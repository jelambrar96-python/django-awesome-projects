from django.db import models 


class GFG(models.Model): 
    name = models.CharField(max_length=100) 


class Item(models.Model): 
    gfg = models.ForeignKey(GFG, on_delete=models.CASCADE) 
    item_title = models.CharField(max_length=100)
