# django-nba-webscraping
將nba中文官方網站上的焦點新聞儲存至資料庫中

##### 此專案運行在heroku平台上
##### 網址為 https://nick-nba-scraping.herokuapp.com/ 

#### 版本
```cmd
python : 3.5.2
django : 1.10.3
requests : 2.18.4
beautifulsoup4 : 4.6.0
djangorestframework : 3.6.4
django-celery : 3.2.1
```

#### 使用方法： <br>
```cmd
cd ChuangShun
source bin/activate
cd src 
python manage.py runserver
```

#### 開啟瀏覽器 127.0.0.1:8000 即可看到目前已儲存的文章
##### 點選標題或 view 可看文章內容
##### 點擊右上方的 update article, 程式會去爬蟲 nba官方網站, 並將資料存到資料庫中


#### 開啟瀏覽器 127.0.0.1:8000/admin 可觀看儲存的資料
```cmd
帳號 test
密碼 test1234
```


#### 在local端使用 django-celery 來實做定時爬蟲
##### 使用方法：
##### 設定在admin中的  DJCELERY -> Periodic tasks, 
##### 點擊 ADD PERIODIC TASK後設定 Name、 Interval & Task( nba_news.tasks.update_news)

```cmd
另外開啟2個終端機

一個執行       python manage.py celery worker -l info

接著另一個執行  python manage.py celery beat
```
##### 即可定時在背景自動執行抓取文章的function!

