import matplotlib.pyplot as plt
import pandas as pd
import random

def calc(ks,vals):
    total=0
    for x in range(len(vals)):
        total+=ks[x]*vals[x]
    return total

def lossMSE(real,predicted):
    return (real-predicted)**2

def changeParams(params,real,mse):
    for x in range(len(params)):
        params[x]=params[x]-(step*real[x]*(mse))
    #print(params)
    return params
    

df=pd.read_csv("2021.csv",index_col=0)
names=list(df.index)
df=df.values.tolist()

# Initialize the step
step=0.001

# Number of times the model goes through training data
epochs=150

# Initialize the parameters (k's) between 0 and 1.
k=[]
for x in range(9):
    k.append(random.randint(0,1000)/1000)

# Normalize the ratings
for index in range(len(df)):
    for col in range(len(df[index])-2):
        df[index][col]=df[index][col]/100
    df[index].insert(0,1)
        
# Normalize the points
for index in range(len(df)):
    df[index][len(df[index])-1]=df[index][len(df[index])-1]/114

print(df)

history=[]
for x in range(epochs):
    temp=[]
    for team in df:
        ypred = calc(k,team[:9])
        loss = lossMSE(team[len(team)-1],ypred)
        temp.append(loss)
        k=changeParams(k,team,loss)
        #print(loss)

    cost=0
    for x in temp:
        cost+=loss
    cost=cost/len(temp)
    history.append(cost)
    #print(cost)

    #if(cost<0.0001):
    #    break


data=pd.read_csv("2022.csv",index_col=0)
nms=list(data.index)
data=data.values.tolist()

i=0
every=[]
for team in data:
    team.insert(0,1)
    pred=calc(k,team[:9])
    every.append((nms[i],pred))
    i+=1
    #print(pred)
    #print(team[len(team)-1])

every.sort(key=lambda tup: tup[1])
print(every)
print(k)

i=0
preds=[]
for team in df:
    pred=calc(k,team[:9])*114
    real=team[len(team)-1]*114
    preds.append((names[i],pred,real,((real-pred)/pred)*100))
    i+=1

#print(preds)

plt.plot(history)
plt.ylabel('Cost')
plt.xlabel('Epoch')
plt.show()


