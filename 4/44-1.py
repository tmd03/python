


class PasswordLengthShort(Exception):
    def __init__(self, str):
        super().__init__(f'{password}: 길이 5 미만!!')
class PasswordLengthLong(Exception):
    def __init__(self, str):
        super().__init__(f'{password}: 길이 10초과!!')
class PasswordWrong(Exception):
    def __init__(self, str):
        super().__init__(f'{password}: 잘못된 비번!!')

adps = 'admin1234'
password = input('input admin password: ')

try:
    if len(password) < 5:
        raise PasswordLengthShort(password)
    elif len(password) > 10:
        raise PasswordLengthLong(password)
    elif password != adps:
        raise PasswordWrong(password)
    elif password == adps:
        print('빙고!!!')
        
except PasswordLengthShort as e1:
    print(e1)
except PasswordLengthLong as e2:
    print(e2)
except PasswordWrong as e3:
    print(e3)