import cv2
import matplotlib.pyplot as plt

# Carregar a imagem em tons de cinza
imagem = cv2.imread('aula7/ifcx.jpg', cv2.IMREAD_GRAYSCALE)

# Calcular o histograma
histograma = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# Exibir o histograma
plt.figure()
plt.plot(histograma, color='black')
plt.xlabel('Níveis de Cinza')
plt.ylabel('Número de Pixels')
plt.title('Histograma da Imagem em Tons de Cinza')
plt.xlim([0, 256])
plt.show()
