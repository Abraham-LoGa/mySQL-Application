from colorama import Cursor
import Notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f" {usuario[1]} Vamos a crear una nueva nota")

        titulo = input("Introduce el titulo de la nota: ")
        description = input("Mete el contenido de tu nota: ")
        
        nota = modelo.Nota(usuario[0],titulo,description)
        guardar = nota.guardar()
        if guardar[0]>=1:
            print(f"\n Se ha guardado {nota.titulo}")
        else:
            print(f"\n No se ha guardado la nota correctamente {usuario[1]}")
    
    def mostrar(self,usuario):
        print(f"\n{usuario[1]} enseguida se muestran tus notas: ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        for nota in notas:
            print("\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print(nota[2])
            print(nota[3])
            print(nota[4])
            print("")
    
    def purge(self, usuario):
        print(f"\n{usuario[1]} vamos a borrar notas: ")

        title= input("Introduce el titulo de la nota: ")

        nota=modelo.Nota(usuario[0], title)
        delete=nota.delete()
        if delete[0]>=1:
            print(f"\n Se ha borrado la nota: {nota.titulo}")
        else:
            print(f"\n No se ha borrado la nota correctamente {usuario[1]}")

    
        