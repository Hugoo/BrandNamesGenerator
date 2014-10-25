# -*- coding: utf-8 -*-
from random import *

#Let's try to create brand names.

#Put here the letters you want to keep.
lc = ['B','C','D','F','G','H','L','M','N','P','S','T','V']
lv = ['A','E','O','I']

#Keep a record of the words we already created
mots = []
while 1!=0:
  for i2 in range(0,10):
    mq=""
    nv = 0
    nc = 0
    pl = int(int(random()*100)*6/100) #place l

    for i in range(0,6):
      #3voyelles et 3 consonnes
      if i == pl:
        mq+="ED"
      else:
        if(((int(int(random()*100)*2/100)==1) and (nc<3)) or nv>3):
          pl = lc[int(int(random()*100)*len(lc)/100)] #next letter
          if(len(mq)>0): #Avoid certain letters combinations
            while((mq[len(mq)-1]=="L" and pl=="R") or (mq[len(mq)-1]=="W" and pl=="Q") or (mq[len(mq)-1]=="H" and pl=="F") or (mq[len(mq)-1]=="F" and pl=="H") or (mq[len(mq)-1]=="H" and pl=="P") or (mq[len(mq)-1]=="E" and pl=="E") or (mq[len(mq)-1]=="H" and pl=="H") or (mq[len(mq)-1]=="P" and pl=="P") or (mq[len(mq)-1]=="L" and pl=="L") or (mq[len(mq)-1]=="I" and pl=="I") or (mq[len(mq)-1]=="N" and pl=="D") or (mq[len(mq)-1]=="H" and pl=="N") or (mq[len(mq)-1]=="V" and pl=="B") or (mq[len(mq)-1]=="Y" and pl=="Y") or (mq[len(mq)-1]=="H" and pl=="V") or (mq[len(mq)-1]=="H" and pl=="W") or (mq[len(mq)-1]=="H" and pl=="T") or (mq[len(mq)-1]=="S" and pl=="W") or (mq[len(mq)-1]=="H" and pl=="S") or (mq[len(mq)-1]=="P" and pl=="N") or (mq[len(mq)-1]=="B" and pl=="B")):
              pl = lc[int(int(random()*100)*len(lc)/100)]
          mq+=pl
          nc+=1
        elif (nv<3):
          mq+=lv[int(int(random()*100)*len(lv)/100)]
          nv+=1
      
    
    if (mq not in mots) and (len(mq)==6):
      mots.append(mq)
      print mq
  raw_input()
