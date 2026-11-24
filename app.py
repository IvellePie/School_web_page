from flask import Flask, redirect, url_for, request, render_template
import funciones
import Usuarios_informacion as u_i

#INICIAR SESION
app = Flask(__name__)
@app.route('/loginEstudiantes', methods=['GET', 'POST'])
def incr_scn():
        if request.method == 'POST':
            funciones.iniciar_sesionE() 
            if funciones.sesion_activa == False:
              return(redirect(url_for("incr_scn")))
            else:
                return redirect(url_for('inicio', nomYApe = f"{funciones.userInf[2]}{funciones.userInf[3]}"))
        else:
            return render_template('login_estudiantes.html')

@app.route('/loginProfesores', methods=['GET', 'POST'])
def incr_scn1():
        if request.method == 'POST':
            funciones.iniciar_sesionT() 
            print(1)
            if funciones.sesion_activaT == False:
                return(redirect(url_for("incr_scn1")))
            else:
                return redirect(url_for('editar_notas', nomYApe = f"{funciones.teacherInf[1]}{funciones.teacherInf[2]}"))
        else:
            return render_template('login_profesores.html')

#MODULOS ESTUDIANTES

@app.route('/inicio/<nomYApe>', methods = ['GET', 'POST'])
def inicio(nomYApe):
    if funciones.userE == "":
        return redirect(url_for('incr_scn'))
    else:
        print(u_i.usersAcData)
        u_i.usersAcData[funciones.userE][0] = u_i.usersAcData[funciones.userE][0] + 1
        return render_template('Inicio.html', userInf = funciones.userInf)

@app.route('/InformacionAcademica/<nomYApe>')
def ver_notas(nomYApe):
    if funciones.userE == "":
        return redirect(url_for('incr_scn'))
    else:
        print(u_i.usersAcData)
        analisisDatos = False
        u_i.usersAcData[funciones.userE][1] = u_i.usersAcData[funciones.userE][1] + 1
        funciones.promedio()
        funciones.puesto()
        analisisDatos = True
        if analisisDatos == True:
            print(funciones.code)
            return render_template('verNotas.html', userInf = funciones.userInf, promedio = funciones.promedio_notas, puesto = funciones.puesto_usuario, code = funciones.code)

@app.route('/HorarioEscolar/<nomYApe>')
def ver_horario(nomYApe):
    if funciones.userE == "":
        return redirect(url_for('incr_scn'))
    else:
        print(u_i.usersAcData)
        u_i.usersAcData[funciones.userE][2] = u_i.usersAcData[funciones.userE][2] + 1
        matriz_horarios = funciones.userInf[5]
        horario_1 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[0]])
        horario_2 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[1]])
        horario_3 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[2]])
        horario_4 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[3]])
        horario_5 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[4]])
        horario_6 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[5]])
        horario_7 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[6]])
        horario_8 = "".join([f"<td class = 'td'>{materia}</td>" for materia in matriz_horarios[7]])
        return render_template('verHorario.html', userInf = funciones.userInf, horario_1 = horario_1, horario_2 = horario_2, horario_3 = horario_3,  horario_4 =  horario_4,horario_5 = horario_5, horario_6 = horario_6,horario_7 = horario_7, horario_8 = horario_8) 

#MODULOS PROFESORES

@app.route('/EdicionInfoAca/<nomYApe>', methods=['GET', 'POST'])
def editar_notas(nomYApe):
    if funciones.userT == "":
        return redirect(url_for('incr_scn1'))
    else:
        if request.method == 'POST':
            data = request.form
            print(data)
            for clave, valor in data.items():
                if clave.startswith('nota_'):
                    partes = clave.split('_')
                    materia = partes[1].capitalize()
                    estudianteUsuario = partes[2]
                    notaNueva = valor
                    if estudianteUsuario in u_i.users_info:
                        u_i.users_info[estudianteUsuario][0][materia] = float(notaNueva)
            print(list(u_i.users_info.values())[0])
            return redirect(url_for('editar_notas', nomYApe=nomYApe))
        else:
            funciones.tablas_profes()    
            return render_template('Edicion_infoAca.html', teacherInf = funciones.teacherInf, estudiantes_P = funciones.estudiantes_P)
        
@app.route('/analisisDatos')
def ver_analisis():
    if funciones.userT == "":
        return redirect(url_for('incr_scn1'))
    else:
            funciones.cantidad_maxima()
            return render_template('analisisData.html', inicio = funciones.max_inicio,horario = funciones.max_horario, notas = funciones.max_notas)


if __name__ == '__main__':
    app.run(debug=True)
