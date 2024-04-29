import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('aula9/clown.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar a Transformada de Fourier
fourier = np.fft.fft2(imagem)
fourier_shifted = np.fft.fftshift(fourier)

# Criar o primeiro filtro passa-baixa (ideal)
rows, cols = imagem.shape
crow, ccol = rows // 2, cols // 2
d1 = 30  # raio do primeiro filtro
filtro_passa_baixa_1 = np.zeros((rows, cols), np.uint8)
cv2.circle(filtro_passa_baixa_1, (ccol, crow), d1, 255, -1)

# Aplicar o primeiro filtro na frequência (multiplicação na frequência)
fourier_filt_1 = fourier_shifted * filtro_passa_baixa_1

# Inverter a Transformada de Fourier
fourier_invert_1 = np.fft.ifftshift(fourier_filt_1)
imagem_filtrada_1 = np.fft.ifft2(fourier_invert_1)
imagem_filtrada_1 = np.abs(imagem_filtrada_1)

# Criar o segundo filtro passa-baixa (ideal)
d2 = 10  # raio do segundo filtro
filtro_passa_baixa_2 = np.zeros((rows, cols), np.uint8)
cv2.circle(filtro_passa_baixa_2, (ccol, crow), d2, 255, -1)

# Aplicar o segundo filtro na frequência (multiplicação na frequência)
fourier_filt_2 = fourier_filt_1 * filtro_passa_baixa_2

# Inverter a Transformada de Fourier
fourier_invert_2 = np.fft.ifftshift(fourier_filt_2)
imagem_filtrada_2 = np.fft.ifft2(fourier_invert_2)
imagem_filtrada_2 = np.abs(imagem_filtrada_2)

# Exibir as imagens original e filtrada
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(imagem_filtrada_1, cmap='gray')
plt.title('Imagem Filtrada - 1ª Camada')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(imagem_filtrada_2, cmap='gray')
plt.title('Imagem Filtrada - 2ª Camada')
plt.axis('off')

plt.show()
