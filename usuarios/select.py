from soupsieve import select
import usuarios.usuario as modelo
import Notas.next_select as action

class Select:

    def registro(self):

        print("\n Ok!! Vamos a registrarte en el sistema....")
        name = input("Ingresa tu nombre: ")
        lastname = input("Ingresa tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Ingresa tu constraseña: ")
        usuario = modelo.Create_U(name,lastname,email,password)
        registro= usuario.Registrar()

        if registro[0]>=1:
            print(f"\n Se ha registrado {registro[1].name} con el correo {registro[1].email}")
        else:
            print("\n No se ha registrado correctamente")

    
    def login(self):
        print("\n Entiendo, Hay que ingresar... ")
        try:
            email = input("Introduce tu email: ")
            password = input("Ingresa tu constraseña: ")

            usuario = modelo.Create_U('','',email,password)
            login=usuario.Identificar()

            if email==login[3]:
                print(f"\n BIENVENIDO {login[1]}, te has registrado el día {login[5]}")
                self.next_select(login)

        except Exception as e:
            print(type(e).__name__)
            print("Datos incorrectos")
    
    def next_select(self,usuario):
        print("""
                Acciones disponibles:
                    - Crear nota
                    - Mostrar notas
                    - Eliminar notas
                    - Salir
                """)
        select= input("\n¿Que deseas?  ")

        do_=action.Acciones()

        if select== "Crear":
            
            print("Vamos a crear")
            do_.crear(usuario)
            self.next_select(usuario)
        elif select== "Mostrar":
            
            print("Vamos a mostrar")
            do_.mostrar(usuario)
            self.next_select(usuario)
        if select== "Eliminar":
            print("Vamos a Eliminar")
            do_.purge(usuario)
            self.next_select(usuario)
        if select== "Salir":
            print("Good bye ")
            exit()