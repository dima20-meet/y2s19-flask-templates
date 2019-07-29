from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template(
"index.html")


if __name__ == '__main__':
   app.run(debug = True)

# def hello_world():
#     food = ["pizza", "sushi", "qr3"] 
#     return render_template(
# "index.html",
# food=food,)

