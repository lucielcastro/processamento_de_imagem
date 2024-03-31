import cv2

# Carregar a imagem
img = cv2.imread('aula2/original.jpeg')

# Redimensionar a imagem para facilitar a visualização
img = cv2.resize(img, (350, 505))

# Converter a imagem para o espaço de cores HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Fazer uma cópia da imagem original para a imagem em escala de cinza resultante
gray = img.copy()

# Obter as dimensões da imagem
(row, col) = img.shape[0:2]

# Iterar sobre cada pixel na imagem
for i in range(row):
    for j in range(col):
        # Verificar se a matiz do pixel está fora da faixa desejada
        if (hsv[i, j][0] < 170) or (hsv[i, j][0] > 200):
            # Calcular a média dos valores de cada canal de cor (BGR)
            gray_value = sum(img[i, j]) * 0.33
            # Atribuir o valor calculado a cada canal de cor na imagem em escala de cinza
            gray[i, j] = [gray_value, gray_value, gray_value]

# Exibir as imagens
cv2.imshow('Original', img)  # Imagem original
cv2.imshow('HSV', hsv)        # Imagem no espaço de cores HSV
cv2.imshow('Result', gray)     # Imagem resultante (apenas pixels com matiz na faixa desejada em escala de cinza)

# Aguardar até que uma tecla seja pressionada
cv2.waitKey(0)

# Fechar todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
