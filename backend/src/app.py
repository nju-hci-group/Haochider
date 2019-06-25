from flask import Flask, request, jsonify, session, url_for, escape
from flask_cors import *
from peewee import *
import random

from yummyModel import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/hello')
def hello_world():
    return "hello"
@app.route('/customer/orders/get')
def oredr_get():
    orders=[]
    orderLists=[]
    email = ""
    if 'email' in session:
       email = session['email']
    else:
        return jsonify({"res": "PleasLogin"})

    order_s = NewOrder.select().where(NewOrder.uid == email)
    for e in order_s:
        s = NewOrderlist.select().where(NewOrderlist.oid == e.oid)
        for ele in s:
            p = NewMeal.get(ele.mid)
            orderLists.append({"name": p.name, "price": p.price, "num": ele.num})
        r = NewRes.select().where(NewRes.rid == e.tid)
        for es in r:
            rs = es
        if e.stata == 0:
            state = "已完成"
        elif e.stata == 1:
            state = "待送达"
        elif e.stata == 2:
            state = "已取消"
        orders.append(
            {"id": e.oid, "time": e.time, "avatar": rs.photo, "rid": rs.rid,"rname":rs.name, "price": e.cost, "orders": orderLists,
             "state": state, "contents": ''})
        orderLists = []

    return jsonify({'data':orders})

@app.route('/Yummy/api/customer/get',methods=['GET'])
def customer():
    return jsonify({"username":"蔡徐坤"})

@app.route('/Yummy/api/customer/sign-in', methods=['POST'])
def login():
    email = request.args.get('email')
    pew=request.args.get('pwd')
    cust = Customer.get(email)
    session['email']=email
    session['username'] = cust.name
    return jsonify({"result":0})

@app.route('/restaurant/name/get',methods=['GET'])
def rname():
    rid = request.args.get("rid")
    res_data = NewRes.get(rid=rid)
    rname = NewRes.name
    return jsonify({"name":rname})



@app.route('/Yummy/api/restaurant/get',methods=['GET'])
def res():
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


@app.route('/restaurant/categories', methods=['GET'])
def res_c():
    type_data = NewTag.select()
    type_res = []
    for e in type_data:
        type_res.append(e.tagname)
    return jsonify({'code': 1, 'data': type_res})

@app.route('/restaurant', methods=['GET'])
def res_show():
    res_json = []
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
