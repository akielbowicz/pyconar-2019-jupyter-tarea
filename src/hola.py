import ipycanvas
import numpy

def dibujar():
    ancho, altura = 800,200
    cantidad_puntos = 628
    canvas = ipycanvas.Canvas(size=(ancho,altura))
    canvas.font = '70px helvetica'

    for color in ['green','red','yellow','blue']:
        canvas.fill_style = color
        x = numpy.random.randint(0,ancho,cantidad_puntos)
        y = numpy.random.randint(0,altura,cantidad_puntos)
        tamanios = numpy.random.randint(0,10,cantidad_puntos)
        canvas.fill_rects(x,y,tamanios)

    canvas.fill_style = 'magenta'
    canvas.fill_text('Bienvenide al taller.',12,102)
    canvas.fill_style = 'Black'
    canvas.fill_text('Bienvenide al taller.',10,100)
    return canvas