"""conversiones.py
a Sol peruano: 0.0046
a Peso Argentino: 0.093
a Dólar Americano: 0.0013
['conversiones.py', '0.0046', '0.093', '0.0013', '10000']
"""
from sys import argv
pe = float(argv[1])
arg = float(argv[2])
usd = float(argv[3])
clp = int(argv[4])
cl_pe = pe*clp
cl_arg = arg*clp
cl_usd = usd*clp
print(f"""
      Los {clp} pesos chilenos equivalen a:
      {cl_pe:.1f} Soles
      {cl_arg:.1f} Pesos Argentinos
      {cl_usd:.1f} Dolares
      """)

