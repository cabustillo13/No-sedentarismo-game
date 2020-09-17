#Es una implementacion para Python3
import cv2
import imutils
import numpy as np
from collections import deque
import time
import pyautogui
from threading import Thread
import modos

#Clase que implementa subprocesos separados para la lectura de los frames.
class WebcamVideoStream:
    def __init__(self):
        self.stream = cv2.VideoCapture(0)
        self.ret, self.frame = self.stream.read()
        self.stopped = False
    def start(self):
        Thread(target = self.update, args=()).start()
        return self
    def update(self):
        while True:
            if self.stopped:
                return
            self.ret, self.frame = self.stream.read()
    def read(self):
        return self.frame
    def stop(self):
        self.stopped = True

#Recordar que es sensible a la gama de verdes o amarillo fosforecente
#Definir la gama de colores HSV para objetos de color verde
colorLower = (29, 86, 6)
colorUpper = (64, 255, 255)

#Se utiliza en la estructura dequeu para almacenar numeros de puntos del buffer dados.
buffer = 20

#Se usa para que PyAutogui no haga clic en el centro de la pantalla en cada frame.
flag = 0

#Puntos deque estructura almacenando 'buffer' -> numero de coordenadas de objeto
pts = deque(maxlen = buffer)
#Cuenta el numero minimo de frames que se detectaran cuando se produzca un cambio de direccion.
counter = 0
#El cambio de direccion se almacena en dX y dY
(dX, dY) = (0, 0)
#Variable para almacenar cadena de direccion.
direction = ''
#Ultima variable presionada para detectar que tecla presiono PyAutogui
last_pressed = ''

#Delay de 2 segundos para encender la camara y arranque adecuadamente.
time.sleep(2)

#Usar la funcion de PyAutogui para detectar el ancho y alto de la pantalla. 
width,height = pyautogui.size()

#Inicie la captura de video en un thread separado del thread principal.
vs = WebcamVideoStream().start()

#Hacer click en el centro de la pantalla. Por eso la ventana del juego debe colocarse aqui.
pyautogui.click(int(width/2), int(height/2))

while True:

    #Guardar el frame leido en la variable frame
    frame = vs.read()
    #Voltea el frame para evitar el efecto espejo que se produce al tomar la foto. Mi brazo derecho en la imagen es mi brazo izquiedo.
    frame = cv2.flip(frame,1)
    #Redimensionar el frame dado y pasarlo a una ventana de 600x600.
    frame = imutils.resize(frame, width = 600)
    #Usar el filtro gaussiano de kernel size 11, para remover el excesivo ruido.
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    #Convertir el frame a HSV. Como HSV nos permite una mejor segmentacion.
    hsv_converted_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    #Crear una mascara para cada frame, mostrando los valores verdes. 
    mask = cv2.inRange(hsv_converted_frame, colorLower, colorUpper)
    #Erosione la salida enmascarada para eliminar pequeños puntos blancos presentes en la imagen enmascarada.
    mask = cv2.erode(mask, None, iterations = 2)
    #Dilatar la imagen resultante para restaurar nuestro objetivo.
    mask = cv2.dilate(mask, None, iterations = 2)

    #Encontrar todos los contornos en la imagen enmascarada
    cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Para Python3

    #Definir el centro de la bola que se muestra en pantalla, para que se detecte como Ninguno.
    center = None

    #Si se detecta algún objeto, que comience el while
    if(len(cnts) > 0):
        #Encontrar el contorno que presenta el area maxima.
        c = max(cnts, key = cv2.contourArea)
        #Encontrar el centro del circulo, que contiene el radio con la mayor circunferencia. 
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        #Calcular el centroide de la bola. Esto nos servira para dibujar el circulo alrededor.
        M = cv2.moments(c)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        #Proceda solo si se detecta una bola con un size considerable
        if radius > 10:
            #Dibujar el circulo alrededor del objeto y su centro
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, center, 5, (0,255,255), -1)
            #Agregar el objeto detectado al frame en la estructura de puntos deque
            pts.appendleft(center)

    #Se usa la funcion arange de numpy para un mejor rendimiento. Se hace un loop para todos los puntos detectados.
    for i in np.arange(1, len(pts)):
        #Si no hay puntos detectados, muevete.
        if(pts[i-1] == None or pts[i] == None):
            continue

        #Si al menos 10 frames tienen un cambio de direccion, se procede.
        if counter >= 10 and i == 1 and pts[-10] is not None:
            #Calcular la distancia entre el frame actual y el decimo frame.
            dX = pts[-10][0] - pts[i][0]
            dY = pts[-10][1] - pts[i][1]
            (dirX, dirY) = ('', '')

            #Si la distancia es mayor a 50 pixeles, se debe considerean que la direccion ha cambiado.
            if np.abs(dX) > 50:
                dirX = 'Izquierda' if np.sign(dX) == 1 else 'Derecha'

            if np.abs(dY) > 50:
                dirY = 'Arriba' if np.sign(dY) == 1 else 'Abajo'

            #Set el valor de la direccion a la direccion detectada.
            direction = dirX if dirX != '' else dirY
            #Escribir la direccion detectada en el frame.
            cv2.putText(frame, direction, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

        #Dibuja una linea roja al final para representar el movimiento del objeto.
        thickness = int(np.sqrt(buffer / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

    last_pressed = modos.tipoJuego(last_pressed,direction,'right','left','space','down',"Derecha","Izquierda","Arriba","Abajo")
    #Mostrar el frame en el output.
    cv2.imshow('Game Control Window', frame)
    key = cv2.waitKey(1) & 0xFF
    #Actualizar el contador a medida que se detecta el cambio de direccion.
    counter += 1

    #Si PyAutogui no hace click al medio, que haga click una vez para enfocarte en la ventana del juego.
    if (flag == 0):
        pyautogui.click(int(width/2), int(height/2))
        flag = 1

    #Sí se presiona q, cerrar la ventana.
    if(key == ord('q')):
        break
#Despues de todos los procesos, cerrar la webcam y destruir todas las ventanas.
vs.stop()
cv2.destroyAllWindows()
 
