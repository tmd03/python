def cmToMm(cm) :
    result = cm * 10

    return result

length = float(input('길이(cm) 입력: '))
returnValue = cmToMm(length)
print(f'returnValue: {returnValue}mm')


#==========================

totalvisit = 0

def counttotalvisit():
    global totalvisit

    totalvisit = totalvisit + 1
    print(f'누적 방문객: {totalvisit}')

counttotalvisit()
counttotalvisit()
counttotalvisit()
counttotalvisit()
counttotalvisit()