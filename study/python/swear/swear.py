import random
import os

maleNoun=[]
maleAdjective=[]
femaleNoun=[]
femaleAdjective=[]
neutralNoun=[]
neutralAdjective=[]
print(os.path.realpath(__file__))

maleNf=open(os.path.realpath(__file__).replace('swear.py','maleNou.txt'),'r')
for line in maleNf:
	maleNoun.append(line.replace('\n',''))
maleNf.close()
maleAf=open(os.path.realpath(__file__).replace('swear.py','maleAdj.txt'),'r')
for line in maleAf:
	maleAdjective.append(line.replace('\n',''))
maleAf.close()

femaleNf=open(os.path.realpath(__file__).replace('swear.py','femaleNou.txt'),'r')
for line in femaleNf:
	femaleNoun.append(line.replace('\n',''))
femaleNf.close()
femaleAf=open(os.path.realpath(__file__).replace('swear.py','femaleAdj.txt'),'r')
for line in femaleAf:
	femaleAdjective.append(line.replace('\n',''))
femaleAf.close()

neutralNf=open(os.path.realpath(__file__).replace('swear.py','neutralNou.txt'),'r')
for line in neutralNf:
	neutralNoun.append(line.replace('\n',''))
neutralNf.close()
neutralAf=open(os.path.realpath(__file__).replace('swear.py','neutralAdj.txt'),'r')
for line in neutralAf:
	neutralAdjective.append(line.replace('\n',''))
neutralAf.close()

def manSwear():
	print(random.choice(maleNoun),random.choice(maleAdjective))
def womenSwear():
	print(random.choice(femaleNoun),random.choice(femaleAdjective))
def uniSwear():
	print(random.choice(neutralNoun),random.choice(neutralAdjective))

choice=int(input('Кого надо послать?(введи цифру)\n1)Мужика\n2)Бабу\n3)Универсально\nТвой выбор: '))
if choice==1:
	manSwear()
elif choice==2:
	womenSwear()
elif choice==3:
	uniSwear()
else:
	print('Ты еблан? Иди нахуй')
	a=input('пресс эни кей чтобы пойти нахуй')