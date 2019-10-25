from datetime import datetime

dates=['01 Mar 2017','03 Feb 2017','15 Jan 1998']


print(sorted(dates,key=lambda date: datetime.strptime(date, '%d %b %Y')))
map={}
ls=[]
for i in dates:
    map[(datetime.strptime(i, '%d %b %Y'))]=i
print([v for k,v in sorted(map.items(),key=lambda x:x[0])])

