from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.aphp.fr'  # Serveur de messagerie
app.config['MAIL_PORT'] = 25  # Port du serveur de messagerie
app.config['MAIL_USE_TLS'] = False  # Utiliser TLS pour la connexion sécurisée
app.config['MAIL_USERNAME'] = 'your-email@example.com'  # Votre adresse e-mail
app.config['MAIL_PASSWORD'] = ''  # Votre mot de passe e-mail

mail = Mail(app)

@app.route('/')
def index():
    return render_template('formulaire.html')

@app.route('/envoyer_email', methods=['POST'])
def envoyer_email():
    destinataire = request.form['destinataire']
    message = request.form['message']
    piece_jointe = request.files['piece_jointe']

    msg = Message('Sujet de l\'e-mail', sender='your-email@example.com', recipients=[destinataire])
    msg.body = message

    if piece_jointe:
        msg.attach(piece_jointe.filename, piece_jointe.mimetype, piece_jointe.read())

    mail.send(msg)

    return 'E-mail envoyé avec succès !'

if __name__ == '__main__':
    app.run()
