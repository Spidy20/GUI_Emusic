import pyglet

animation = pyglet.image.load_animation('em.gif')
animsprite = pyglet.sprite.Sprite(animation)

w = animsprite.width
h = animsprite.height

wind = pyglet.window.Window(width=w,height=h)
r,g,b,alpha = 0.5,0.5,0.8,0.5
pyglet.gl.glClearColor(r,g,b,alpha)

@wind.event
def on_draw():
    wind.clear()
    animsprite.draw()