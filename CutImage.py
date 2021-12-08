#este codigo hace un recorte en la imagen de prueba 
import cv2

imagen = cv2.imread('ave.jpg')
#imagen [fila inicial: fila final, Columna inicial: Columna Final]
imagenSalida = imagen [60:220,280:480]

cv2.imshow('IMAGEN DE PRUEBA', imagen)
cv2.imshow('RECORTE', imagenSalida)
cv2.waitKey(0)
cv2.destroyAllWindows()
