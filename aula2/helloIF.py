# import cv2
# # import 'logo'
# img = cv2.imread('logo-if.jpg')

# #TODO processar
# # print(img)

# cv2.imshow('Logo IF',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2

# Carregar a imagem
img = cv2.imread('aula2/logo-if.jpg')

# Verificar se a imagem foi carregada com sucesso
if img is None:
    print("Erro: Imagem não carregada")
else:
    # Exibir a imagem
    cv2.imshow('Logo IF', img)
    # Aguardar pressionamento de qualquer tecla
    cv2.waitKey(0)
    # Fechar todas as janelas do OpenCV
    cv2.destroyAllWindows()
