import datetime, os

usuario = os.getlogin()
hora = datetime.datetime.now().strftime("%H:%M:%S")
print(f"Hola {usuario}, la hora actual es {hora}")
