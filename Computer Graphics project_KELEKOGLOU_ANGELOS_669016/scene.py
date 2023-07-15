from model import *

class Scene:
    def __init__(self,app):
        self.app = app
        self.objects = []
        self.load()

    def add_object(self,obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        n, s = 10, 2
        for x in range(-n,n,s):
            for z in range(-n,n,s):
                add(Cube(app,tex_id=1,pos=(x,-s,z)))

        add(Cube(app,pos=(1,2,0)))





    def render(self):
        for obj in self.objects:
            obj.render()
