import sys
import math
alkoPercent=float(input('Введите крепость напитка: '))
alkoMass=int(input('Введите количество выпитого в милилитрах: '))*0.8
doverie=int(input('Насколько Амбарова доверяет себе по 9-ти бальной шкале: '))
A=(alkoMass*0.85)*(alkoPercent/100) #Масса спирта
c=A/(65*0.6) #Формула Видмарка для расчета концентрации алкоголя в крови
doverie=doverie/(c*10) #Изменение доверия
nedoeb=[0,]
for i in range(1,10,+1): #Вычисляем реальное значение степени недоеба
	nedoeb.insert(i,math.exp((math.log(i)/2)))
for i in range(10):
	chance=math.sqrt(nedoeb[i])*(c*10)*2-(doverie*100)
	print('При недоебе равном',i,'шанс перепихона',chance,'%')