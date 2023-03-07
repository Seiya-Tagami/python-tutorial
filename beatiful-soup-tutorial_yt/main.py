from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.orangepage.net/recipes/search?utf8=%E2%9C%93&search_recipe%5Bkeyword%5D=%E3%81%AB%E3%82%93%E3%81%98%E3%82%93&button=')
soup = BeautifulSoup(res.text, 'html.parser')

# タグ指定
# h2_tags = soup.find_all('h2')
# h2_strings = [x.string for x in h2_tags]
# print(h2_strings)

# class, id指定
# recipes = soup.find('div', id="recipe_list", class_="recipesList")
# p_tit_tags = recipes.find_all('h2', class_="tit")
# print([x.string for x in p_tit_tags])

# 属性指定
recipes = soup.find('div', id="recipe_list", class_="recipesList")
a_tag = recipes.find_all('a')
print([x['href'] for x in a_tag])