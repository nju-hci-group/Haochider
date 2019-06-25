from flask import Flask, request, jsonify, session
from flask_cors import *
import random

import time

from yummyModel import *

app = Flask(__name__)
CORS(app, supports_credentials=True)

logins=0



@app.route('/hello')
def hello_world():
    return "hello"
@app.route('/Yummy/api/customer/orders/get')
def oredr_get():
    orders=[]
    orderLists=[]
    email = "161250192@smail.nju.edu.cn"
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
    if logins==0:
        return jsonify({"data":{"AccessDenied":"1"}})
    else:
        return jsonify({"data":{"name":"蔡徐坤"}})

@app.route('/Yummy/api/customer/sign-in', methods=['POST'])
def login():
    global logins
    logins+=1
    return jsonify({"result": 0})

@app.route('/Yummy/api/customer/sign-out', methods=['POST'])
def logout():
    global logins
    logins==0
    return jsonify({"result": 0})


@app.route('/Yummy/api/restaurant/order/post', methods=['POST'])
def orderpost():
    if request.method == 'POST':
        rid = request.data['rid']
        price = request.data['price']
        orders = request.data['orders']
    times=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    p = NewOrder.create(tid=rid, cost=price, stata=0, uid="161250192@smail.nju.edu.cn", time=times)
    for e in orders:
        ol = NewOrderlist.create(mid=e['fid'], num=e['number'], oid=p.oid)
    return jsonify({"result": "success"})


@app.route('/Yummy/api/restaurant/name/get',methods=['GET'])
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
    return jsonify({'data': res_json})


@app.route('/Yummy/api/restaurant/categories', methods=['GET'])
def res_c():
    type_data = NewTag.select()
    type_res = []
    for e in type_data:
        type_res.append({e.tagname})
    return jsonify({'data': type_res})

@app.route('/Yummy/api/restaurant/pictures', methods=['GET'])
def res_p():
    photo_data=[]
    photo_data.append(
        {'url': "https://fuss10.elemecdn.com/8ef12630c266d008a08733effa92070bjpeg.jpeg",
         'rid': "E15104388440383987282"})
    photo_data.append({'url':"https://fuss10.elemecdn.com/7afe0df785fe8e04f009cddf0ff372d5jpeg.jpeg",'rid': "E5545917783901406104"})
    photo_data.append(
        {'url':"https://fuss10.elemecdn.com/f88c26b6c61ae96459894e864a56eb30jpeg.jpeg", 'rid':"E14825464048244892398"})
    photo_data.append(
        {'url':"https://fuss10.elemecdn.com/3b141a39ff987a7bbf99e509723c996ajpeg.jpeg", 'rid':"E16200833748681328248"})
    photo_data.append({'url':"https://fuss10.elemecdn.com/b77341aca13efd12874b8d406ba29508jpeg.jpeg", 'rid':"E6387385026588375130"})
    photo_data.append(
        {'url':"https://fuss10.elemecdn.com/c1bd46c09210cc022484a9af0066772cjpeg.jpeg", 'rid':"E11204101347899364163"})
    photo_data.append({'url':"https://fuss10.elemecdn.com/d5ccc3d3416a616d14ff128e39f3de48jpeg.jpeg", 'rid':"E4850881976237283649"})
    photo_data.append(
        {'url':"https://fuss10.elemecdn.com/016b2de4ab16fafeac00b678d469866ajpeg.jpeg", 'rid':"E15056118707731574566"})
    photo_data.append(
        {'url':"https://fuss10.elemecdn.com/6a8432cd40b20dab7b91edf8b0d9a3f1jpeg.jpeg", 'rid':"E15056118707731574566"})

    return jsonify({'data': photo_data})

@app.route('/Yummy/api/restaurant', methods=['GET'])
def res_show():
    res_data=[]

    page=int(request.args.get("page"))
    pageSize=int(request.args.get("pageSize"))
    limit1 = (page - 1) * pageSize
    limit2 = pageSize
    resa = NewRes.select().limit(limit2).offset(limit1)

    for e in resa:
        if e.photo[-2]=='e':
            photo="https://fuss10.elemecdn.com/"+e.photo+".jpeg"
        else:
            photo = "https://fuss10.elemecdn.com/" + e.photo + ".png"
        res_data.append({"id":e.rid,"name":e.name,"description":e.des,"address":e.area,"type":random.choice("123456789"),"image":e.photo})
    return jsonify({'data': res_data})
if __name__ == '__main__':
    # http_server = WSGIServer(('',5000),app)
    # http_server.serve_forever()
    app.config["JSON_AS_ASCII"]=False
    app.run()
