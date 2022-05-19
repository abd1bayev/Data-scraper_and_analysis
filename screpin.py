from operator import itemgetter

import pandas as pd
import requests
from bs4 import BeautifulSoup
import seaborn as sns
import matplotlib.pyplot as plt


# kun_uz = BeautifulSoup(requests.get('https://kun.uz/').text, 'html.parser')
# v = kun_uz.find_all("dev", class_='big-news__content')[0].select_one('div.big-news__description')
# print(v)

def kun_uz(url):
    return requests.get(url)


def qator(page):
    soup = BeautifulSoup(page.text, "html.parser")
    a = soup.find_all("div", class_="single-content")
    return a


def aylantirish(html_repos):
    result = []
    # print(html_repos.text)
    for row in html_repos:
        kun = ','.join(sorted(row.text.split()))
        result.append(kun.split(','))
        # print(result)
        return result


def toza_data(repositories_data):
    res = []
    # a = pd.Series(repositories_data)
    # print(a)

    for x in repositories_data[0]:

        if x.startswith("("):
            continue
        if x.startswith("-"):
            continue
        if x.startswith("«"):
            continue
        if x.startswith("Анн"):
            continue
        if x.startswith("У"):
            continue
        if x.startswith("НАТОга"):
            continue
        if x.startswith("НАТОнинг"):
            continue
        if x.startswith("икки"):
            continue

        if x.isdigit():
            continue
        if x == "/":
            continue
        if x == "ва":
            continue
        if x == "билан":
            continue
        if x == "бу":
            continue
        if x == "учун":
            continue
        if x == "бир":
            continue

        if x == "ҳам":
            continue

        if x == '':
            continue
        else:
            res.append(x)

    return res


def data_sanash(data):
    sanash = {element: data.count(element) for element in data}

    sort = sorted(sanash.items(), key=itemgetter(1), reverse=True)

    main = sort[0:16]

    return main


def vizual(tayyor):
    viz = pd.DataFrame.from_dict(tayyor)
    viz = viz.rename(columns={0: 'words', 1: 'count'})
    sns.barplot(x='count', y='words', data=viz)
    return plt.show()
    # return viz


def _main():
    url = "https://kun.uz/news/2022/05/17/nato-kengaymoqda-kremlning-reaksiyasi-hayratlanarli-darajada-bosiq-nima-uchun"
    page = kun_uz(url)
    html_repos = qator(page)
    repositories_data = aylantirish(html_repos)
    data = toza_data(repositories_data)
    tayyor = data_sanash(data)
    vizualiz = vizual(tayyor)

    print(vizualiz)


_main()
