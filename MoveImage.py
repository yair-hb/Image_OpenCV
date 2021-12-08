#este codigo realiza traslacion de la imagen de prueba 
import cv2
import numpy as np

imagen = cv2.imread('ave.jpg')
ancho = imagen.shape[1]
alto = imagen.shape[0]
#se realizq la traslacion 
m = np.float32([[1,0,-150],[0,1,150]]) #se modifican los valores para la posicion
imagenSalida = cv2.warpAffine(imagen, m, (ancho, alto))

cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.imshow('IMAGEN DE SALIDA', imagenSalida)
cv2.waitKey(0)
cv2.destroyAllWindows()
