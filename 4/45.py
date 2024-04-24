
import time

lt = time.localtime()
dateStr = '['+str(lt.tm_year)+'년'+ str(lt.tm_mon)+'월'+ str(lt.tm_mday)+'일] '

today = input('오늘 일정: ')

file = open('C:/pythontxt/test.txt','w')
strCnt = file.write(dateStr + today)
file.close()

# w : 쓰기 전용(덮어쓰기), a: 쓰기전용(덧붙임), x: 쓰기 전용(파일 있으면 에러발생), r: 읽기 전용(파일 없으면 에러발생)