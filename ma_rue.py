from ipycanvas import Canvas
rue = Canvas(width = 800, height = 400)

def affiche(canvas):
    canvas.clear()
    display(canvas)


if __name__ == '__main__':
    affiche(rue)