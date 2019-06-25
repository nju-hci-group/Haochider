from flask import Flask, request, jsonify, session, url_for, escape
from flask_cors import *
from peewee import *
import random

from yummyModel import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀

@app.route('/hello')
def hello_world():
    return "hello"


@app.route('/Yummy/api/customer/get',methods=['GET'])
def customer():
    if 'username' in session:
        # return 'Logged in as %s' % escape(session['username'])
        return jsonify({"name": session['username']})
    return "AccessDenied"

@app.route('/Yummy/api//customer/sigh-in', methods=['POST'])
def login():
    email = request.args.get('email')
    pew=request.args.get('pwd')
    cust = Customer.get(email)

    session['username'] = cust.name
    return jsonify({"result":0})





@app.route('/Yummy/api/restaurant/get',methods=['GET'])
def res():
    map_data=[]

    rid=request.args.get("rid")
    res_data = NewRes.get(rid=rid)

    mda=res_data.dc
    if(mda=="免配送费"):
        mda=0
    else:
        print(mda)
        mda=float(mda.split("¥")[1])
    res_json={"name":res_data.name,"priceStart":res_data.mda,"priceDelivery":mda,"avatarSrc":res_data.photo,"address":res_data.area,"decription":res_data.des,"stars":res_data.stars}
    # print(jsonify({'code': 1, 'data': map_data}))
    return jsonify({'code': 1, 'data': res_json})

@app.route('/Yummy/api/restaurant/get/meals',methods=['GET'])
def res_meals():
    map_data=[]
    rid = request.args.get("rid")
    meal_data=NewMeal.select().where(NewMeal.rid==rid)

    res_json =[]
    for ele in meal_data:
        res_json.append({"id":ele.nid,"name":ele.name,"desc":ele.des,"price":ele.price,"type":ele.type,"picSrc":ele.photo})
    return res_json

@app.route('/Yummy/api/restaurant', methods=['GET'])
def res_show():
    res_json = []
    type_data=NewTag.select()
    type_res=[]
    for e in  type_data:
        type_res.append(e.tagname)
    res_json.append(type_res)
    photo_data=[]
    photo_data.append({"https://fuss10.elemecdn.com/7afe0df785fe8e04f009cddf0ff372d5jpeg.jpeg", "E5545917783901406104"})
    photo_data.append({"https://fuss10.elemecdn.com/f88c26b6c61ae96459894e864a56eb30jpeg.jpeg", "E14825464048244892398"})
    photo_data.append({"https://fuss10.elemecdn.com/3b141a39ff987a7bbf99e509723c996ajpeg.jpeg", "E16200833748681328248"})
    photo_data.append({"https://fuss10.elemecdn.com/b77341aca13efd12874b8d406ba29508jpeg.jpeg", "E6387385026588375130"})
    photo_data.append({"https://fuss10.elemecdn.com/c1bd46c09210cc022484a9af0066772cjpeg.jpeg", "E11204101347899364163"})
    photo_data.append({"https://fuss10.elemecdn.com/d5ccc3d3416a616d14ff128e39f3de48jpeg.jpeg", "E4850881976237283649"})
    photo_data.append({"https://fuss10.elemecdn.com/016b2de4ab16fafeac00b678d469866ajpeg.jpeg", "E15056118707731574566"})
    photo_data.append({"https://fuss10.elemecdn.com/6a8432cd40b20dab7b91edf8b0d9a3f1jpeg.jpeg", "E15056118707731574566"})
    res_json.append(photo_data)

    res_data=[]

    page=int(request.args.get("page"))
    pageSize=int(request.args.get("pageSize"))
    limit1 = (page - 1) * pageSize
    limit2 = pageSize
    resa = NewRes.select().limit(limit2).offset(limit1)
    for e in resa:
        res_data.append({e.rid,e.name,e.des,e.area,e.photo,random.choice("123456789")})
    res_json.append(res_data)
    return jsonify({'code': 1, 'data': res_json})
if __name__ == '__main__':
    # http_server = WSGIServer(('',5000),app)
    # http_server.serve_forever()

    app.config["JSON_AS_ASCII"]=False
    app.run()
