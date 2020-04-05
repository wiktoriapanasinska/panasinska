def setup():
    size(600, 600)
    frameRate(30)
    global slownik_kolorow
    background(230,214,144)
    
    slownik_kolorow = {"różowy":(222,076,138, 80), "niebieski":(0,0,255,80), "żółty":(255,255,000,80)}
    global lista_kolorow
    lista_kolorow = []
    
    for klucz, wartosc in slownik_kolorow.items():
        lista_kolorow.append(wartosc)
    global iteracja
    iteracja =570

def draw():
    global iteracja
    iteracja -=1

    

    rect(iteracja/2,iteracja,30,30)



    stroke(222,076,138, 80)
    stroke(*slownik_kolorow["różowy"])
    strokeWeight(5)
    fill(*lista_kolorow[iteracja%len(lista_kolorow)])
    
    print(lista_kolorow)
    print(len(lista_kolorow))
    print(iteracja)
    print(iteracja%3)
    print(lista_kolorow[0])
    print(lista_kolorow[1])
    print(lista_kolorow[2])
    

    
    if mousePressed:
        exit()
