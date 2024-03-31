import cv2

# Carregar a imagem
img = cv2.imread('aula2/logo-if.jpg')

# Imprimir a forma da imagem (número de linhas, colunas e canais de cor)
print(img.shape)

# Obter as dimensões da imagem
(row, col) = img.shape[0:2]

# Iterar sobre cada pixel na imagem
for i in range(row):
    for j in range(col):
        # Calcular a média dos valores de cada canal de cor (BGR)
        gray_value = sum(img[i, j]) * 0.33
        
        # Atribuir o valor calculado a cada canal de cor
        img[i, j] = [gray_value, gray_value, gray_value]

# Exibir a imagem em escala de cinza resultante
cv2.imshow('GRAY', img)

# Aguardar até que uma tecla seja pressionada
cv2.waitKey(0)

# Fechar todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
