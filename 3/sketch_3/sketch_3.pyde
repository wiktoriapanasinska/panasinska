def setup():
    size(400, 400)
    textSize(60)
    background(230,214,144)
    frameRate(10)
    slownik_kolorow = {"różowy":(222,076,138), "niebieski":(0,0,255), "żółty":(255,255,000)}
    global lista_kolorow
    lista_kolorow = []
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc)
    global iteracja
    iteracja =570

def draw():                         
    global iteracja_programu
    iteracja_programu +=1 
    
    
def draw():
    clear()
    background(230,215,144)
    text("W", 140, 200)
    print(hex(get(mouseX, mouseY)))
    fill(255,255,000)
    text("P",200,200)
    
    if keyPressed:
        text("P",200,200)
        print(hex(get(mouseX, mouseY)))
        fill(*lista_kolorow[iteracja%len(lista_kolorow)])
    
        
    
    
    s = createShape() 
    s.beginShape() 
    s.fill(255,255,224,80) 
    s.stroke(222,076,138,80)
    strokeWeight(5)
    s.vertex(100,height/4*2)
    s.vertex(250,height/4*2)
    s.vertex(200,height/2-100)
    s.vertex(210,height/2-80)
    s.vertex(100,height/2-100)

    
    
    s.endShape(CLOSE)
    shape(s, 25, 25) 
    


def mouseMoved():
        print(hex(get(150,200))) 
        fill(222,076,138)
