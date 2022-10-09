#Gabriel Alejandro Vicente Lorenzo
#SR1 UVG

#Se importan los metodos solicitados por el ejercicios
import gl


gl.glInit()
#Se crea la Ventana (Que renderiza a.bmp)
gl.glCreateWindow(1024,1024)

#Cambia el color con el que trabaja Clear
gl.glClearColor(0,1,0.75)

#Pinta TODOELMAPA de bits de un mismo color
gl.glClear()

#Se crea el ViewPort (Ventana mas pequeña que se dibuja apartir de x y y)
gl.glViewPort(100, 100, 824, 824)

#Definir el color del punto
gl.glColor(1,1,1)

#Se pinta el punto
gl.glVertex(-1,-1)

#Escribe el archivo .bmp
gl.glFinish()
