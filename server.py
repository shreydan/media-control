from flask import Flask, jsonify, render_template, request
from controller import control


app = Flask(__name__, template_folder="remote", static_folder="remote/static")


@app.route("/")
def remote():
    return render_template("index.html")


@app.route('/control/', methods=['POST'])
def send_command_to_keyboard():
    data = request.get_json()
    control(mode = data['mode'], key = data['button_id'])
    return jsonify(key = data['button_id'])
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
