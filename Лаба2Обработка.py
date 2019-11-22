import json
from datetime import datetime, time, date
import calendar

def is_time_between(begin_time, end_time, check_time):  # функция проверят, попадает ли введённое время в диапазон
    if check_time >= begin_time and check_time <= end_time:
        return False
    else:
        return True

now = datetime.now() # текущая дата
youDate = input().split() # вводим дату
nowTime = input().split() # вводим время
attributes = input().split() # вводим атрибуты аудитории (комп, проектор, фонд, лабаратория)
year = str(youDate[0])
month = str(youDate[1])
day = str(youDate[2])
audienceTime = []  # массив аудиторий, подходящих по времени
audienceDesktop = []  # аудитории с компьютерами
audienceCamera = []  # аудитории с проекторами
audienceUnlock = []  # аудитории общего фонда
audienceFlask = []  # аудитории с лабораториями
BigArray = []  # массив массивов
suitableAudiences = [] # массив с подходящими аудиториями
week = ''
fileWithFirstDay = open('D:\Папка\Python\Files for Pycharm\JSON\FirstDay.json', 'r', encoding='utf8') # файл с датой первого учебного дня в семестре
firstDay = json.loads(fileWithFirstDay.read())
weekday = calendar.day_abbr[date(int(year), int(month), int(day)).weekday()] # день недели
numberOfTheFirstWeek = date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[1] # номер первой учебной недели семестра
#if calendar.day_abbr[date(now.year, int(firstDay [0]), int(firstDay [1])).weekday()] == 'Sun':
# kek = date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[0]
# print(kek)
if date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[0] == 'Sun':
    numberOfTheWeek += 1
# numberOfTheFirstAutumnWeek = date(now.year, 9, 1).isocalendar()[1] # номер первой учебной недели осеннего семестра
# if calendar.day_abbr[date(now.year, 9, 1).weekday()] == 'Sun':
#     numberOfTheFirstAutumnWeek += 1
# numberOfTheFirstSpringWeek = date(now.year, 2, 4).isocalendar()[1] # номер первой учебной недели весеннего семестра
# if calendar.day_abbr[date(now.year, 2, 4).weekday()] == 'Sun':
#     numberOfTheFirstSpringWeekWeek += 1
inputWeek = date(int(year), int(month), int(day)).isocalendar()[1] # номер искомой недели
if (inputWeek - numberOfTheFirstWeek) % 2 == 0:
    week = 'Нечётн'
else:
    week = 'Чётн'
fin = open('D:\Папка\Python\Files for Pycharm\JSON\Reboot.json', 'r', encoding='utf8')
dct = json.loads(fin.read())
#print(dct)
desiredDay = dct[week+weekday]
# print(week+weekday, desiredDay)
for audience in desiredDay:
    numberOfLessons = 0  # количество пар
    goodlessons = 0  # количество пар, в которые не попало время
    for lessonTime in desiredDay[audience][0]:
        numberOfLessons += 1
        hourStart = lessonTime[:2]
        minuteStart = lessonTime[3:5]
        hourFinish = lessonTime[8:10]
        minuteFinish = lessonTime[11:13]
        # print(hourStart)
        # print(minuteStart)
        # print(hourFinish)
        # print(minuteFinish)
        if is_time_between(time(int(hourStart), int(minuteStart)), time(int(hourFinish), int(minuteFinish)), time(int(nowTime[0]), int(nowTime[1]))) == True:
            goodlessons += 1
    if numberOfLessons == goodlessons:
        audienceTime.append(audience)
    # if 'alert alert-info' in desiredDay[audience][1]:
    #     audienceTime.append(audience)
    if 'fa fa-desktop' in desiredDay[audience][1]:
        audienceDesktop.append(audience)
    if 'fa fa-video-camera' in desiredDay[audience][1]:
        audienceCamera.append(audience)
    if 'fa fa-unlock' in desiredDay[audience][1]:
        audienceUnlock.append(audience)
    if 'fa fa-flask' in desiredDay[audience][1]:
        audienceFlask.append(audience)
BigArray.append(audienceTime)
if int(attributes[0]) == 1:
    BigArray.append(audienceDesktop)
if int(attributes[1]) == 1:
    BigArray.append(audienceCamera)
if int(attributes[2]) == 1:
    BigArray.append(audienceUnlock)
if int(attributes[3]) == 1:
    BigArray.append(audienceFlask)
for auditor in BigArray[0]:
    good = 1
    for i in range(1, len(BigArray)):
        if auditor in BigArray[i]:
            good *= 1
        else:
            good *= 0
    if good == 1:
        suitableAudiences.append(auditor)
if len(suitableAudiences) == 0:
    print('Аудиторий не найдено')
for aud in suitableAudiences:
    print(aud)
# print(numberOfTheFirstAutumnWeek)
# print(numberOfTheFirstSpringWeek)
# print(inputWeek)
# print(week)
# print(audienceTime)
# print(audienceDesktop)
# print(audienceCamera)
# print(audienceUnlock)
# print(audienceFlask)
# print(BigArray)
# print(suitableAudiences)
fin.close()
fileWithFirstDay.close()