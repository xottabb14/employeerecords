# -*- coding: utf-8 -*-
import subprocess as sp
import time
import subprocess
import os

base_file = "base.txt"
i = 0
first_in = 0
cur_path = os.path.dirname(os.path.abspath(__file__));

def startcmd(cmd):
	PIPE = subprocess.PIPE
	p = subprocess.Popen(cmd, shell = True)
	p.poll();

def clean_textn (text):
			if not isinstance(text, str):
				raise TypeError('Это не текст')
			for i in ['\n']:
				text = text.replace(i,'')
			return text

def nowtime(now_time): #строка с текущим временем
    t_timet = time.ctime(now_time) #текущее время в нормальном виде
    hmn_time = time.strptime(t_timet) #текущее время в строке
    str_hn = time.strftime("%H",hmn_time) #текущие часы в строке
    str_mn = time.strftime("%M", hmn_time) #текущие минут в строке
    str_yn = time.strftime("%Y",hmn_time)
    str_mmn = time.strftime("%m",hmn_time)
    str_dn = time.strftime("%d",hmn_time)
    str_hmn = str_hn+':'+str_mn+'  '+str_dn+'.'+str_mmn+'.'+str_yn #строка для вывода текущего времени
    return str_hmn

def write_flist(text,namef): #запись в файл
    fname = namef+'.txt'
    o = open(fname,'a', encoding = "utf-8")
    o.write(text)
    o.close()

def write_base(namef,onwork): #перезапись флажка onwork в базе
    o = open(base_file,'r', encoding = "utf-8")
    base_all = list(o)
    o.close()
    s_n = 0
    for w in base_all:
        if namef in w:
            break
        else:
            s_n+=1
    str_new = clean_textn (base_all[s_n])
    str_new = str_new[:-1]+onwork
    str_new = str_new+"\n"
    bb = ""
    if s_n == 0:
        o = open(base_file,'w+', encoding = "utf-8")
        base_new = base_all[1:len(base_all)]
        for b in base_new:
            str_new = str_new+b
        o.write(str_new)
        o.close()
    elif s_n == (len(base_all)-1):
        o = open(base_file,'w+', encoding = "utf-8")
        base_new = base_all[0:(len(base_all)-1)]
        for b in base_new:
            bb = bb+b
        str_new = bb+str_new
        o.write(str_new)
        o.close()
    else:
        o = open(base_file,'w+', encoding = "utf-8")
        base_aftbef = base_all[0:s_n]
        for b in base_aftbef:
            bb = bb+b
        str_new = bb+str_new
        bb = ""
        base_aftbef = base_all[(s_n+1):len(base_all)]
        for b in base_aftbef:
            bb = bb+b
        str_new = str_new+bb
        o.write(str_new)
        o.close()

def read_flist(str_num): #читаем из базы указанную строку
    o = open(base_file,'r', encoding = "utf-8")
    str_pers = list(o)[str_num]
    o.close()
    return str_pers

def pers_test(hostname,namef,onwork,dtm):
    response,result = sp.getstatusoutput("ping " + hostname)
    if 'TTL' in result:
        str_onwork = ' --- На работе ---\n'
        onwork_cur = "1"
    else:
         str_onwork = ' --- КОМПЬЮТЕР ВЫКЛЮЧЕН!\n'
         onwork_cur = "0"
    if onwork != onwork_cur:
        write_base(namef,onwork_cur)
        text = dtm+str_onwork
        write_flist(text,namef)
    else:
        pass
    print (dtm," ",hostname," ",namef," ",onwork,str_onwork)

startcmd("python serv.py")

while True:
    o = open(base_file,'r', encoding = "utf-8")
    num_pers = len(list(o))
    o.close()
    while i!= num_pers:
        res_per = read_flist(i)
        res_per = clean_textn (res_per)
        res_per = res_per.split(",")
        namef = res_per[0]
        hostname = res_per[1]
        onwork = res_per[2]
        now_time = time.time()#текущее время в сек
        dtm = nowtime(now_time)
        if first_in == 0:
            write_flist("___Включение учета___\n",namef)
            if onwork == "0":
                text = dtm+" --- КОМПЬЮТЕР ВЫКЛЮЧЕН!\n"
                write_flist(text,namef)
            else:
                text = dtm+" --- На работе ---\n"
                write_flist(text,namef)
        else:
            pass
        pers_test(hostname,namef,onwork,dtm)
        i+=1
    time.sleep(5)
    i = 0
    first_in = 1