import pygame as pg
from object_3D import *
from camera import *
from object_3D import *
from projection import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1000,700
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()#após criar o main (a janela)
        
    def create_objects(self):#após criar o main (a janela)
        self.camera = Camera(self, [0.5, 1, -4])
        self.projection = Projection(self)
        self.object = Object3D(self) 
        self.object.translate([0.2, 0.4, 0.2])
        #self.object.rotate_y(math.pi / 6)(changed the command)
        self.axes = Axes(self)   
        self.axes.translate([0.7, 0.9, 0.7])
        self.world_exes = Axes(self)  
        self.world_exes.movement_flag = False     
        self.world_exes.scale(2.5)
        self.world_exes.translate([0.0001, 0.0001, 0.0001])    
          
       
    
    def draw(self):
        self.screen.fill(pg.Color('darkslategray')) 
        self.world_exes.draw()   
        self.axes.draw()
        self.object.draw()
         
   
        
    def run(self):
        while True:
            self.draw()
            self.camera.control()#Trabalhando com a movimentação da imagem.
            [exit()for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)
            
if __name__ == '__main__':
    app = SoftwareRender()
    app.run()                