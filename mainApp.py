from flask import Flask,render_template


app=Flask(__name__)



@app.route("/play")
def play():
    return render_template("index.html",boxes=3,color="blue")


@app.route("/play/<num>")
def num(num):
    return render_template("index.html",boxes=int(num),color="blue")


@app.route("/play/<num>/<colors>")
def color(num,colors):
    print(colors)
    if(colors!="red" and colors!="blue" and colors!="green"):
        print("Error")
        return render_template("index.html",boxes=int(num),color="blue") 
    return render_template("index.html",boxes=int(num),color=colors)

@app.route("/")
def root():
    return render_template("base.html")

@app.route("/child")
def child():
    return render_template("child.html")



if(__name__=="__main__"):
    app.run(debug=True)