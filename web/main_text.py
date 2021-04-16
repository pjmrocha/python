from flask import Flask

app = Flask("__main__")

@app.route("/")
@app.route("/hello")
def hello():
    return ("Hello World!")

@app.route("/bye")
def bye():
    return ("Goodbye World!")

if __name__ == "__main__":
    app.run(debug=True)
