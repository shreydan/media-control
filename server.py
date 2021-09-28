from flask import Flask, jsonify, render_template, request
from controller import control


app = Flask(__name__, template_folder="remote", static_folder="remote/static")


@app.route("/")
def remote():
    return render_template("index.html")

@app.route("/test/")
def test():
    return jsonify(
        response= 200,
        value= f'you sent me this: {request.args.get("command")}'
    )


@app.route('/control/', methods=['POST'])
def send_command_to_keyboard():
    data = request.get_json()
    print('heres the damn data:', data, type(data))
    control(data['button_id'])
    return jsonify(damn = 'damn')
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
