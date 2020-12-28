import turtle,time,random,math
turtle.tracer(3)
wn=turtle.Screen()
wn.setup(850,880)
FONT=('times New Roman',15,'bold')
wn.bgpic('background1.gif')
image11 = ("fi11.gif")
image12 = ("fi12.gif")
image31 = ("fi31.gif")
image32 = ("fi32.gif")
wn.addshape(image11)
wn.addshape(image12)
wn.addshape(image31)
wn.addshape(image32)
t=turtle.Turtle()
t.speed(10)
t.penup()
t.hideturtle()

t1=turtle.Turtle()
t1.up()
t1.goto(0,-120)

t2=turtle.Turtle()   #Sun
t2.hideturtle()
t2.up()
t2.goto(269,382)
wn.addshape('Sun.gif')
t2.shape('Sun.gif')
t2.showturtle()

t3=turtle.Turtle()
t3.up()
t3.pensize(10)
t3.hideturtle()

t4=turtle.Turtle()
t4.up()
t4.hideturtle()
t4.goto(257,360)
t4.pensize(10)
t4.down()

A0=int(wn.textinput('Преломление Луча','Угол падения= '))
A1=270-A0
A_rad=math.radians(A0)
sin_A=math.sin(A_rad)
B_rad=math.asin(sin_A/1.33)
B_degree=math.degrees(B_rad)
B_degree1=int(round(B_degree,0)) 

t4.setheading(A1)
t3.setheading(90+A0)

t4X=t4.xcor()
t4Y=t4.ycor()

t5=turtle.Turtle()#             Угол падения
t5.hideturtle()
t5.up()
t5.color('navy')
t51=t5.clone()

t6=turtle.Turtle()#                   Угол преломления
t6.hideturtle()
t6.up()
t6.color('navy')

t7=turtle.Turtle()
t7.hideturtle()
t7.up()
wn.addshape('line.gif')
t7.shape('line.gif')
t7.hideturtle()
t7.goto(1000,1000)

turtle.tracer(3)
X,Y=90,-90
dx,dy=8,16
k,r=0,0
t4.showturtle()
n=0
t5.hideturtle()
while True:
    t4.showturtle()
    if t4.ycor()>200:
        t4.setheading(A1)
        t4.color('red')
        t4.fd(10)
        t4_position=t4.position()
        t3.setposition(t4_position)
        t4X=t4.xcor()
        t4Y=t4.ycor()
       
        if t4.ycor()<215 and t4.ycor()>200:
            n=n+1
            if n==2 and A0>39:
                t5.goto(t4X+5,t4Y+30)
                t51.goto(t4X-30,t4Y+30)                
                t5.write(A0,font=FONT)
                t51.write(A0,font=FONT)
                t6.goto(t4X-28,t4Y-80)
                t6.write(B_degree1,font=FONT)
            
            if n==2 and A0<40:
                t5.goto(t4X+5,t4Y+100)
                t51.goto(t4X-30,t4Y+100)                
                t5.write(A0,font=FONT)
                t51.write(A0,font=FONT)
                t6.goto(t4X-28,t4Y-140)
                t6.write(B_degree1,font=FONT)
   
    if t4.ycor()<205 and t4.ycor()>-270:
        t4.setheading(270-B_degree)
        t4.color('blue')
        t4.fd(10)
        t3.color('red')
        t3.showturtle()
        if t3.ycor()<350:
            t3.down()
            t3.fd(10)
        if t3.ycor()>350:
            t3.fd(0)
      
        t7.goto(t4_position)
        t7.showturtle()
        t7.shape('line.gif')
    
    if t4.ycor()<-100:
        turtle.tracer(2)
        t4.fd(0)
        t4.clear()
        t4.hideturtle()
        t4.up()
        t4.goto(257,360)
        t4.showturtle()
        t4.color('gold')
        t4.down()
        
        t3.up()
        t3.clear()
        t3.hideturtle()
        t3.up()
        t3.setposition(t4_position)
        t7.goto(1000,1000)
        n=0
        t5.clear()
        t51.clear()
        t6.clear()
    r=r+1
    k=k+1
    k1=k%9
    r1=r%100
    time.sleep(0.1)
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
    
