from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    # template_path = "response.html"

    x = 0

    x_list = []
    for i in range(50):
        x += 1
        x_list.append(x)

    return render_template("response.html", x_list=x_list)


if __name__ == '__main__':
    app.run(debug=True)
