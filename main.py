from flask import Flask, render_template, request
import smtplib
app = Flask(__name__)
#server = smtplib.SMTP("smtp.gmail.com", 587)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contato', methods=['GET', 'POST'])
def contato():
#    msg = "Nome: " +request.form['name']+ "\nTelefone: "+request.form['phone']+"\nE-mail: "+request.form['email']+"\nMenssagem: "+ request.form['message']
#    server.sendmail("mercadotrevisol@hotmail.com", "lucas.claro.tr@gmail.com", msg)
#    print(request.form['name'])
#    print(request.form['phone'])
#    print(request.form['email'])
#    print(request.form['message'])
    return ""

if __name__ == '__main__':
    app.run(port=80)
#    server.login("mercadotrevisol@hotmail.com", "g033127g")