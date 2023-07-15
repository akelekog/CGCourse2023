import numpy as np
import glm
import pygame as pg
import moderngl as mgl

class BaseModel:
    def __init__(self,app,vao_name,tex_id,pos=(0,0,0)):
        self.app = app
        self.pos = pos
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera =  self.app.camera
        self.vao_name = vao_name
    def update(self):...

    def get_model_matrix(self):
        m_model =  glm.mat4()
        #translate
        m_model = glm.translate(m_model,self.pos)
        return  m_model
    def render(self):
        self.update()
        self.vao.render()

class Cube(BaseModel):
    def __init__(self,app,vao_name='cube',tex_id=0,pos=(0,0,0)):
        super().__init__(app,vao_name,tex_id,pos)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)

        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)
    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()




    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        #depth texture
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)

        #shadow
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)

        #texture
        self.texture =  self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)


        #mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

        #light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)







