from tinydb import TinyDB, Query
import hashlib
from bs4 import BeautifulSoup
import requests
import threading
from flask import Flask, request, render_template
import time


def get_product(url):
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",'Cookie': ''}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    product_title = soup.find(id='productTitle').text.replace('\n','')
    price_str = soup.findAll("span","a-size-medium a-color-price")[0].text
    price = ""
    currency = ""
    for i in price_str:
        if i.isdigit() or i==".":
            price += i
        else:
            currency += i
    currency = currency.replace('\n','').replace('\u00a0','').replace(',','')
    id = hashlib.sha256(product_title.encode("utf-8")).hexdigest()
    return {'product_price':price, 'product_title':product_title, 'previous_price':price,'id':id, 'currency':currency, 'url':url}

def check_amazon():
    while True:
        user_db = TinyDB('json/product.json')
        user_product = user_db.all()
        search = Query()
        for a in user_product:
            while True:
                status = True
                try:
                    result = get_product(a['url'])
                except Exception:
                    status = False
                    pass
                if status:
                    break
            current_price = float(a['product_price'])
            new_price = float(result['product_price'])
            if current_price - new_price > 0:
                price_drop = current_price - new_price
                user_db.update({'product_price':str(new_price), 'previous_price':str(current_price)}, search.id == a['id'])
        print("Checking product")
        time.sleep(180)
        
                


app = Flask("Python Amazon Price Tracker") 



@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    user_db = TinyDB('json/product.json')
    products = user_db.all()
    result = {'products':[]}
    for i in products:
        result['products'].append(i)
    return result

@app.route('/add_track', methods=['POST'])
def add_track():
    url = request.get_json()
    user_product = TinyDB("json/product.json")
    while True:
        status = True
        try:
            product = get_product(url['url'])
        except Exception:
            status = False
            pass
        if status:
            break
    product_search = Query()
    find_product = user_product.search(product_search.id == product['id'])
    if find_product == []:
        user_product.insert(product)
        return "Product Saved."
    else:
        return "You've already added this product."


@app.route('/remove_track', methods=['POST'])
def remove_track():
    url = request.get_json()
    user_product = TinyDB("json/product.json")
    product_search = Query()
    user_product.remove(product_search.id == url['id'])
    return "Product Deleted."

threading.Thread(target=check_amazon).start()
app.run(host='0.0.0.0',debug=False, port=10086)