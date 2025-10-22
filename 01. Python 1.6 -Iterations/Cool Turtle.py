import turtle

bob=turtle.Turtle()
wn=turtle.Screen()
bob.shape("turtle")
bob.color("green")
bob.speed(100)

x=0
while x<120:
    bob.circle(20) # Draw a circle of radius 20px
    bob.forward(10)  # move forward 10 px
    bob.right(3)
    x=x+1
