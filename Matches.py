import pandas as pd

teams=pd.read_csv("2021.csv",index_col=0)
names=list(teams.index)
teams=teams.drop(['League Position','Points'], axis=1).values.tolist()

matches=pd.read_csv("matches.csv").values.tolist()



final = []

for match in matches:
    row=[]
    hometeam=match[0]
    awayteam=match[1]
    for x in range(len(names)):
        if(hometeam==names[x]):
            for a in teams[x]:
                row.append(a)
            break
        
    for x in range(len(names)):
        if(awayteam==names[x]):
            for a in teams[x]:
                row.append(a)
            break
        
    row.append(match[3])
    if(len(row)==17):
        final.append(row)
        
df=pd.DataFrame(final).to_csv("matches_final.csv",index=False)
        
