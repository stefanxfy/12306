import requests
r=requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js",verify=False)
#print(r.text)
stationdict={}
stations=r.text.split('@')[1:]
for station in stations:
    stationlist=station.split('|')
    stationdict[stationlist[1]]=stationlist[2]