
from flask import Flask, render_template, redirect, url_for, request, jsonify, abort

app = Flask(__name__, template_folder="client/templates", static_folder="client/static")

maintenance_mode = False

def check_maintenance():
    if maintenance_mode:
        return 'olyium is down.'
    return None

@app.route('/', methods=['POST', 'GET'])
def LandingPage():

    maintenance_message = check_maintenance()
    
    if maintenance_message:
        return maintenance_message

    if request.method == "POST":
        return 'fuck you'
    
    return render_template('landingpage.html', image=url_for('static', filename='images/image.png'))

@app.errorhandler(Exception)
def handle_all_errors(e):
    return redirect(url_for('LandingPage'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 