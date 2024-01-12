import turtle as t
x=0
y=0
a=float(input("Quadratic term coefficients"))
b=float(input("Primary term coefficients"))
c=float(input("Constant terms"))
t.screensize(1,1)
t.speed('fastest')
t.ht()
t.up()
t.goto(0,0)
t.down()
while y<=200 and y>=-200:#Image Limit Range
    y=a*(x**2)+b*x+c#expression
    t.goto(x,y)
    x=x+0.05
t.up()
t.goto(0,0)
t.down()
y=0
x=0
while y>=-200 and y<=200:#Image Limit Range
    y=a*(x**2)+b*x+c#expression
    t.goto(x,y)
    x=x-0.05
#Draw the x and y axes
t.up()
t.goto(0,0)
t.down()
t.pencolor("red")
t.fd(300)
t.lt(180)
t.write('x')
t.fd(600)
t.lt(180)
t.fd(300)
t.pencolor("blue")
t.lt(90)
t.fd(300)
t.lt(180)
t.write('y')
t.fd(600)
t.done()
