from flask import Flask, jsonify, render_template, request

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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
