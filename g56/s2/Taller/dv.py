serie_dv = [2,3,4,5,6,7]
rut = input("Ingrese su rut sin puntos ni digito verificador:\n>")
rut = list(rut)
rut.reverse()
dv = ""
#Igualar el largo de ambas listas
#------------------------------------------
equilibrio = 0
while len(rut) > len(serie_dv):
    if equilibrio > len(serie_dv)-1:
        equilibrio = 0
    serie_dv.append(serie_dv[equilibrio])
    equilibrio+=1
#-------------------------------------------
suma=0
for i in range(len(rut)):
    suma = int(rut[i]) * serie_dv[i] + suma
mod11 = 11 - (suma % 11)
if mod11 == 10:
    dv = "K"
elif mod11 == 11:
    dv = "0"
else:
    dv = mod11
print(f"Su dígito verificador es {dv}")
    


