import random
add_library('pdf') 


def setup():
    global img 
    size(400, 400) 
    img1 = loadImage("zdj.png") 
    beginRecord(PDF, "zdj.pdf")
    image(img1,0,0, height, width)
    
    print(random.random())
    print(type(img1))


def draw():
    if keyPressed:
        if key == ('m'):
            img1 = loadImage("zdj.png")
            image(img1,0,0,height,width)
            global img
            img = loadImage("lips.png")
            beginRecord(PDF,"lips.pdf")
            image(img,140,215,height-300,width-350)
            endRecord() 
        if key == ('n'):
            img1 = loadImage("zdj.png")
            image(img1,0,0,height,width)
            global img
            img = loadImage("lips2.png")
            beginRecord(PDF,"lips2.pdf")
            image(img,140,215,height-292,width-340)
            endRecord()

def mousePressed():
    exit()
