from flask import Flask
app = Flask(__name__)

@app.route("/")
def test():
    numberlist = []
    for count in range (1,101):
        numberlist.append(count)
    return str (numberlist).strip("[]")
        

if __name__ == "__main__":
    app.debug = True
    app.run()
