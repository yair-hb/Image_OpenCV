#este codigo es para mostraar el video de la camara web de forma espejo
import cv2

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if ret == False: break

    anchoMitad = int(frame.shape [1]/2)
    frame[:,:anchoMitad] = cv2.flip(frame[:,anchoMitad:],1)
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
