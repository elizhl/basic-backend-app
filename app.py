from flask import Flask, url_for
from flask import request, render_template
from markupsafe import escape
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('view.html')

@app.route('/health', methods=['POST'])
def health_check():
	return {"success": True}

@app.route('/save-ticket', methods=['POST'])
def save_config():
    info = request.form

    folio = str(uuid.uuid4()).split("-")[0]

    with open('/etc/toggles.json') as f:
        d = json.load(f)

        kv_value = d.get('toggles', {}).get('toggle_1', False)

    version = kv_value

    if not version:
        return {
            'success': True, 
            'name': info.get('name', ""), 
            'folio': folio,
            'email': False
        }
    
    else:

        data = {'email': info.get('email', "")}

        r = requests.post('http://172.20.20.22:8000/send-notification', data=data)

        return {
            'success': True, 
            'name': info.get('name', ""), 
            'folio': folio,
            'email': True
        }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
