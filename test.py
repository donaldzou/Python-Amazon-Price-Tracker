# from tinydb import TinyDB, Query

# set_db = TinyDB("json/setting.json")
# set_search = Query()

# data = {"sleep_time": "10000"}

# for i in data.keys():
#     print(i)
#     print(data[i])
#     set_db.update({'content':data[i]}, set_search.title == i)

# while True:
#     floor = input("Floor: ")
#     if floor.isdigit():
#         floor = int(floor)
#         groundfloor = 0
#         if floor > 10:
#             groundfloor = floor - 1
#             print (groundfloor)
#         else:
#             groundfloor = floor + 1
#             print (groundfloor)
#         print("the elevator will travel to the actual floor", groundfloor)
#         break
#     else:
#         print("This is not a number")

from bs4 import BeautifulSoup
import requests

url = "https://www.amazon.cn/dp/B07PTMKYS7/ref=sr_1_1?keywords=Oculus&qid=1597095824&sr=8-1"

payload = {}
headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        'Cookie': '',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding':'gzip, deflate, br'
}

response = requests.request("GET", url, headers=headers, data = payload)

soup = BeautifulSoup(response.content, "html.parser")
product_title = soup.find(id='productTitle').text.replace('\n','')
medium = soup.findAll("span","a-size-medium a-color-price")
base = soup.findAll("span","a-size-base a-color-price")
try:
        price_str = soup.findAll("span","a-size-medium a-color-price")[0].text
except Exception:
        price_str = soup.findAll("span","a-size-base a-color-price")[0].text

print(price_str)

