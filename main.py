from flask import Flask, send_file
import turtle
import math

app = Flask(__name__)

def draw_heart():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.tracer(0) 

    t = turtle.Turtle()
    t.speed(0)
    t.color("red")
    t.penup()

    def a(k):
        return 15 * math.sin(k) ** 3

    def b(k):
        return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

    for i in range(6000):
        t.goto(a(i) * 20, b(i) * 20)
        t.pendown()

    screen.update()

    ts = t.getscreen()
    ts.getcanvas().postscript(file="heart.ps")
    turtle.bye() 

draw_heart()

@app.route('/run-code', methods=['GET'])
def run_code():
    draw_heart()
    return send_file("heart.ps", mimetype="image/postscript")

if __name__ == '__main__':
    app.run(debug=True)
