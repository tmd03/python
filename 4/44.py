def sendSMS(msg):

    if len(msg) > 10:
        raise Exception('길이 초과!!!!', 1)

    else:
        print('sms 발송')


def sendMMS(msg):

    if len(msg) <= 10:
        raise Exception('길이 미달!!!', 2)
    else:
        print('mms 발송')

msg = input('input message: ')

try:
    sendSMS(msg)

except Exception as e :
    print(f'e: {e.args[0]}')
    print(f'e: {e.args[1]}')

    if e.args[1] == 1:
        sendMMS(msg)
    elif e.args[1] == 2:
        sendSMS(msg)
    else:
        print('다시써')
