import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('aula8/noise.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro gaussiano para remover ruídos
imagem_filtrada = cv2.GaussianBlur(imagem, (5, 5), 0)

# Aplicar thresholding para binarizar a imagem
_, imagem_binarizada = cv2.threshold(imagem_filtrada, 150, 255, cv2.THRESH_BINARY)

# Exibir as imagens original, filtrada e binarizada
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(imagem_filtrada, cmap='gray')
plt.title('Imagem Filtrada (Filtro Gaussiano)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(imagem_binarizada, cmap='gray')
plt.title('Imagem Binarizada')
plt.axis('off')

plt.show()
