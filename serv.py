# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template

app = Flask(__name__)

def read_file(fname): #читаем из файла
    o = open(fname,'r', encoding = "utf-8")
    data_pers = list(o)
    o.close()
    return data_pers

def clean_textn (text):
			if not isinstance(text, str):
				raise TypeError('Это не текст')
			for i in ['\n']:
				text = text.replace(i,'')
			return text

@app.route('/', methods=['GET'])
def index():
    base = read_file("base.txt")
    baseout = []
    userout = []
    for s in base:
        stlst = s.split(",")
        namef = stlst[0]
        hostname = stlst[1]
        onwork = stlst[2]
        onwork = clean_textn(onwork)
        if onwork == "0":
                text = "ОТСУТСТВУЕТ."
        else:
                text = "НА РАБОТЕ."
        cur_str = namef+" ******** IP компьютера: "+hostname+" Сейчас "+text
        baseout.append(cur_str)
        userout.append(namef)
    return render_template('index.html', title='Список работников.', baseout=baseout, userout=userout)

@app.route('/<command>', methods=['GET'])
def command(command):
    base = read_file("base.txt")
    fname = command.lower()+".txt"
    fout = []
    fout_revers = []
    for s in base:
        s = s.lower()
        if command in s:
            fdata = read_file(fname)
            for d in fdata:
                fout.append(d)
            fnum = len(fout)-1
            while fnum != 0:
                fout_revers.append(fout[fnum])
                fnum = fnum-1
            fout_revers.append(fout[0])
            out = render_template('onewoker.html', title=command, user=command, statout=fout_revers)
            break
        else:
            out = render_template('onewoker.html', title='Нет работника.')

    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3309, debug=True)