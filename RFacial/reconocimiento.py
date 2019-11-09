import numpy as np
import cv2

#Cargamos la plantilla e inicilizamos la webcam
cv2.CascadeClassifier
face_cascade = cv2.CascadeClassifier('RFacial\haarcascade_frontalface_alt.xml')
cap = cv2.VideoCapture(0)

while(True):
    #Leemos un frame y lo guardamos
    valido, img = cap.read()

    #Si el frame se ha capturado correctamente, continuamos
    if valido:

        #Convertimos la imagen a blanco y negro
        img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        #Buscamos las coordenadas de los rostros(si lo hay)
        #guardamos su posicion
        array_rostros = face_cascade.detectMultiScale(img_gris, 1.3, 5)

        # Iteramos el array de rostros y pintamos un recuadro alrededor
        # de cada uno 
        for (x, y, w, h) in array_rostros:
            cv2.rectangle(img, (x,y),(x+w, y+h),(125,255,0),2)

        # Mostramos la imagen
        cv2.imshow('img',img)

        # Con la tecla 'q' salimos del programa
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
