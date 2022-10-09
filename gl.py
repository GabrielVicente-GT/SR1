#Archivo gl solicitado por SR1

#Importa el archivo proporcionado en clase
import  Render 

#Le asigna al renderizado global un render sencillo
def glInit():
    global renderizado
    renderizado = Render.Render(1,1)

#Crea la ventana con el ancho y la altura que el usuario desea
def glCreateWindow(width, height):
    global renderizado
    global widthFrame
    global heightFrame

    #Si el ancho y alto cumplen con la condicion de que sean valores
    #modulos de 4 se crea el render, de otrao forma, se adaptan para que sean
    #modulos de 4
    
    if width % 4 == 0 and height % 4 == 0:
        renderizado       = Render.Render(width,height)
    else:
        width   = width+width%4
        height  = height+height%4
        renderizado       = Render.Render(width,height)
    
    widthFrame  = width
    heightFrame = height
    
#Se crea la ventana donde se trabajara el punto
def glViewPort(x, y, width, height):

    #posicion desde la que se crea el view port
    #Se crea desde la esquina inferior izquierda
    global xPositionVP
    global yPositionVP
    
    #altura y ancho de viewport
    global widthVP
    global heightVP

    #si sobrepasan la altura y ancho de la ventana total se hace una reasignacion
    if  x > widthFrame or x < 0:
        x = widthFrame
    elif y > heightFrame or y < 0:
        y = heightFrame

    #posicion de inicio para el viewport
    xPositionVP = x
    yPositionVP = y


    #si sobrepasa la suma de la altura con la posicion el alto y ancho
    #respectivo, se hace una reasignacion
    if (xPositionVP + width) > widthFrame:
        width = widthFrame - xPositionVP
    if (yPositionVP + height) > heightFrame:
        height = heightFrame - yPositionVP
    
    widthVP     = width
    heightVP    = height

    #se renderiza el viewport
    for w in range (xPositionVP, xPositionVP + widthVP):
        for z in range (yPositionVP, yPositionVP + heightVP):
            renderizado.point(w, z)

#Se pinta todo el tablero de pixeles con el color predeterminado
def glClear():
    global renderizado
    renderizado.clear()

#Se cambia el color predeterminado
def glClearColor(r, g, b):
    global renderizado
    renderizado.window_color = Render.color(round(255*r), round(255*g), round(255*b))

#Se dibuja un punto en las cordenadas especificas (respetando el viewport)
def glVertex(x, y):
    global puntomedidoX
    global puntomedidoY
    
    if y > 0:
        puntomedidoY = yPositionVP + round(heightVP/2) + round((heightVP/2)*y)
    elif y < 0:
        puntomedidoY = yPositionVP + round(heightVP/2) - round((heightVP/2)*(-y))
    elif y == 0:
        puntomedidoY = yPositionVP + round(heightVP/2)
        
    if x > 0:
        puntomedidoX = xPositionVP + round(widthVP/2) + round((widthVP/2)*(x))
    elif x < 0:
        puntomedidoX = xPositionVP + round(widthVP/2) - round((widthVP/2)*(-x))
    elif x == 0:
        puntomedidoX = xPositionVP + round(widthVP/2)
        
    # for xx in range(10):
    #     for yy in range (10):
    # # print(puntomedidoX,puntomedidoY)
    #         renderizado.point(923+xx,100+yy)
    if puntomedidoY == (yPositionVP +heightVP):
        
        puntomedidoY = puntomedidoY -1
        
    if puntomedidoX == (xPositionVP +widthVP):
        
        puntomedidoX = puntomedidoX -1
    renderizado.uniquepoint(puntomedidoY,puntomedidoX)

#Se cambia el color con el que se dibuja el punto
def glColor(r, g, b):
    global renderizado
    renderizado.point_color = Render.color(round(255*r), round(255*g), round(255*b))

#Se escribe el archivo
def glFinish():
    global renderizado
    renderizado.write('a.bmp')



