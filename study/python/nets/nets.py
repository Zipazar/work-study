#D:\Users\Alexandrov\Desktop\py\text.txt
import sys
print(sys.version)
print('Prepare your file with networks. It must look like this:\nFirst string: SiteID\nSecond: PtP\nThird: PKT\nFourth: PKD\nThere may be much nets')
path=str(input('Enter path to your file:'))
filesList=[]
siteIDlist=[]
PtPList=[]
PKT=[]
PKD=[]
userFile=open(path,'r')
if userFile.closed:
	print('Can\'t open this file, check path please')
	path=str(input('Enter path to your file:'))
linesCount=int(0)
n=int(0)
for line in userFile:
	filesList.append(line)
	linesCount+=1
userFile.close()
n=len(filesList)
for i in range(0,n):
	tempStr=str(filesList[i])
	filesList[i]=tempStr.strip('\n')
for i in range(0,n,+4):
	siteIDlist.append(filesList[i])
for i in range(1,n,+4):
	PtPList.append(filesList[i])
for i in range(2,n,+4):
	PKT.append(filesList[i])
for i in range(3,n,+4):
	PKD.append(filesList[i])
a=len(siteIDlist)
for i in range(0,a):
	print('ip route vrf russianpost_Telemat',PtPList[i],'255.255.255.252 GigabitEthernet0/0/3.2025 192.168.110.73 name',siteIDlist[i],
	'\nip route vrf russianpost_Telemat',PKT[i],'255.255.255.224 GigabitEthernet0/0/3.2025 192.168.110.73 name',siteIDlist[i],
	'\nip route vrf russianpost_Telemat',PKD[i],'255.255.255.240 GigabitEthernet0/0/3.2025 192.168.110.73 name',siteIDlist[i])
close=input('Enter any letter to close program')