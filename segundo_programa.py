# importação das bibliotecas
import cv2
# Leitura da imagem com função VideoCapture
captura = cv2.VideoCapture(0)
#Loop para executar a função de leitura e de mostrar a imagem
while True:
    ret, imagem = captura.read()
    if ret == True:
        cv2.imshow("Video", imagem)
    # (b, g, r) = imagem[0,0]
    # print("Vermelho", r, "Azul", b, "Verde", g)
    #Pixel
    # imagem[0,0] = (255, 0, 0)
    #Retangulo
    # imagem[30:50, :] = [255, 0, 0]
        # if cv2.waitKey(30) & 0xff:
        #     break
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

captura.release()
cv2.destroyAllWindows()

# Atividade para próxima aula: Pegar uma imagem da zebra e apagar as listas da zebra

# #inserindo texto na imagem
# fonte = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(imagem, "walter", (15,65), fonte, 2, (255, 255, 255), 2, cv2.LINE_AA)