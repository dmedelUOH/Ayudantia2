

semana = [('YF5519', 'Viernes', 10, 'Providencia'),('YF5519', 'Martes', 15, 'Las Condes'),('BZXC19', 'Lunes', 10, 'Providencia'),('BZXC19', 'Miercoles', 10, 'Vitacura'),('HNMP01', 'Miercoles', 10, 'Vitacura'),('HNMP01', 'Jueves', 10, 'Las Condes'),('YF5519', 'Lunes', 10, 'Providencia'),('YF5519', 'Lunes', 10, 'Providencia')]

def horasXmaquina(semana):
    horas_dic = dict()
    for maquina in semana:
        if maquina[0] in horas_dic:
            #voy a sumar las horas
            horas_dic[maquina[0]] += maquina[2]
        else:
            horas_dic[maquina[0]] = maquina[2]
    return horas_dic

cantidad_horas = horasXmaquina(semana)

print(cantidad_horas)