import json
firstSemesterDay = input().split()
fout = open('D:\Папка\Python\Files for Pycharm\JSON\FirstDay.json', 'w', encoding='utf8')
json.dump(firstSemesterDay, fout, ensure_ascii=False)
fout.close()