import random
add_library('pdf') 


def setup():
    global img 
    size(400, 400) # proporcja nie zgadza się ze zdjęciami dokumentowymi
    img1 = loadImage("zdj.png") 
    beginRecord(PDF, "zdj.pdf")
    image(img1,0,0, height, width) # wystarczy tutaj, nie ma potrzeby rysować co klatkę
    
    print(random.random())
    print(type(img1))


def draw():
    if keyPressed:
        if key == ('m'):
            global img
            img = loadImage("lips.png")
            #beginRecord(PDF,"lips.pdf")
            image(img,140,215,height-300,width-350)
            endRecord() 
        if key == ('n'):
            global img
            img = loadImage("lips2.png")
            #beginRecord(PDF,"lips2.pdf")
            image(img,140,215,height-292,width-340)
            endRecord()

def mousePressed():
    exit()
    
1,25p
