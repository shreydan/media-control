from flask import Flask, jsonify, render_template, request
from controller import control

# initializing app
app = Flask(__name__, template_folder="remote", static_folder="remote/static")


# remote
@app.route("/")
def remote():
    return render_template("index.html")

# API endpoint for remote control 
@app.route('/control/', methods=['POST'])
def send_command_to_keyboard():
    data = request.get_json()
    control(mode = data['mode'], key = data['button_id'])
    return jsonify(key = data['button_id'])
    


"""
flask is running on all addresses
in your current network.
Default host address = 0.0.0.0
Default port = 5000

-> Check firewall if port 5000 is allowed or not.
-> Change host to the local IP address of the device
   you want to control.
-> There is currently no security over this connection,
   avoid using in a public network.

"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
