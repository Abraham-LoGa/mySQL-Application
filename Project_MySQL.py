from usuarios import select

print("""
Acciones disponibles:
    - Registro
    - Login
""")

do=select.Select()
option=input("¿Que quieres hacer? ")

if option=='Registro':
    do.registro()

elif option=='Login':
    do.login()

