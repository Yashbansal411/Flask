from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello_world'
@app.route('/count/')
def count_sub():
    file = open('read.txt','r')
    string = file.read()
    substring = 'ubuntu'
    count = 0
    start = 0
    print(string)
    while start < len(string):
        pos = string.find(substring,start)
        if pos == -1:
            break
        else:
            start = pos +1
            count = count+1

    ans = {
           "sub-string": substring,
           "count": count
           }
    return ans

if __name__ == "__main__":
    app.run(debug = True)
