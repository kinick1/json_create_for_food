import urllib.request
from bs4 import BeautifulSoup
import json

def PageCrawler(recipeUrl):
    url = 'https://www.10000recipe.com/' + recipeUrl
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    recipe_title = []
    recipe_source = {}
    recipe_step = []
    recipe_tag = []

    res = soup.find('div', 'view2_summary')
    res = res.find('h3')
    recipe_title.append(res.get_text())
    res = soup.find('div', 'view2_summary_info')
    recipe_title.append(res.get_text().replace('\n', ''))

    res = soup.find('div', 'ready_ingre3')

    try:
        for n in res.find_all('ul'):
            source = []
            title = n.find('b').get_text()
            recipe_source[title] = ''
            for tmp in n.find_all('li'):
                source.append(tmp.get_text().replace('\n', '').replace(' ', ''))
            recipe_source[title] = source 
    except AttributeError:
        return

    res = soup.find('div', 'view_step')
    i = 0
    for n in res.find_all('div', 'view_step_cont'):
        i = i + 1
        recipe_step.append('#' + str(i) + ' ' + n.get_text().replace('\n', ' '))

    if res.find('div', 'view_tag'):
        recipe_tag = res.find('div', 'view_tag').get_text()

    if not recipe_step:
        return

    recipe_all = [recipe_title, recipe_source, recipe_step, recipe_tag]
    return recipe_all

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

recipe_data = PageCrawler("URL")  # "recipeUrl" 부분을 원하는 레시피 URL로 변경해주세요.
save_to_json(recipe_data, 'name.json') # 원하는 이름을 name에 입력
