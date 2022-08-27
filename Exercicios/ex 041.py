from time import sleep
ano = int(input('Em que ano você nasceu?'))
print('\033[1;31;40mPROCESSANDO SUA CATEGORIA....\033[m')
#sleep(3)
num = 2022 - ano
print(num)
if num <= 9:
    print('MIRIM')
elif num > 9 and num <= 14:
    print('INFANTIL')
elif num > 14 and num <= 19:
    print('JUNIOR')
elif num > 19 and num <= 25:
    print('SÊNIOR')
elif num > 25:
    print('MASTER')
