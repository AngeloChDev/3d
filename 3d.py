from ursina import *


app = Ursina()                                  #### inizialize app 3d

cube = Entity(model='cube', color=color.green, texture='withe_cube', scale=2 )    ### create a identity object

def update():
    cube.rotation_x = cube.rotation_x + 0.25
    cube.rotation_y = cube.rotation_y + 0.25
    cube.x += held_keys['s'] * 0.2
    cube.x -= held_keys['a'] * 0.2
    cube.y += held_keys['q'] * 0.2
    cube.y -= held_keys['d'] * 0.2
    
app.run()
    