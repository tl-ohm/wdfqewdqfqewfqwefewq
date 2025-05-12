
from flask import Flask, render_template, redirect, url_for, request, jsonify, abort
import requests

app = Flask(__name__, template_folder="client/templates", static_folder="client/static")

maintenance_mode = False

def check_maintenance():
    if maintenance_mode:
        return 'olyium is 100% down rn. (jokeing ts is still up)'
    return None

@app.route('/', methods=['POST', 'GET'])
def LandingPage():

    maintenance_message = check_maintenance()
    
    if maintenance_message:
        return maintenance_message

    if request.method == "POST":
        return 'fuck you'
    
    return render_template('landingpage.html', image=url_for('static', filename='images/image.png'))

@app.route('/ansi', methods=['POST', 'GET'])
def ansi():

    maintenance_message = check_maintenance()
    
    if maintenance_message:
        return maintenance_message

    if request.method == "POST":
        return 'fuck you'
    
    return render_template('ansi.html')

@app.route('/email', methods=['POST', 'GET'])
def email():

    maintenance_message = check_maintenance()
    
    if maintenance_message:
        return maintenance_message

    if request.method == "POST":
        
        DATA = {
            'content': f"""Requester: {request.form.get('email')}\nWants: {request.form.get('suc')}\nWants To Pay: {request.form.get('bid')}"""
        }
        DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1371613773986529340/sFeR8_iVLvfqmPJCQzV2DfeB4vT_uQPGU3-fXi4g3KoGqB5j1MDFo8jaeR5Gv-KcQf50"
        requests.post(DISCORD_WEBHOOK_URL, data=DATA)
        return render_template("messagepage.html", message="Sent request succesfully. We will get back to you as soon as possible.")
    
    return render_template('email.html')


@app.route('/protected')
def Protected():

    try:

        Referer = request.headers.get("Referer")
    
    except:

        pass

    return f'You have been redirected to olyiums protected network to ensure the stability and uptime of {Referer}'

@app.errorhandler(Exception)
def handle_all_errors(e):
    return redirect(url_for('LandingPage'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 
