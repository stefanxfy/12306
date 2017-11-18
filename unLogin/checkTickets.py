import requests
import json
import stations
from_station=""
to_station=""
train_date="2017-11-26"
def deal(from_station,to_station):
    f_s=stations.stationdict[from_station]
    t_s=stations.stationdict[to_station]
    return f_s,t_s  #返回元组
t=deal("西安","九江")
from_station=t[0]
to_station=t[1]
url="https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT"%(train_date,from_station,to_station)
r1=requests.get(url,verify=False)
result=json.loads(r1.text)

for ticket in result["data"]["result"]:
    i = 0
    tlist=str.split(ticket,'|')
    for t in tlist:
       # print(i,t)
        i+=1
    print('''车次%s,出发时间%s,到达时间%s,历时%s,
            商务座特等座%s,一等座%s,二等座%s,
            高级软卧%s,软卧%s,硬卧%s,硬座%s,无座%s'''%(tlist[3],tlist[8],tlist[9],tlist[10],tlist[32],tlist[31],tlist[30],tlist[21],tlist[23],tlist[26],tlist[28],tlist[29]))