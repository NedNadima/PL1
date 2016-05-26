from flask import Flask
app = Flask(__name__)


@app.route("/test/<int:x>")
def test(x):
    numberlist = []
    for count in range (1,x):
        numberlist.append(count)
    return  ','.join(str (n) for n in numberlist)
        

if __name__ == "__main__":
    app.debug = True
    app.run()

