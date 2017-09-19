from django.shortcuts import render
from django.views import View

from .models import New
import requests
from bs4 import BeautifulSoup
import re

def nba(request):
    url = 'https://nba.udn.com/nba/index'
    NBA_hot = requests.get(url)
    NBA_hot.encoding='utf-8'
    NBA_hot_soup = BeautifulSoup(NBA_hot.text, 'html.parser')
    NBA_hot_list = NBA_hot_soup.findAll('div', attrs={'id': 'news', 'class':'box'})
    NBA_hot_list2 = NBA_hot_list[0].findAll('dt')
    show = []
    for host_list in NBA_hot_list2:
        obj = {}
        temp = host_list.find('a')
        url = "https://nba.udn.com/" + temp['href']
        NBA_detail = requests.get(url)
        NBA_detail.encoding='utf-8'
        NBA_detail_soup = BeautifulSoup(NBA_detail.text, 'html.parser')

        findID = NBA_detail_soup.find('div', attrs={'id' : 'story_body'})
        obj['article_id'] = findID['data-article']

        total = NBA_detail_soup.find('div', attrs={'id' : 'story_body_content'})

        obj['title'] = total.find('h1', attrs={'class':'story_art_title'}).text

        image = total.findAll( 'img', {})
        obj['imagelink'] = image[0]['data-src']
        content = total.findAll('p')
        content[0].find('div', {'class':'only_web'}).decompose()
        obj['content'] = content[0].text
        if New.objects.filter( unique_id = obj['article_id']) :
            print( 'Exist' )
            pass
        else:
            New.objects.create( unique_id = obj['article_id'], title = obj['title'],
                            content= obj['content'], image_link = obj['imagelink'] )
            show.append(obj)
            print('Success add a article')

    return render(request, "nba_news/NBA.html", {"obj": show })
