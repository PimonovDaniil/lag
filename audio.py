import pyglet

song = pyglet.media.load('./video/audio2.mp3')
song.play()
pyglet.app.run()