def setup():
    size(300,400)# wartoby wykorzystac te wartosci pod wbudowanymi zmiennymi height i width
    rectMode(CORNERS)
    print(50,50)
    
def draw():
    if mousePressed:
        print(mouseX,mouseY,mousePressed)
        rect(mouseX,mouseY,220,220)
    # miało się też coś zadziać, gdy nie klikamy
# 1,5 pkt
    
