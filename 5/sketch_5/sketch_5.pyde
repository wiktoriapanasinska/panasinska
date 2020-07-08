class Kolo(): 
    kolor = False 
    def __init__(self, arg_1, arg_2, arg_3): #lepiej gdy nazwy wskazują na to czym są, lepiej się wóczas korzysta z kodu
        self.arg_1 = arg_1
        self.arg_2 = arg_2
        self.arg_3 = arg_3
    def mydraw(self): # stosowanie nazw wbudowanych może mieć nieprzewidziane konsekwencje, zamiast twojej metody może sie wywołąć wbudowana
        if self.kolor:
            fill(125, 60, 152)
        circle(self.arg_1, self.arg_2, self.arg_3)
        noStroke()
        noFill() # żeby inne rysowane po Twoim kole elementy nie posiadały tego koloru

def setup():                      
    size(400,400)
    global kolo1
    global kolo2
    kolo1 = Kolo(250,120, 100)                            
    kolo2 = Kolo(160, 250, 150)
        
def keyPressed():
    if key == CODED:              
        if keyCode == RIGHT:
            kolo1.arg_1 = min(kolo1.arg_1,345)+5
        elif keyCode == LEFT:
            kolo1.arg_1 = max(kolo1.arg_1,55)-5
        elif keyCode == UP:
            kolo1.arg_2 = max(kolo1.arg_2,55)-5
        elif keyCode == DOWN:
            kolo1.arg_2 = min(kolo1.arg_2,345)+5
            
def mouseMoved():
    a = (hex(get(mouseX, mouseY)))
    print(a)
    if a == "FF27AE60" or a == "FF7D3C98":
        kolo2.kolor = not kolo2.kolor
 
def draw():
    background(255, 192, 203)
    fill(39, 174, 96)
    kolo2.mydraw()
    fill(255, 165, 0)
    kolo1.mydraw()
    
def mousePressed():
    exit()
    
#1,75pkt i plus do aktywności za zmianę koloru w wymagający sposób
    
    
