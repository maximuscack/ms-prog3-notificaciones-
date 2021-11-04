# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 01:42:46 2021

@author: juanc
"""

# save this as app.py salvado
from flask import Flask
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/email")
def enviarCorreo():
    destino = request.args.get("correo_destino")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    
    message = Mail(
    from_email='juan.1701718236@ucaldas.edu.co',
    to_emails=destino,
    subject=asunto,
    html_content=mensaje)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "OK"
    except Exception as e:
        print(e.message)
        return "KO"
        

if __name__ == '__main__':
    app.run()