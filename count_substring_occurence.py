from flask import Flask,request
from flask_restful import Api,Resource
from pathlib import Path
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'
@app.route('/count/',methods=["GET","POST"])
def count_sub():
    substring = request.args.get('substring')
    req_data = request.get_json()
    path = req_data['path']
    file = open(Path(path), 'r')
    string = file.read()
    #substring = 'ubuntu'
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring,start)
        if pos == -1:
            break
        else:
            start = pos+1
            count = count+1

    ans = {
           "sub-string": substring,
           "count": count
           }
    return ans
#app.add_url_rule('/count/','count')
#app.view_functions['count']=count_sub
if __name__ == "__main__":
    app.run(port=8080,debug = True)
