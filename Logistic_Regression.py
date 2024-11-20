import matplotlib.pyplot as plt
import pandas as pd
import random
import math

def sigmoid(x):
    return 1/(1+math.exp(-x))

def calc(ks,vals, debug):
    total=0
    
    for x in range(len(vals)):
        total+=ks[x]*vals[x]
        if(debug==True):
            print(ks[x],vals[x])
            #print(total)

    #if(debug==True):
    #    print(total, sigmoid(total))
    #    print(vals)
    #    print(ks)
    return sigmoid(total)

def loss(real,predicted):
    if(int(real)==1):
       return -math.log(predicted)
    else:
        return -math.log(1-predicted)

def changeParams(params,real,loss):
    for x in range(len(params)):
        params[x]=params[x]-(step*real[x]*loss)
        
    return params

df=pd.read_csv("matches_final.csv",header=None)
names=list(df.index)
print(df)
df=df.values.tolist()
new=[]

# Normalize the ratings
for index in range(len(df)):
    for col in range(len(df[index])-1):
        df[index][col]=df[index][col]/100
    df[index].insert(0,1)

for game in df:
    if(game[15]!=0.5):
        #print(game)
        new.append(game)

old=df
df=new


# Initialize the step
step=0.02

# Number of times the model goes through training data
epochs=100

# Initialize the parameters (k's) between 0 and 1.
k=[]
for x in range(17):
    k.append(random.randint(0,1000)/1000)

history=[]
for x in range(epochs):
    temp=[]
    for team in df:
        ypred = calc(k,team[:len(team)-1], False)
        l = loss(team[len(team)-1],ypred)
        temp.append(l)
        k=changeParams(k,team,ypred-team[len(team)-1])

    cost=0
    for x in temp:
        cost+=x
    cost=cost/len(temp)
    history.append(cost)

tot=0
for team in old:
    q=calc(k,team[:len(team)-2],False)
    if(q<=0.55 and q>0.45):
        q=0.5
    else:
        q=float(round(q))
    w=team[len(team)-1]
    if(q==w):
        #if(q==0.5):
        #    print(q)
        tot+=1



print(str(tot)+"/"+str(len(old))+", "+str((tot/(len(old)))*100)+"%")

#plt.plot(history)
#plt.ylabel('Cost')
#plt.xlabel('Epoch')
#plt.show()




data=pd.read_csv("matches_predict.csv")
league=[]
homes=list(data['0'])
aways=list(data['1'])
for x in homes:
    if([x,0] not in league):
        league.append([x,0])
print(league)
data=data.values.tolist()

# Normalize the ratings
for index in range(len(data)):
    for col in range(2,len(data[index])):
        data[index][col]=data[index][col]/100
    data[index].insert(2,1)

i=0


def addVal(arr,name,val):
    for x in arr:
        if(x[0]==name):
            x[1]+=val
    return arr

for match in data:
    #print(match)
    pred=calc(k,match[2:len(match)], False)
    #print(match[0],match[1], pred)

    if(q<=0.55 and q>0.45):
        league=addVal(league,match[0],1)
        addVal(league,match[1],1)
    elif(q==1):
        league=addVal(league,match[0],3)
    else:
        league=addVal(league,match[1],3)
    
    i+=1

print(league)

#every.sort(key=lambda tup: tup[1])
#print(every)
#print(k)

"""

"""
