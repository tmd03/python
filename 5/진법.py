dNum = int(input('input num: '))

# bin = #b / oct = #o / hex = #x -> format(n, '#b')

print(f'2진수: {format(dNum, '#b')}')
print(f'8진수: {oct(dNum)}')
print(f'16진수: {hex(dNum)}')

print(f'2진수 -> 10진수({int(format(dNum, '#b'), 2)})')
print(f'8진수 -> 10진수({int(oct(dNum), 8)})')
print(f'16진수 -> 10진수({int(hex(dNum), 16)})')
