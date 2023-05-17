# importação das bibliotecas
import cv2
# Leitura da imagem com função VideoCapture
captura = cv2.VideoCapture(0)
#Loop para executar a função de leitura e de mostrar a imagem
while True:
    ret, imagem = captura.read()
    cv2.imshow("Video", imagem)
    if cv2.waitKey(1) == ord('q'):
        break


captura.release()
cv2.destroyAllWindows()