import cv2
import numpy as np

# Função para realizar a rotação da imagem em torno de um ponto específico
def rotate_image(image, angle, center):
    # Obter a matriz de rotação
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Aplicar a rotação na imagem
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

# Função de callback do mouse para obter as coordenadas do ponto de rotação
def get_rotation_point(event, x, y, flags, param):
    global rotation_point
    if event == cv2.EVENT_LBUTTONDOWN:
        rotation_point = (x, y)

# Carregar a imagem
image = cv2.imread('aula6/if-cxs.jpg')

# Definir o ponto de rotação como o centro da imagem (ponto padrão)
rotation_point = (image.shape[1] // 2, image.shape[0] // 2)

# Criar a janela e definir a função de callback do mouse
cv2.namedWindow('Rotated Image')
cv2.setMouseCallback('Rotated Image', get_rotation_point)

# Loop principal
while True:
    # Copiar a imagem original para evitar alterações permanentes
    rotated_image = image.copy()

    # Exibir a imagem rotacionada
    cv2.imshow('Rotated Image', rotated_image)

    # Aguardar a entrada do usuário
    key = cv2.waitKey(1)

    # Rotacionar a imagem quando a tecla 'r' for pressionada
    if key == ord('r'):
        # Calcular o ângulo de rotação (por exemplo, 45 graus)
        angle = 45
        # Realizar a rotação da imagem em torno do ponto definido pelo mouse
        rotated_image = rotate_image(image, angle, rotation_point)

    # Sair do loop se a tecla 'q' for pressionada
    elif key == ord('q'):
        break

# Fechar todas as janelas abertas
cv2.destroyAllWindows()
