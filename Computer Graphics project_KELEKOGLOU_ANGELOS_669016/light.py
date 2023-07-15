import glm



#phong lighting

class Light:
    def __init__(self,position=(50,50,-10),color=(1,1,1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        #added
        self.direction = glm.vec3(0,0,0)

        #intensities
        self.Ia = 0.1 * self.color #ambient
        self.Id = 0.8 * self.color #diffuse
        self.Is = 0.01  * self.color #specular

        #added
        self.m_view_light = self.get_view_matrix()

    #added
    def get_view_matrix(self):
        return  glm.lookAt(self.position,self.direction,glm.vec3(0,1,0))

