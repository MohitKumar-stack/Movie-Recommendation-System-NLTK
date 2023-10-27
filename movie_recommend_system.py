from flask import Flask,request
import pandas
from flask import render_template
import json

with open('movies_list.json', 'r') as json_file:
        data = json.load(json_file)
with open('similarity.json', 'r') as json_file:
        similarity = json.load(json_file)

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
        output_list=[]
        movie_name = request.form['movie_name']
        movie_index=data.index(movie_name)
        # print(movie_name)
        # print(data.index(movie_name))
        # print(movie_index)
        distance =similarity[movie_index]
        movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
        for i in movie_list:
              output_list.append(data[i[0]])
        return render_template('index.html', output_list=output_list,data=data)
    
    return render_template('index.html', data=data)

     