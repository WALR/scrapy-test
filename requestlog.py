# -*- encoding: utf-8 -*-
import requests
from pyquery import PyQuery
payload = {
    'uid': 'wlemusr',
    'passwd': 'W@lr6074500'
}

with requests.Session() as s:
  print "Ingresando, espera..."
  p = s.post('https://apps.umg.edu.gt/signup/', data=payload)
  # p = s.post('https://github.com/login', data=payload)
  # print the html returned or something more intelligent to see if it's a successful login page.
  # print p.text

  datanota = {
    'c': '1',
    'y': '2016'
  }

  print "Obteniendo Notas, espera...."
  n = s.post('https://apps.umg.edu.gt/notas?v-n', data=datanota)

  q = PyQuery(n.text)

  cusosList = []
  cn = []

  # for el in q('#marks tbody tr').items('td'):
  #   # print el.text()
  #   if n <= 5:
  #     cn += [el.text()]
  #     n = n + 1
  #   else:
  #     cusosList += [cn]
  #     n = 1
  #     cn = []
  #     cn += [el.text()]
  #     n = n + 1

  for el in q('#marks tbody').items('tr'):
    for el2 in q(el).items('td'):
        cn += [el2.text()]
    cusosList += [cn]
    cn = []


  
  # print "CURSOS: %s" %cusosList
  for cur in cusosList:
    print "Curso: %s \nP#1: %s pts. \nP#2: %s pts. \nAct.: %s pts. \nFinal: %s pts. \nNota: %s pts. \n\n" %(cur[0], cur[1], cur[2], cur[3], cur[4], cur[5])
    




        


    # if "LEGISLACION LABORAL Y MERCANTIL" in n.text:
    #   print "fuck yeahhhhhh"
    # else:
    #   print "OHHHhh NOOOOO"

    # response = s.get('https://apps.umg.edu.gt/')

    # q = PyQuery(response.text)

    # print q

    # nombre = q('a[href="https://apps.umg.edu.gt/settings"]').text()
    # nombre = q('#user-information')
    # tablas = q.items('table')

    # print tablas

    # print nombre

    # An authorised request.
    # print response.text
    # if "Ver Notas" in response.text:
    #   print '->>>>>>>>>>>>> YEAHHHHHHHHHHHHHHHHHHHHHHHH'
    # else:
    #   print '-->>>>>>>>>>>>> NOOOOOOOOOO :('
    # r = s.get('https://github.com/WALR')
    # print r.text
        # etc...