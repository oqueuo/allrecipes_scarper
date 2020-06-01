from my_imports import *
from recipe import Recipe
import pandas as pd
import random


recipe_book = {'1': ['Instant Pot® Chicke...Paprikash', {...}, [...], [...]],
               '10': ["World's Best Lasagna", {...}, [...], [...]], 
               '11': ['Carrot, Potato, and...bage Soup', {...}, [...], [...]], 
               '12': ['Easy Korean Ground Beef Bowl', {...}, [...], [...]], 
               '13': ['Good Old Fashioned Pancakes', {...}, [...], [...]], 
               '14': ["Best Potatoes You'l...ver Taste", {...}, [...], [...]], 
               '15': ['Best Brownies', {...}, [...], [...]], 
               '16': ['Dill Pickle Soup', {...}, [...], [...]], 
               '17': ['Garlic Roasted Chic... Potatoes', {...}, [...], [...]], 
               '18': ['Cake Mix Cinnamon Rolls', {...}, [...], [...]], 
               '19': ['Fluffy Pancakes', {...}, [...], [...]], 
               '2': ['Two-Ingredient Pizza Dough', {...}, [...], [...]], 
               '20': ['Pan-Fried Shrimp', {...}, [...], [...]], 
               '3': ['Best Chocolate Chip Cookies', {...}, [...], [...]], ...}

# Get existing DataFrame from csv file
df_existing = pd.read_csv('C:/Users/Cookie/Desktop/cook_simple/scraper/recipe_book.csv')
# Remove duplicates
print(df_existing)



df = DataFrame(df_existing, index = ['Title','Time', 'Ingredients', 'Directions'])