# Python Amazon Price Tracker
This is a Python Flask App that could track the price of Amazon products! It could work with any Amazon site (.cn, .jp, .com...). Frontend is powered by jQuery and Bootstrap. When there is a price drop, there will be **Desktop Notification** and also **On website notification**.

**Tracking**

![Example Image](https://github.com/donaldzou/Python-Amazon-Price-Tracker/raw/master/templates/example.png)

**Price Dropped Notification**

![Notification Image](https://github.com/donaldzou/Python-Amazon-Price-Tracker/raw/master/templates/notification.png)

# Dependencies
- **Python**
  - TinyDB
  - Flask
  - Beautiful Soup 4
- **Front End**
  - jQuery
  - Bootstrap
  - Push.js
# Install & Run
1. Clone this git
2. Run ```python3 -m pip install -r requirements.txt```
3. After finishing install dependencies, run ```python3 tracker_server.py```
4. Accese the server with ```http://127.0.0.1:10086```
5. Happy tracking!
