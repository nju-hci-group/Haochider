from flask import Flask, request, jsonify
from flask_cors import *
from peewee import *
from yummyModel import *
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


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
    res_json= {
            "name":res_data.name,
            "priceStart":res_data.mda,
            "priceDelivery":mda,
            "avatarSrc":res_data.photo,
            "address":res_data.area,
            "decription":res_data.des,
            "stars":res_data.stars
    }
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


    return jsonify({'code': 1, 'data': res_json})
if __name__ == '__main__':
    # http_server = WSGIServer(('',5000),app)
    # http_server.serve_forever()
    app.config["JSON_AS_ASCII"]=False
    app.run()
