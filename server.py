from flask import Flask, render_template, request, redirect, url_for, session # type: ignore
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "password"

def get_db():
    conn = sqlite3.connect("tareas.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        # Generar hash seguro de la contraseña
        contrasena = generate_password_hash(request.form["contraseña"])
        conn = get_db()
        try:
            conn.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contrasena))
            conn.commit()
        except:
            return "Usuario existente"
        finally:
            conn.close()
        return redirect(url_for("login"))
    return render_template("registro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena_ingresada = request.form["contraseña"]
        conn = get_db()
        user = conn.execute("SELECT * FROM usuarios WHERE usuario=?", (usuario,)).fetchone()
        conn.close()
        if user and check_password_hash(user["contraseña"], contrasena_ingresada):
            session["usuario"] = usuario
            return redirect(url_for("tareas"))
        else:
            return "Credenciales inválidas"
    return render_template("login.html")

@app.route("/tareas", methods=["GET", "POST"])
def tareas():
    if "usuario" not in session:
        return redirect(url_for("login"))
    conn = get_db()
    if request.method == "POST":
        descripcion = request.form["descripcion"]
        conn.execute("INSERT INTO tareas (usuario, descripcion) VALUES (?, ?)", (session["usuario"], descripcion))
        conn.commit()
    tareas = conn.execute("SELECT descripcion FROM tareas WHERE usuario=?", (session["usuario"],)).fetchall()
    conn.close()
    return render_template("tareas.html", usuario=session["usuario"], tareas=tareas)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
