import pygame as pg
import  moderngl as mgl

class Texture:
    def __init__(self,app):
        self.app = app
        self.ctx  = app.ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='container2.png')
        self.textures[1] = self.get_texture(path='texturew.jpg')
        #added
        self.textures['depth_texture'] = self.get_depth_texture()

#added
    def get_depth_texture(self):
        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    def get_texture(self,path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture,flip_x=False,flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(),components=3,
                                   data=pg.image.tostring(texture,'RGB'))

        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR,mgl.LINEAR)
        texture.build_mipmaps()
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]
