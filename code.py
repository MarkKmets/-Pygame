from pygame import *
window=display.set_mode((500,500))
display.set_caption('Віконце')
picture=image.load('project.jpg')
transform.scale(picture,(500,500))
clock = time.Clock()
play=True
color=(0,255,0)

class Area(sprite.Sprite):
    def __init__(self,x,y,width,height,color):
        super().__init__()
        self.rect=Rect(x,y,width,height)
        self.fill_color=color
    def draw(self):
        draw.rect(window,self.fill_color,self.rect)
class Pic(sprite.Sprite):
    def __init__(self,x,y,width,height):
        super().__init__()
        self.image=transform.scale(image.load('doge.jpg'),(width,height))
        self.x=x
        self.y=y
    def draw(self):
        window.blit(self.image,(self.x,self.y))
    
        
doge=Pic(200,100,110,110)
cube=Area(100,100,60,60,color)
while play:
    time.delay(50)
    window.blit(picture,(0,0))  
    for e in event.get():
        if e.type == QUIT:
            play=False
    cube.draw()
    doge.draw()
    display.update()
    clock.tick(40)
display.update()