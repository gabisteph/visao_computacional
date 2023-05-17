#importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('/home/lse/Área de Trabalho/visao_computacional/imagens/imagem.jpeg')
print('Largura em pixels:', end='')
print(imagem.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0]) #altura da imagem
print('Qtde de Canais: ', end='')
print(imagem.shape[2])
#Mostra a imagem com a função imshow
cv2.imshow("Janela", imagem)
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com a função imrite()
cv2.imwrite("Saída.jpg", imagem)

