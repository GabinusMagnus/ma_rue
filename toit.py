from ipycanvas import Canvas
rue = Canvas(width=800, height=400)

def toit1(x, niveau):
    y = rue.height - niveau * 60
   
   
    rue.begin_path();
    rue.fill_style = 'black';
    rue.move_to(x-70, y);
    rue.line_to(x, y-40);
    rue.line_to(x+70, y);    
    rue.fill();
   
toit1(150, 2)
rue
