from flask import Flask, render_template, request

app = Flask(__name__, static_folder = './static')

# 기본
@app.route('/')
def index():
    return render_template('index.html')

# 전화번호부에 저장하기 위한 기능
@app.route('/store/', methods=['GET'])
def store():
    # html의 input value로부터 받은 값음 name, tel 에 각각 저장한다.
    name = request.args.get('name')
    tel = request.args.get('tel')

    # 'a'모드로 phonebook.txt에 이름과 전화번호 내용을 덧붙여 나간다.
    file = open('./data/phonebook.txt', 'a')
    data = "%s,%s\n" % (name, tel)
    file.write(data)

    file.close()
    return render_template('index.html', msg='저장되었습니다.')

# 검색하기 위한 기능
@app.route('/search/', methods=['POST'])
def search():
    # html의 input value로부터 받은 값음 findName 저장한다.
    findName = request.form['name']

    file = open('./data/phonebook.txt', 'r')
    # 파일에서 한 line씩 읽으면서 name 과 tel 을 각각 저장한다.
    for aline in file.readlines():
        name = aline.split(',')[0];
        tel = aline.split(',')[1];
        # html에서의 findName과 파일의 name 이 같다면 전화번호를 rendering 해준다.
        if(findName == name):
            file.close()
            return render_template('index.html', msg='검색되었습니다.', name = findName, findTel = tel)

    # 찾지 못했다면, findTel의 값을 "못 찾았습니다"로 return 한다.
    file.close()
    return render_template('index.html', msg='검색되었습니다.', name = findName, findTel = "못 찾았습니다.")

# 전화번호부를 보기 위한 기능
@app.route('/view/', methods=['GET'])
def view():
    dict1 = {}   #rending 할 전화부를 저장한 dictionary

    file = open('./data/phonebook.txt', 'r')
    # 파일에서 한 line씩 읽으면서 name 과 tel 을 각각 저장하고 dict1에 저장한다.
    for aline in file.readlines():
        name = aline.split(',')[0]
        tel =  aline.split(',')[1]

        dict1[name] = tel

    file.close()
    # dict1을 rendering 해준다.
    return render_template('view.html', dict = dict1)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
