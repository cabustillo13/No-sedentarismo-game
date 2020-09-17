#Python3
import cv2
import imutils
import numpy as np
from collections import deque
import time
import pyautogui
from threading import Thread
import modos

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

#Definir gama de colores
colorLower = (29, 86, 6)
colorUpper = (64, 255, 255)

buffer = 20
flag = 0
pts = deque(maxlen = buffer)
counter = 0

(dX, dY) = (0, 0)
direction = ''
last_pressed = ''

time.sleep(2)

width,height = pyautogui.size()
vs = WebcamVideoStream().start()
pyautogui.click(int(width/2), int(height/2))

while True:

    frame = vs.read()
    frame = cv2.flip(frame,1)
    frame = imutils.resize(frame, width = 600)
    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv_converted_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_converted_frame, colorLower, colorUpper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)

    cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Para Python3
    center = None

    if(len(cnts) > 0):
        c = max(cnts, key = cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

        if radius > 10:
            pts.appendleft(center)

    for i in np.arange(1, len(pts)):
        if(pts[i-1] == None or pts[i] == None):
            continue

        if counter >= 10 and i == 1 and pts[-10] is not None:
            dX = pts[-10][0] - pts[i][0]
            dY = pts[-10][1] - pts[i][1]
            (dirX, dirY) = ('', '')

            if np.abs(dX) > 50:
                dirX = "Izquierda" if np.sign(dX) == 1 else "Derecha"
            if np.abs(dY) > 50:
                dirY = "Arriba" if np.sign(dY) == 1 else "Abajo"

            direction = dirX if dirX != '' else dirY
            
    last_pressed = modos.tipoJuego(last_pressed,direction,'right','left','space','down',"Derecha","Izquierda","Arriba","Abajo")
    counter += 1
        
vs.stop()
cv2.destroyAllWindows()
 
