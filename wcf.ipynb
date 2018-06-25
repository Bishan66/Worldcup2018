import pandas as pd
import numpy as np
from collections import OrderedDict


f=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/result18.csv',',',)
f
v=pd.read_csv('C:/Users/ASUS/Desktop/upgrad/2018wc/index18.csv',',')
h=np.array(v)
Point={}
#dic={"Brazil":2,"England":3,"Portugal":4,"France":1,"Iran":4,"Sweden":4,"Denmark":7,"Australia":4,"Russia":4,"Paraguay":4,"Colombia":4}
list1=["Egypt","Spain","Belgium","Brazil","England","Portugal","France","Iran","Sweden","Denmark","Australia","Russia","Colombia","Morocco","Mexico","Uruguay","Germany","SaudiArabia","Morocco","Peru","Croatia","Nigeria","Iceland","Argentina","Switzerland","Serbia","CostaRica","SouthKorea","Tunisia","Panama","Japan","Senegal","Poland"]
groupingsasTeam1 = f.groupby(['Team1']) [['Team1Goals','Team2Goals']].sum()
#print(groupingsasTeam1)
groupingsasTeam2 = f.groupby(['Team2']) [['Team1Goals','Team2Goals']].sum() 
#print(groupingsasTeam2)  
for item in list1:
    play=f[f.Team2==item]+f[f.Team1==item]
    print("number of play matchs of",item,len(play))
    draw=f[f.Winner==item]+f[f.Losser==item]
    
    d=len(play)-len(draw)
    print("number of draw matchs of",item,d)
    win=f[f.Winner==item]
    dm=0
    print("number of Win matchs of",item,len(win))
    los=f[f.Losser==item]
    p=1
    print("number of losses matchs of",item,len(los))
    i1=item 
    hoo=f[f.Winner==f.Losser]
    ho1=hoo[hoo.Team1==item]
    ho=hoo[hoo.Team2==item]
    listofdraw=list(ho.Team1)+list(ho1.Team2)
    print(listofdraw)
    
   # Point[i1]= round((len(win)*6+y*2)/len(play),2 )
    goalsgiven=groupingsasTeam1.Team1Goals[groupingsasTeam1.index==item] + groupingsasTeam2.Team2Goals[groupingsasTeam2.index==item]
    print(goalsgiven.dtypes)
  #  goalsgiven=goalsgiven.astype('int')
#    print(goalsgiven.dtypes)
 #   print(goalsgiven+4)
    goalsagainst=groupingsasTeam1.Team2Goals[groupingsasTeam1.index==item] + groupingsasTeam2.Team1Goals[groupingsasTeam2.index==item]
    goaldiff=goalsgiven-goalsagainst
    print("number of goaldiff of",goaldiff)
    l=list(win.Losser)
    lost=list(los.Winner)
    gd=goaldiff.item()
    lp=0
    u=t=y=0
    for i in range(0,len(l)):
        for j in range(0,206):
                     
              if (l[i]==(h[j][1])):
                  p=p+(h[j][2])
                  
              
                  
                  
                 
    for i in range(0,len(listofdraw)):
        for j in range(0,206):
                     
             if (listofdraw[i]==(h[j][1])):
                 dm=dm+h[j][2]
                 
    for i in range(0,len(lost)):
        for j in range(0,206):
                     
             if (lost[i]==(h[j][1])):
                 lp=lp+1.5-(h[j][2])
                 
                 print(h[j][1])
   
    Point[i1]= round(((dm*2+p*6-lp+(gd/10))/len(play)),2 )
    
    
#print(Point)
Point_new = OrderedDict(sorted(Point.items(), key=lambda x: x[1]))
print(Point_new)


 

    
    


