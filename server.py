from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder="client/templates", static_folder="client/static")

maintenance_mode = False

def check_maintenance():
    if maintenance_mode:
        return 'olyium is under maintenance.'
    return None

@app.route('/', methods=['POST', 'GET'])
def LandingPage():
    maintenance_message = check_maintenance()
    if maintenance_message:
        return maintenance_message
    return render_template('landingpage.html', image=url_for('static', filename='images/image.png'))

@app.route('/ansi', methods=['POST', 'GET'])
def ansi():
    maintenance_message = check_maintenance()
    if maintenance_message:
        return maintenance_message
    return render_template('ansi.html')

@app.route('/mines', methods=['POST', 'GET'])
def mines():
    maintenance_message = check_maintenance()
    if maintenance_message:
        return maintenance_message
    return render_template('mines.html')

@app.route('/games', methods=['POST', 'GET'])
def games():
    maintenance_message = check_maintenance()
    if maintenance_message:
        return maintenance_message
    return render_template('game_landingpage.html')
    
@app.route('/protected')
def Protected():
    referer = request.headers.get("Referer")
    return f'You have been redirected to Olyium\'s protected network to ensure the stability and uptime of {referer}'

@app.errorhandler(Exception)
def handle_all_errors(e):
    print(f"[ERROR] {e}")
    return "An unexpected error occurred.", 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
