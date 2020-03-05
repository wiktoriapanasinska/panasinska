def setup():
    size(300,400)
    rectMode(CORNERS)
    print(50,50)
    
def draw():
    if mousePressed:
        print(mouseX,mouseY,mousePressed)
        rect(mouseX,mouseY,220,220)
    
