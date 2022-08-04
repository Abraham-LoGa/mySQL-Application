
import datetime
import hashlib
import usuarios.connection as conexion

connect=conexion.do_connection()
database = connect[0]
cursor = connect[1]
class Create_U:
    
    def __init__(self,name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def Registrar(self):
        fecha=datetime.datetime.now()
        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuarios=(self.name, self.lastname, self.email, cifrado.hexdigest(),fecha)

        try:
            cursor.execute(sql, usuarios)
            database.commit()
            result = [cursor.rowcount,self]

        except:
            result = [0,self] 
        return result

    def Identificar(self):
        sql="SELECT * FROM usuarios WHERE email= %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        usuario = (self.email,cifrado.hexdigest())

        cursor.execute(sql,usuario)
        result = cursor.fetchone()
        return result