from flask import Flask, render_template, request, redirect, url_for, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32) 

@app.route('/', methods=['GET', 'POST'])
def home():
    naam = session.get("naam", "")   
    
    if request.method == "POST":
        naam = request.form.get("naam")
        session["naam"] = naam 
        return redirect(url_for("home"))  

    return render_template('index.html', naam=naam)

@app.route("/logout")
def logout():
    session.clear()  
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
