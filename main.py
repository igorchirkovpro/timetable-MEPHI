import PyQt5
import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
from PyQt5 import QtWidgets, QtGui,QtCore,uic
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import MainWindow  # Это наш конвертированный файл дизайна
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime, time, date, timedelta
import urllib
import calendar
import json


class MainWindowApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    flags = [1,1,0,0] # 1 - проектор 0 - компьютерный класс 3 - лабаратория 2 - общий фонд
    result = ""

    year = ""
    month = ""
    day = ""

    hour = ""
    minute = ""

    isEvenWeek = True

    def __init__(self,parent = None):
        super().__init__()
        self.setupUi(self)

        fmt = self.calendarWidget.headerTextFormat()

        fmt.setBackground(QtGui.QColor('#c7f7ea'))
        self.calendarWidget.setHeaderTextFormat(fmt)

        self.checkBox.stateChanged.connect(self.checkFlags)
        self.checkBox_2.stateChanged.connect(self.checkFlags)
        self.checkBox_3.stateChanged.connect(self.checkFlags)
        self.checkBox_4.stateChanged.connect(self.checkFlags)

        self.timeEdit.setDateTime(QtCore.QDateTime.currentDateTime()) #ставим на часах текущее время

        self.date_time_button.clicked.connect(self.currDateTime)
        self.StartButton.clicked.connect(self.setResult)

        self.update_button.clicked.connect(self.setSecondWindow)
        self.back_button.clicked.connect(self.setFirstWindow)
        self.start_upload_button.clicked.connect(self.pre_upload)


    def pre_upload(self):
        firstSemesterDay = [" "]*2
        date = self.dateEdit.date()
        now = datetime.now()
        if QtCore.QDate(now.year,8,25) < date < QtCore.QDate(now.year, 9 ,25) or QtCore.QDate(now.year,1,25) < date < QtCore.QDate(now.year, 2 ,25):
            Date = date.toString("MM dd")
            firstSemesterDay[0] = Date[:2]
            firstSemesterDay[1] = Date[3:5]
            fout = open('JSON\FirstDay.json', 'w', encoding='utf8')
            json.dump(firstSemesterDay, fout, ensure_ascii=False)
            fout.close()
            #self.textBrowser_2.setText("Обновление...")
            self.upload()
            print("!")
        else:
            self.textBrowser_2.setText("Введенная вами дата не может быть началом семестра.")



    def setFirstWindow(self):
        self.setMinimumSize(560,585)
        self.setMaximumSize(560,585)
        self.stackedWidget.setCurrentIndex(1)
    def setSecondWindow(self):
        self.stackedWidget.setCurrentIndex(0)
        self.setMinimumSize(560,320)
        self.setMaximumSize(560,320)
        fileWithFirstDay = open('JSON\FirstDay.json', 'r', encoding='utf8') # файл с датой первого учебного дня в семестре
        firstDay = json.loads(fileWithFirstDay.read())
        fileWithFirstDay.close()
        now = datetime.now()
        self.dateEdit.setDate(QtCore.QDate(now.year, int(firstDay[0]),int(firstDay[1])))
        self.textBrowser_2.setText("Введите дату начала первой (нечетной) недели текущего семестра, эта информация "
                                   "требуется для правильной настройки расписания.\n" 
                                    'После этого нажмите кнопку "Начать обновление"')


    #---------Laba2Peerezagruzka.py------
    def upload(self):


        week = ''
        dctWeek = {1 : 'Mon',2 : 'Tue', 3 : 'Wed', 4 :'Thu',5 : 'Fri', 6 : 'Sat', 7 :'Sun'}
        fileWithFirstDay = open('JSON\FirstDay.json', 'r', encoding='utf8') # файл с датой первого учебного дня в семестре
        firstDay = json.loads(fileWithFirstDay.read())
        now = datetime.now() # текущая дата
        if date(now.year, now.month, now.day).isocalendar()[2] == 1:
            flag = True
        else:
            flag = False
        numberOfTheFirstWeek = date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[1] # номер первой учебной недели семестра
        if date(now.year, int(firstDay [0]), int(firstDay [1])).isocalendar()[2] == 7:
            numberOfTheFirstWeek += 1

        inputWeek = date(now.year, now.month, now.day).isocalendar()[1]  # номер искомой недели
        if (inputWeek - numberOfTheFirstWeek) % 2 == 0:
            week = 'Нечётн'
        else:
            week = 'Чётн'

        #linksAndNumbers = {} # словарь с сылками и названиями аудиторий
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
                text = "Обновление: " + str(j+1) + "/14"
                self.textBrowser_2.setText(text)

                parcingDct = {}  # словарь с номерами аудиторий и атрибутами
                currentDay = now + timedelta(days=j)
                year = str(currentDay.year)
                month = str(currentDay.month)
                day = str(currentDay.day)
                weekday = dctWeek[date(int(year), int(month), int(day)).isocalendar()[2]]
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
                    newResponse = urlopen('https://home.mephi.ru' + url + '/day?date=' + self.year + '-' + self.month + '-' + self.day)
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
            fout = open('JSON\Reboot.json', 'w', encoding='utf8')
            json.dump(daysDct, fout, ensure_ascii=False)
            fout.close()
            fileWithFirstDay.close()
        except urllib.error.URLError: # проверка на подключение к интернету
            self.textBrowser_2.setText("Соединение с интернетом разорванно, повторите процедуру обновления.")
            self.disconnectMessage()
    #-----------------------------
    #---------Laba2Obrabotka.py-----------
    def processing(self):
        audienceTime = []  # массив аудиторий, подходящих по времени
        audienceDesktop = []  # аудитории с компьютерами
        audienceCamera = []  # аудитории с проекторами
        audienceUnlock = []  # аудитории общего фонда
        audienceFlask = []  # аудитории с лабораториями
        BigArray = []  # массив массивов
        suitableAudiences = [] # массив с подхлдящими аудиториями

        week = ''
        fileWithFirstDay = open('JSON\FirstDay.json', 'r', encoding='utf8') # файл с датой первого учебного дня в семестре
        firstDay = json.loads(fileWithFirstDay.read())
        dctWeek = {1 : 'Mon',2 : 'Tue', 3 : 'Wed', 4 :'Thu',5 : 'Fri', 6 : 'Sat', 7 :'Sun'}
        weekday = dctWeek[date(int(self.year), int(self.month), int(self.day)).isocalendar()[2] ]# день недели

        numberOfTheFirstWeek = date(int(self.year), int(firstDay [0]), int(firstDay [1])).isocalendar()[1] # номер первой учебной недели семестра
        if date(int(self.year), int(firstDay [0]), int(firstDay [1])).isocalendar()[2] == 7 :
            numberOfTheFirstWeek += 1
        inputWeek = date(int(self.year), int(self.month), int(self.day)).isocalendar()[1] # номер искомой недели
        if (inputWeek - numberOfTheFirstWeek) % 2 == 0:
            week = 'Нечётн'
            self.result += " (Расписание нечетной недели):\n\n"
        else:
            week = 'Чётн'
            self.result += " (Расписание четной недели):\n\n"
        fin = open('JSON\Reboot.json', 'r', encoding='utf8')
        dct = json.loads(fin.read())

        desiredDay = dct[week+weekday]

        for audience in desiredDay:
            numberOfLessons = 0  # количество пар
            goodlessons = 0  # количество пар, в которые не попало время
            for lessonTime in desiredDay[audience][0]:
                numberOfLessons += 1
                hourStart = lessonTime[:2]
                minuteStart = lessonTime[3:5]
                hourFinish = lessonTime[8:10]
                minuteFinish = lessonTime[11:13]

                if (time(int(self.hour), int(self.minute)) >= time(int(hourStart), int(minuteStart)) and (time(int(self.hour), int(self.minute)) <= time(int(hourFinish), int(minuteFinish))) ) == False:
                    goodlessons += 1
            if numberOfLessons == goodlessons:
                audienceTime.append(audience)

            if 'fa fa-desktop' in desiredDay[audience][1]:
                audienceDesktop.append(audience)
            if 'fa fa-video-camera' in desiredDay[audience][1]:
                audienceCamera.append(audience)
            if 'fa fa-unlock' in desiredDay[audience][1]:
                audienceUnlock.append(audience)
            if 'fa fa-flask' in desiredDay[audience][1]:
                audienceFlask.append(audience)
        BigArray.append(audienceTime)

        if self.flags[0] == 1:
            BigArray.append(audienceDesktop)
        if self.flags[1] == 1:
            BigArray.append(audienceCamera)
        if self.flags[2] == 1:
            BigArray.append(audienceUnlock)
        if self.flags[3] == 1:
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
            self.result += 'Аудиторий не найдено\n'
        for aud in suitableAudiences:
            self.result += aud
            self.result += "\n"
        self.result +="\n"

        fin.close()
        fileWithFirstDay.close()

    #------------------------------------

    def setResult(self):
        self.reciveDateTime()
        self.processing()
        self.textBrowser.setText(self.result)



    def currDateTime(self):
        self.timeEdit.setTime(QtCore.QTime.currentTime())
        self.calendarWidget.setSelectedDate(QtCore.QDate.currentDate())

    def reciveDateTime(self):
        Date = ""
        Time = ""

        date = self.calendarWidget.selectedDate()
        Date += date.toString("yyyy MM dd")

        time = self.timeEdit.time()
        Time += time.toString("HH mm")

        self.year = Date[:4]
        self.month = Date[5:7]
        self.day = Date[8:10]

        self.hour = Time[:2]
        self.minute = Time[3:6]

        self.result +=self.day + "." + self.month + "." + self.year + " в " + self.hour + ":" + self.minute


    def checkFlags(self):
        chk = self.sender()
        if chk == self.checkBox: # 3 -лабаратория
            self.flags[3] ^= 1
        elif chk == self.checkBox_2:
            self.flags[2] ^= 1 # 2 - общий фонд
        elif chk == self.checkBox_3:
            self.flags[1] ^= 1 # 1 - проектор
        else:
            self.flags[0] ^= 1 #0 - комп. класс

    def disconnectMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.NoIcon)
        msg.setWindowTitle("Ошибка")
        msg.setText("Проверьте подключение к интернету")
        okButton = msg.addButton('OK', QtWidgets.QMessageBox.AcceptRole)
        msg.exec()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    main = MainWindowApp()  # Создаём объект класса MainWindowApp
    main.show()  # Показываем окно
    sys.exit(app.exec_()) # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
