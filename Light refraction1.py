import turtle,time,random,math
turtle.tracer(3)
wn=turtle.Screen()
wn.setup(850,880)
FONT=('times New Roman',15,'bold')
turtle.tracer(1)
#def fonts(value):
#    FONT=('times New Roman',value,'bold')
wn.bgpic('background1.gif')
image11 = ("fi11.gif")
image12 = ("fi12.gif")
image31 = ("fi31.gif")
image32 = ("fi32.gif")
wn.addshape(image11)
wn.addshape(image12)
wn.addshape(image31)
wn.addshape(image32)
AQ=['im1.gif','im2.gif','im3.gif',\
    'im4.gif','im5.gif',\
'im6.gif','im7.gif','im8.gif','im9.gif']

for i in range(9):
    wn.addshape(AQ[i])

t=turtle.Turtle()#   рыба
t.speed(10)
t.penup()
t.hideturtle()

t1=turtle.Turtle()
t1.up()
t1.hideturtle()
t1.goto(0,0)
t1.shape(AQ[0])

t3=turtle.Turtle()#  Отраженный луч
t3.up()
t3.color('red')
t3.pensize(10)
t3.hideturtle()


t4=turtle.Turtle()
t4.up()
t4.pensize(10)
t4.color('red')
t4.goto(257,360)

t5=turtle.Turtle()#             Угол падения величина величина
t5.hideturtle()
t5.up()
t5.color('navy')
t51=t5.clone()

t6=turtle.Turtle()#                   Угол преломления величина
t6.hideturtle()
t6.up()
t6.color('navy')


t7=turtle.Turtle('square')   #  Вертикальная прямая
t7.hideturtle()
t7.up()
t7.color('black')
t7.shapesize(15,0.05)

A0=int(wn.textinput('Преломление Луча','Угол падения= '))
A1=270-A0
A_rad=math.radians(A0)
sin_A=math.sin(A_rad)
B_rad=math.asin(sin_A/1.33)
B_degree=math.degrees(B_rad)
t4.setheading(A1)
t4.down()
t4.showturtle()
t4.fd(160/math.cos(A_rad))

t4_position=t4.position()
t4X=t4.xcor()
t4Y=t4.ycor()
print('T4=',t4X,t4Y)

if A0<30:
    t5.goto(t4X+7,t4Y+70)
    t51.goto(t4X-25,t4Y+70)
if A0>29:
    t5.goto(t4X+7,t4Y+40)
    t51.goto(t4X-25,t4Y+40)

t5.write(A0,font=FONT)
t51.write(A0,font=FONT)

B_degree1=int(round(B_degree,0)) 
print(B_degree1)

if A0<30:
    t6.goto(t4X-22,t4Y-110)
if A0>29:
    t6.goto(t4X-22,t4Y-65)
    
t6.write(B_degree1,font=FONT)

t7.showturtle()
t7.goto(t4_position)

t3.setheading(90+A0)
t3.setposition(t4_position)
t3.down()
t3.fd(140/math.cos(A_rad))
t3.showturtle()
t4.setheading(270-B_degree)
t4.color('blue')
t4.fd(160/math.cos(A_rad))
t4.showturtle()

X,Y=90,-90
dx,dy=8,16
k,r=0,0
t1.showturtle()
while True:
    time.sleep(0.12)
    r=r+1
    k=k+1
    k1=k%9
    r1=r%100
    t1.shape(AQ[k1])
    t.setposition(X+dx,Y+dy)
    X,Y=t.position()
    if dx>0 and r1<50:
        t.showturtle()
        t.shape(image11)
        
    if dx>0 and r1>50:
        t.showturtle()
        t.shape(image12)
    if dx<0 and r1<50:
        t.showturtle()
        t.shape(image31)
    if dx<0 and r1>50:
        t.showturtle()
        t.shape(image32)
    if X>300 or X<-300:
        dx=-dx
    if Y<-230 or Y>120:
        dy=-dy
    
    