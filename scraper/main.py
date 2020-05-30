from my_imports import *
from recipe import Recipe
import pandas as pd

# Add incognito argument to webdriver
option = webdriver.ChromeOptions()
option.add_argument("- incognito")

# Make a Chrome instance
br = webdriver.Chrome(executable_path='C:/Program Files (x86)/Google/Chrome/chromedriver.exe')

"""
Make the Request
"""
# 1. Pass in the desired website url
br.get("https://www.allrecipes.com/")
# 2. Implement a Try/Except to handle if website times out
timeout = 20
try:
    WebDriverWait(br, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "fixed-recipe-card__img")))
except TimeoutException:
    print("Timed out waiting for AllRecipes to load")
    br.quit

"""
Get the Response. We will be getting recipes on the front page of allrecipes.com
"""
# 1. URLS of the year in which we want the Hall of Fame recipes
recipe_grid = br.find_element_by_id("fixedGridSection")
recipe_box = recipe_grid.find_elements(By.CLASS_NAME, "favorite")

recipe_id = []
urls = []
for i, recipe in enumerate(recipe_box):
    recipe_id.append(recipe.get_attribute('data-id'))
    urls.append('https://allrecipes.com/recipe/' + str(recipe_id[i]))

# 2. Scrape each url
rec = Recipe()
recipe_book = {}
for i, url in enumerate(urls):
    br.get(url)
    time.sleep(10)
    title_and_info = rec.scrape_recipe(br)
    recipe_book[title_and_info[0]] = title_and_info[1]

df = pd.DataFrame.from_dict(recipe_book)
df.to_csv(r'C:/Users/Cookie/Desktop/cs130-stuff/scraper-tutorial-medium/recipe-book.csv')