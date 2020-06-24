def setup():
    size(600,600)
    global img
    img=loadImage("chomiczek.png") 
    background(255, 248, 220)
    
def draw():
    global img
    zaladowanoObrazek = None
    try:
        image(img, 100, 100, 400, 400)
        stroke(30,144,255)
    except:
        fill(0,0,0)
        textSize(20)
        text("Nie znaleziono pliku", 200, 300)
        stroke(255,0,0)
        strokeWeight(2)
    noFill()
    square(100, 100, 400)
