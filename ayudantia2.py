

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

def comunaMasTrabajada(semana):
    horas_dic = dict()
    for maquina in semana:
        comuna = maquina[3]
        horas = maquina[2]
        if comuna in horas_dic:
            #voy a sumar las horas
            horas_dic[comuna] += horas
        else:
            horas_dic[comuna] = horas

    lista = []
    for comunas, horas in horas_dic.items():
        tupla = (comunas,horas)
        lista.append(tupla)

    return lista


print("La cantidad de hora asociadas por maquina son:")
print(horasXmaquina(semana))

print("Resultado problema 2")
print(comunaMasTrabajada(semana))