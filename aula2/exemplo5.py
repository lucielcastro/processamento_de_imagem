import cv2

# Carregar a imagem
img = cv2.imread('aula2/logo-if.jpg')

# Converter a imagem de BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Converter a imagem de BGR para RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Exibir a imagem convertida para HSV
cv2.imshow('HSV', hsv)

# Exibir a imagem convertida para RGB
cv2.imshow('RGB', rgb)

# Aguardar até que uma tecla seja pressionada
cv2.waitKey(0)

# Fechar todas as janelas abertas pelo OpenCV
cv2.destroyAllWindows()
