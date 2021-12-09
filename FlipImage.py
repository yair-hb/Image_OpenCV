#este codigo es para voltear una imagen usando cv2.flip
import cv2

imagen =  cv2.imread('ave.jpg')
imagenGiro = cv2.flip(imagen, 1)

cv2.imshow('IMAGEN DE PRUEBA', imagen)
cv2.imshow('IMAGEN VOLTEADA', imagenGiro)

cv2.waitKey(0)
cv2.destroyAllWindows()
