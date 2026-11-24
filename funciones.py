import Usuarios_informacion as u_i
import app 
from flask import Flask, request

global userInf
global code
global teacherInf
global inicioInforme
global notasInforme
global horarioInforme

userInf = {}
sesion_activa = False
suma_notas = []
code = []
userE = ""
userT = ""
estudiantes_P = []

#INICIO SESION

def iniciar_sesionE ():
    global userE
    userE = request.form.get("usrnmE")
    pasword = int(request.form.get("psswrdE"))
    global sesion_activa
    global userInf
    global code
    
    if userE in u_i.users_info and pasword == u_i.users_info[userE][1]:
        sesion_activa = True
        userInf = u_i.users_info[userE]
        code = dict(userInf[0])
        return ""
    else:
        sesion_activa = False
        return ""

def iniciar_sesionT ():
    global userT
    userT = request.form.get("usrnmT")
    print(userT)
    pasword = int(request.form.get("psswrdT"))
    global sesion_activaT
    global teacherInf
    
    if userT in u_i.teachers_info and pasword == u_i.teachers_info[userT][0]:
        print(1.2)
        sesion_activaT = True
        teacherInf = u_i.teachers_info[userT]
        print(teacherInf)
        return ""
    else:
        sesion_activaT = False
        return ""

#ANALISIS DATOS 
def promedio ():
    notasUsuario = list(code.values())
    global promedio_notas
    promedio_notas = sum(notasUsuario) / len(notasUsuario)
    return ""

def puesto ():
    global puesto_usuario
    lista_notas = [list(d[0].values()) for d in u_i.users_info.values()]
    lista_promedios = [(sum(d)/len(d)) for d in lista_notas]
    lista_promedios.sort(reverse=True)
    puesto_usuario = lista_promedios.index(promedio_notas)
    puesto_usuario = (puesto_usuario) + 1
    return ""

def tablas_profes ():
    global estudiantes_P
    estudiantes_P = []
    for i in u_i.users_info:
        if u_i.users_info[i][4] in teacherInf[3]:
            estudiantes_P.append([i, u_i.users_info[i]])
    return""

#RECOPILAR INFORMACION

def cantidad_maxima():
    global max_inicio
    global max_notas
    global max_horario
    cantidad_inicio = [(d[0]) for d in u_i.usersAcData.values()]
    cantidad_notas = [(d[1]) for d in u_i.usersAcData.values()]
    cantidad_horario = [(d[2]) for d in u_i.usersAcData.values()]
    max_horario = max(cantidad_horario)
    max_notas = max(cantidad_notas)
    max_inicio = max(cantidad_inicio)
    return""

