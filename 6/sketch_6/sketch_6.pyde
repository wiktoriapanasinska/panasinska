class Kwadrat():
    def __init__(self, bok): 
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
class PasiastyKwadrat(Kwadrat): 
    def sketchPasiasty(self, x, y, paski): 
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
class KolorowyPasiastyKwadrat(PasiastyKwadrat):
    def sketchKolorowyPasiasty(self,x, y, paski):
        fill(255, 255, 0,200)
        Kwadrat.sketch(self,x,y)
        space = self.bok/paski
        _xLinii_ = 0 
        for pasek in range(0, paski): 
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            colorMode(HSB, 360, 100, 100)
            for i in range(200): 
                for j in range(100):
                    stroke(i, j, 100)
            
def setup():
    size(500, 500)
    background(250,128,114)
       
    malyKwadrat = Kwadrat(40.0) 
    malyKwadrat.sketch(250, 300)
    duzyKwadrat = Kwadrat(200.0)
    duzyKwadrat.sketch(50, 75)
    malyPasiastyKwadrat = PasiastyKwadrat(30.0)
    malyPasiastyKwadrat.sketchPasiasty(350, 300, 5)
    duzyKolorowyPasiastyKwadrat = KolorowyPasiastyKwadrat (100.0)
    duzyKolorowyPasiastyKwadrat.sketchKolorowyPasiasty(100,300,20)
    malyKolorowyPasiastyKwadrat = KolorowyPasiastyKwadrat (35.0)
    malyKolorowyPasiastyKwadrat.sketchKolorowyPasiasty(400,200,10)
    
    # Przepraszam,że wysyłam tak późno, ale czekałam wczoraj na lot astronautów na ISS i nie zauważyłam, że się nie dodało :(
    # P.S. i tak przełożyli lot niestety




    
    

    
    

  
