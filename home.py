from flask import Flask,send_from_directory,request,jsonify
from utils import food,calories,fat,mineral,vitamin,deficiency
import requests
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#HOME PAGE
@app.route('/',methods=['GET'])
def home_page():
    return send_from_directory("static/","index.html")

#GETS THE DATA OF A PARTICULAR FOOD
@app.route('/food',methods=["GET"])
def get_food():
    data = request.args.get('name')
    data = food.get_food(data)
    data_dict = [{'ID':dat[0],'name':dat[1],'serving_size':dat[2],'calories':dat[3]} for dat in data]
    return jsonify(data_dict),200

#PUTS THE DATA OF A PARTICULAR FOOD
@app.route('/food',methods=["POST"])
def put_food():
    data = request.get_json()
    required_fields = ['name',"serving_size","calories"]
    if not all(key in data for key in required_fields):
        response = {"message":"PLEASE PROVIDE ALL THE REQUIRED FIELDS"}
        return jsonify(response),400
    success = food.put_food(data)
    if success:
        response = {'message':"Data entered with id {}".format(success)}
        return jsonify(response),201

#GETS THE FOOD ITEMS WITH A + OR -2 RANGE OF THE GIVEN CALORIES
@app.route('/calories',methods=["GET"])
def get_calories():
    data = request.args.get('calories')
    if not data:
        response = "Please enter valid data"
        return jsonify(response),400
    val = calories.get_calories(data)
    val_dict = [{'id':va[0],'name':va[1],'serving_size':va[2],'calories':va[3]} for va in val]
    return jsonify(val_dict),200

#GET TOP 50 FOODS WITH THE LOWEST TOTAL FAT
@app.route('/low-fat',methods=["GET"])
def get_low_fat():
    val = fat.get_low_fat()
    val_dict = [{'id':va[0],'name':va[1],'serving_size':va[2],'calories':va[3],'total_fat':va[5]} for va in val]
    return jsonify(val_dict),200

#GET THE FAT DATA OF A PARTICULAR FOOD
@app.route('/food-fat',methods=["GET"])
def get_food_fat():
    data = request.args.get('name')
    val = fat.get_food_fat(data)
    val_dict = [{"name":va[2],"total_fat":va[0],"saturated_fat":va[1]} for va in val]
    return jsonify(val_dict),200

#GET THE MINERAL DATA OF A GIVEN FOOD
@app.route('/mineral',methods=["GET"])
def get_minerals():
    data = request.get_json()
    val = mineral.get_minerals(data)
    val_list = list(val[0])
    val_dict = {k:v for (k,v) in zip(data["fields"],val_list)}
    return jsonify(val_dict),200

#GET THE VITAMIN DATA OF A GIVEN FOOD
@app.route('/vitamin',methods=["GET"])
def get_vitamins():
    data = request.get_json()
    val = vitamin.get_vitamins(data)
    val_list = list(val[0])
    val_dict = {k:v for (k,v) in zip(data["fields"],val_list)}
    return jsonify(val_dict),200

#TELLS IF A PARTICULAR FOOD IS HEALTHY OR NOT BASED ON THE AMOUNT OF FAT AND CALORIES
@app.route('/healthy',methods=["GET"])
def is_healthy():
    response = []
    data = request.args.get("name")
    try:
        url1 = "http://{}/food?name={}".format("localhost:3000",data)
        url2 = "http://{}/food-fat?name={}".format("localhost:3000",data)
        val1 = requests.get(url1)
        val2 = requests.get(url2)
        val1_dict = val1.json()
        val2_dict = val2.json()
        for x,y in zip(val1_dict,val2_dict):
            if y["saturated_fat"] == '':
                y["saturated_fat"]=0.0
            if (float(x["calories"])*0.03) > (float(y["total_fat"])-float(y["saturated_fat"])):
                response.append({'name':x["name"],"healthy":True,"calories":x["calories"],"total_fat":y["total_fat"]})
            else:
                response.append({'name':x["name"],"healthy":False,"calories":x["calories"],"total_fat":y["total_fat"]})
        return jsonify(response),200
    except requests.exceptions.ConnectionError:
        response = {"messsage":"Connection error"}
        return jsonify(response),500

#GETS 50 FOODS THAT ARE RICH IN WATER CONTENT
@app.route('/water',methods=["GET"])
def get_water():
    val = mineral.get_water()
    val = [{"name":va[0],"water":va[1]} for va in val]
    return jsonify(val),200

#GET VITAMIN FOR GIVEN DEFICIENY
@app.route('/deficiency',methods=["GET"])
def get_remedy():
    name = request.args.get("name")
    remedy = deficiency.get_remedy(name)
    ptr = remedy[1]
    data=remedy[0]
    if ptr == 0:
        val = [{"name":dat[0],"protein":dat[1]} for dat in data]
        return jsonify(val),200
    if ptr == 1:
        val = [{"name":dat[0],remedy[2]:dat[1]} for dat in data]
        return jsonify(val),200



#START THE SERVER
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)