from bs4 import BeautifulSoup
import requests
import numpy as np

clubs=["lazio","atalanta","generic-capitale"]

print(np.var([2,3,4,5]))

file=open("final.txt","w+")


for club in clubs:
    url="https://www.futhead.com/21/clubs/"+club+"/"
    
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    players = soup.find_all("div", class_="playercard fut21 card-small nif gold")+soup.find_all("div", class_="playercard fut21 card-small nif silver")+soup.find_all("div", class_="playercard fut21 card-small nif bronze")
    
    if(players==[]):
        print("Bad Link: "+club)
    else:   
        print("Good Link: "+club)
    
        hgk=0
        hdef=0
        hmid=0
        hatt=0
        mdef=0
        mmid=0
        matt=0
        mteam=0

        d=[]
        m=[]
        a=[]
        gk=[]
        
        for player in players:
            position=player.find("div", class_="playercard-position").get_text().replace(" ","").replace("\n","")
            rating=int(player.find("div", class_="playercard-rating").get_text())

            defenders=["RB","LB","CB","LWB","RWB"]
            midfielders=["CDM","CM","LM", "RM","CAM"]
            attackers=["LW","LF","CF","ST","RW","RF"]
            
            if(position in defenders):
                d.append(rating)
                if(rating>hdef):
                    hdef=rating
            elif(position in midfielders):
                m.append(rating)
                if(rating>hmid):
                    hmid=rating
            elif(position in attackers):
                a.append(rating)
                if(rating>hatt):
                    hatt=rating
            else:
                gk.append(rating)
                if(rating>hgk):
                    hgk=rating

        #All players array
        p=np.array(gk+d+m+a)

        #Calculate interquartile range 
        q3, q1 = np.percentile(p, [75 ,25])
        iqr = q3 - q1

        #Calculate lower bound
        lb=q1-iqr

        tkaway=0
        for x in d:
            if(x<lb):
                tkaway+=1
                pass
            else:
                mdef+=x
        mdef=mdef/(len(d)-tkaway)

        tkaway=0
        for x in m:
            if(x<lb):
                tkaway+=1
                pass
            else:
                #print(x)
                mmid+=x
        mmid=mmid/(len(m)-tkaway)

        tkaway=0
        for x in a:
            if(x<lb):
                tkaway+=1
                
                pass
            else:
                matt+=x
        matt=matt/(len(a)-tkaway)

        tkaway=0
        pcut=[]
        for x in p:
            if(x<lb):
                tkaway+=1
                pass
            else:
                pcut.append(x)
                mteam+=x
        mteam=mteam/(len(p)-tkaway)

        variance=np.var(pcut)

        string=str((hatt,hmid,hdef,hgk,mdef,mmid,matt, mteam)).replace("(","").replace(")","")
        string=string[:len(string)-2]+"\n"
        file.write(string)

    #playercard  fut22 card-small  nif  gold

file.close()
