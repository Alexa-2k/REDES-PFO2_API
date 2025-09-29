import requests # type: ignore

BASE_URL = "http://127.0.0.1:5000"

# ejemplo: registro
r = requests.post(BASE_URL + "/registro", data={"usuario": "test", "contraseña": "1234"})
print("Registro:", r.text)

# ejemplo: login
r = requests.post(BASE_URL + "/login", data={"usuario": "test", "contraseña": "1234"})
print("Login:", r.text)

# ejemplo: tareas
r = requests.get(BASE_URL + "/tareas")
print("Tareas:", r.text)