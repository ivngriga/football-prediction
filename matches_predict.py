import pandas as pd

teams=pd.read_csv("2022.csv",index_col=0)
names=list(teams.index)
teams=teams.values.tolist()



final = []
for home in range(len(teams)):
    for away in range(len(teams)):
        if(names[home]!=names[away]):
            row=[]
            row.append(names[home])
            row.append(names[away])
            for a in teams[home]:
                row.append(a)
                
            for b in teams[away]:
                row.append(b)
            final.append(row)

print(len(final))
        
df=pd.DataFrame(final).to_csv("matches_predict.csv",index=False)
        
