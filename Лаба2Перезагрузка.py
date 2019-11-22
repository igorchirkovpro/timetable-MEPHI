# coding=utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, time, date, timedelta
import calendar
import urllib
import json
week = ''
fileWithFirstDay = open('D:\Папка\Python\Files for Pycharm\JSON\FirstDay.json', 'r', encoding='utf8') # файл с датой первого учебного дня в семестре
firstDay = json.loads(fileWithFirstDay.read())
now = datetime.now() # текущая дата
if calendar.day_abbr[date(now.year, now.month, now.day).weekday()] == 'Mon':
    flag = True
else:
    flag = False
numberOfTheFirstWeek = date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[1] # номер первой учебной недели семестра
if calendar.day_abbr[date(now.year, int(firstDay [0]), int(firstDay [1])).weekday()] == 'Sun':
    numberOfTheWeek += 1
# numberOfTheFirstAutumnWeek = date(now.year, 9, 1).isocalendar()[1]  # номер первой учебной недели осеннего семестра
# if calendar.day_abbr[date(now.year, 9, 1).weekday()] == 'Sun':
#     numberOfTheFirstAutumnWeek += 1
# numberOfTheFirstSpringWeek = date(now.year, 2, 4).isocalendar()[1]  # номер первой учебной недели весеннего семестра
# if calendar.day_abbr[date(now.year, 2, 4).weekday()] == 'Sun':
#     numberOfTheFirstSpringWeek += 1
inputWeek = date(now.year, now.month, now.day).isocalendar()[1]  # номер искомой недели
if (inputWeek - numberOfTheFirstWeek) % 2 == 0:
    week = 'Нечётн'
else:
    week = 'Чётн'
# youDate = input().split() # вводим дату
# year = str(youDate[0])
# month = str(youDate[1])
# day = str(youDate[2])
linksAndNumbers = {} # словарь с сылками и названиями аудиторий
daysDct = {} # словарь с видом дня и parcingDct
try:
    response = urlopen("https://home.mephi.ru/rooms?term_id=10")
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html)
    links = [] # массив всех аудиторий
    for audience in soup.find_all('a', attrs= {'class' : 'btn btn-primary btn-outline'}): # выводит ссылки всех аудиторий, которые есть на странице
        if audience.has_attr('href'):
            links.append(audience.get('href'))
    for j in range(14):
        parcingDct = {}  # словарь с номерами аудиторий и атрибутами
        currentDay = now + timedelta(days=j)
        year = str(currentDay.year)
        month = str(currentDay.month)
        day = str(currentDay.day)
        weekday = calendar.day_abbr[date(int(year), int(month), int(day)).weekday()]
        if flag == True:
            flag = False
        else:
            if weekday == 'Mon':
                if week == 'Чётн':
                    week = 'Нечётн'
                else:
                    week = 'Чётн'
        for i in range(len(links)):
            url = str(links[i])
            newResponse = urlopen('https://home.mephi.ru' + url + '/day?date=' + year + '-' + month + '-' + day)
            newhtml = newResponse.read().decode('utf-8')
            newsoup = BeautifulSoup(newhtml)
            audienceTimeAttributes = []
            audienceTime = []
            audienceAttributes = []
            for lessonTime in newsoup.find_all('div', attrs= {'lesson-time'}):
                audienceTime.append(lessonTime.text)
            for noLesson in newsoup.find_all('div', attrs={'alert alert-info'}): # добавляем в массив аудитории, в которых сегодня нет пар
                audienceAttributes.append('alert alert-info')
            for desktop in newsoup.find_all('i', attrs={'fa fa-desktop'}):  # выводит все аудитории с компьютерами
                audienceAttributes.append('fa fa-desktop')
            for projector in newsoup.find_all('i', attrs={'fa fa-video-camera'}):  # выводит все аудитории с проекторами
                audienceAttributes.append('fa fa-video-camera')
            for unlock in newsoup.find_all('i', attrs={'fa fa-unlock'}):  # выводит все аудитории общего фонда
                audienceAttributes.append('fa fa-unlock')
            for flask in newsoup.find_all('i', attrs={'fa fa-flask'}):  # выводит все аудитории с лабораториями
                audienceAttributes.append('fa fa-flask')
            for title in newsoup.find_all('title'):
                audienceTimeAttributes.append(audienceTime)
                audienceTimeAttributes.append(audienceAttributes)
                parcingDct[title.text[22:-24]] = audienceTimeAttributes
        #print(weekday, week, currentDay)
        daysDct[week + weekday] = parcingDct
    fout = open('D:\Папка\Python\Files for Pycharm\JSON\Reboot1.json', 'w', encoding='utf8')
    json.dump(daysDct, fout, ensure_ascii=False)
    fout.close()
    fileWithFirstDay.close()
except urllib.error.URLError: # проверка на подключение к интернету
    print("Соединение с интернетом разорвано.")