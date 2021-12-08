#este codigo cambia el tamaño de de la imagen de prueba 
import cv2
import imutils

imagen = cv2.imread('ave.jpg')

#en esta linea se realiza el cambio de tamaño
imagenSalida = cv2.resize(imagen,(300,500), interpolation=cv2.INTER_CUBIC)

#cambia el tamaño respetando el aspect ratio de la imagen
imagenSalida2 = imutils.resize(imagen, width=750)

cv2.imshow('IMAGEN DE ENTRADA', imagen)
cv2.imshow('IMAGEN DE SALIDA', imagenSalida)
cv2.waitKey(3000)
cv2.destroyAllWindows()
cv2.imshow('IMAGEN DE PRUEBA', imagen)
cv2.imshow('IMAGEN SALIDA USANDO IMUTILS', imagenSalida2)
cv2.waitKey(0)
cv2.destroyAllWindows()