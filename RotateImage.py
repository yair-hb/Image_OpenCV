#este codigo rota y escala la imagen de prueba 
import cv2
import numpy as np

imagen = cv2.imread('ave.jpg')
ancho = imagen.shape[1]
alto = imagen.shape[0]

#aqui se realiza la rotacion
m = cv2.getRotationMatrix2D((ancho/2, alto/2), 45, .5)
imagenSalida = cv2.warpAffine(imagen, m, (ancho, alto))

cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.imshow('IMAGEN DE SALIDA', imagenSalida)
cv2.waitKey(3000)
cv2.destroyAllWindows()
