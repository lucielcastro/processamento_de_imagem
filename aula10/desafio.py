import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('aula9/ifma-caxias.jpg')

# Converter a imagem para tons de cinza
imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Criar uma máscara com os objetos a serem removidos (pode ser manualmente ou usando detecção de objetos)
mask = np.zeros_like(imagem_gray)
mask[200:300, 200:300] = 255  # Exemplo: região retangular de objetos a serem removidos

# Aplicar o algoritmo de inpainting
imagem_sem_objetos = cv2.inpaint(imagem, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Exibir as imagens original e com objetos removidos
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(imagem_sem_objetos, cv2.COLOR_BGR2RGB))
plt.title('Imagem sem Objetos')
plt.axis('off')

plt.show()
