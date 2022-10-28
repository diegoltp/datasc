recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#1.- 2 de Febrero de 2021 a las 6 de la mañana para Empezar el Año.
recordatorios.insert(1,["2021-02-02","06:00","Empezar el año"])

#2.- ya que el 15 de Julio no es feriado. Editar de tal manera que sea el 16 de Julio.
recordatorios[3][0]="2021-07-16"

#3.- Elimine el evento del día del trabajo.
recordatorios.pop(2)

#4.- Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas a las 22 hrs.
recordatorios.insert(4, ['2021-12-24', '22:00', 'Cena de Navidad'])
recordatorios.insert(6, ['2021-12-31', '22:00', 'Cena de Año Nuevo'])

# Output
print(recordatorios)

"""
[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
['2021-02-02', '06:00', 'Empezar el año'],
['2021-07-16', '13:00', 'No hacer nada es feriado'],
['2021-09-18', '16:00', 'Ramadas'],
['2021-12-24', '22:00', 'Cena de Navidad'],
['2021-12-25', '00:00', 'Navidad'],
['2021-12-31', '22:00', 'Cena de Año Nuevo']]
"""
