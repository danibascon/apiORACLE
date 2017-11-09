from sys import argv
import bottle
from bottle import Bottle,route,run,request,template,static_file,redirect,get,post, default_app, response, get, post
import os
import json
import requests
import commands
import sys
import getpass
import cx_Oracle

@route('/', method="get")
def intro():
	return template('inicio.tpl')



@route('/login',method="post")
def inicio():
  user = request.forms.get('user')
  passwd = request.forms.get('passwd')


  login_user ='usuario'
  login_passwd='asdasd'


  if user != login_user or passwd != login_passwd:
  	return template('error1.tpl')

  else:
  	con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
	cur = con.cursor()
	cur.execute('select * from cat')
	lista=[]
	for x in cur:
		lista.append(x[0])
	return template('tablas.tpl', lista=lista)





@route('/consulta',method="post")
def inicio():
  user ='usuario'
  passwd='asdasd'

  tabla = request.forms.get('tabla').upper()
  con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
  cur = con.cursor()
  cur.execute('select * from cat')
  lista3=[]
  for x in cur:
	lista3.append(x[0])

  con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
  cur = con.cursor()
  cur.execute('select nombre from paises')
  lista = []
  for x in cur:
  	lista.append(x[0])

  if tabla not in lista3:
  	return template('error2.tpl')

  else:
  	con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
	cur = con.cursor()
	cur.execute('select * from '+tabla)
	lista2=[]
	for x in cur:
		a=''
		for y in range(0,len(x)):
			a = a+" "+x[y]
		lista2.append(a)
	return template('join.tpl', lista=lista, lista2=lista2, tabla=tabla)









@route('/join',method="post")
def inicio():
  pais = request.forms.get('pais').title()
  user ='usuario'
  passwd='asdasd'
  con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
  cur = con.cursor()
  lista=[]
  cur.execute('select nombre from paises')

  for x in cur:
  	lista.append(x[0])

  if pais not in lista:
  	return template('error3.tpl')

  else:
  	con = cx_Oracle.connect(user+"/"+passwd+"@//172.22.200.170:1521/orcl")
	cur = con.cursor()
	cur.execute("select nombre, sum(nvl(n_heridos,0) + nvl(n_muertos,0)) as afectados from paises p, historial_c h where p.codigo=h.cod_pais and nombre ='"+pais+"'group by nombre")
	lista2=[]
	for x in cur:
		lista2.append(x)
	return template('final.tpl', pais=pais, lista2=lista2, lista=lista)




@route('/static/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='static')


run(host='0.0.0.0',port=argv[1])
