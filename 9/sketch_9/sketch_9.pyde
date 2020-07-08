def setup():
    size(600,600)
    global img
    img=loadImage("chomiczek.png") 
    background(255, 248, 220)
    textSize(20) # nie zmieniasz w trakcie działania programu
    strokeWeight(2) # nie zmieniasz w trakcie działania programu
    
def draw():
    global img
    # zaladowanoObrazek = None # nie używasz tej zmiennej
    try:
        image(img, 100, 100, 400, 400) # tylko tą linię sprawdzamy pod kątem błędu, pozostałę powinny iść do else
    except:
        fill(0,0,0)
        text("Nie znaleziono pliku", 200, 300)
        stroke(255,0,0)
    else:
        stroke(30,144,255)
    finally: # to co się łączy z powyższym kodem powinno jeszcze się znaleźć w finally, jeżeli kolor ramki się nie wykona, nie ma sensu jej rysowanie - więc się łączy
        noFill()
        square(100, 100, 400)
        
# 1,5pkt
