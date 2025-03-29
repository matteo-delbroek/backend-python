from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Zorg ervoor dat je deze geheim houdt

@app.route("/", methods=["GET", "POST"])
def home():
    if "username" in session:  # Controleer of de gebruiker al is ingelogd
        username = session["username"]
        return f"Je bent ingelogd als {username} <br><a href='/logout'>Uitloggen</a>"
    return redirect(url_for('login'))  # Als niet ingelogd, ga naar de loginpagina

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        session["username"] = username  # Zet de sessie voor ingelogde gebruiker
        return redirect(url_for('home'))  # Verwijder de gebruiker naar de homepagina
    return render_template("login.html")  # Toon login formulier

@app.route("/logout")
def logout():
    session.pop("username", None)  # Verwijder de gebruiker uit de sessie
    return redirect(url_for('home'))  # Redirect naar de homepagina

if __name__ == '__main__':
    app.run(debug=True)
