import pyautogui

#Definir modos de juego
def tipoJuego(last_pressed,direction,keyboard1,keyboard2,keyboard3,keyboard4,label1,label2,label3,label4):
    
    #Ej. Si es detectada la direccion Derecha, apretar el boton de la flecha derecha ->. 
    if direction == label1:
        if last_pressed != keyboard1:
            pyautogui.press(keyboard1)
            last_pressed = keyboard1

    #Ej. Si es detectada la direccion Izquierda, apretar el boton de la flecha izquierda <-.
    elif direction == label2:
        if last_pressed != keyboard2:
            pyautogui.press(keyboard2)
            last_pressed = keyboard2

    #Ej. Si es detectada la direccion Arriba, presionar el boton de la flecha para arriba. 
    elif direction == label3:
        if last_pressed != keyboard3:
            pyautogui.press(keyboard3)
            last_pressed = keyboard3

    #Ej. Si es detectada la direccion Abajo, presionar el boton de la flecha para abajo.
    elif direction == label4:
        if last_pressed != keyboard4:
            pyautogui.press(keyboard4)
            last_pressed = keyboard4

    return last_pressed
