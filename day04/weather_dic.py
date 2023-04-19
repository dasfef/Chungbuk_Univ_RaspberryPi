import urllib.request
import json
from time import localtime, strftime
import datetime

dic = {"T1H" : "Temperature", "RN1" : "Rainfall", "UUU" : "Wind E-W",
       "VVV" : "Wind S-N", "REH" : "Humidity", "PTY" : "Precipitation type",
       "VEC" : "Wind direction", "WSD" : "Wind Speed"}

url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"
serviceKey = "ServiceKey=" + "74c5ZdkDfPARwepbwip9XOy3B2OYJkUBxj12RhzlgPLU34nfU9FiPmprQPybkilNGZS10zlDq1jRt9PG6HH0uQ%3D%3D"
numOfRow = "&numOfRows=1000"
pageNo = "&pageNo=1"
dataType = "&dataType=JSON"

current = datetime.datetime.now()
base_date = "&base_date=" + current.strftime("%Y%m%d")
if localtime().tm_min > 30:
    base_time = "&base_time=" + current.strftime("%H00")
else :
    current = current - datetime.timedelta(hours = 1)
    base_time = "&base_time=" + current.strftime("%H00")
    
nx = "&nx=69"
ny = "&ny=107"

queryParams = "?" + serviceKey + numOfRow + pageNo + dataType + base_date + base_time + nx + ny
response = urllib.request.urlopen(url+queryParams).read().decode('utf8')
# print (response)

weather = json.loads(response)
totalCount = weather["response"]["body"]["totalCount"]
print(base_time)
# for k in range(totalCount) :
#     category = weather["response"]["body"]["items"]["item"][k]["category"]
#     obsrValue = weather["response"]["body"]["items"]["item"][k]["obsrValue"]
#     print(category, " : ", obsrValue)

for k in weather["response"]["body"]["items"]["item"]:
    print(dic[k["category"]], " : " , k["obsrValue"])


