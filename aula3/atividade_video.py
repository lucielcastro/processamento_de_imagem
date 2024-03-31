import cv2

# Variáveis globais
drawing = False  # Indica se está desenhando
color = (0, 255, 0)  # Cor inicial do rascunho
radius = 5  # Raio do pincel
output_filename = 'aula3/video_com_rascunhos.mp4'  # Nome do arquivo de saída

# Função de callback do mouse para desenhar
def draw(event, x, y, flags, param):
    global drawing, color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(frame, (x, y), radius, color, -1)
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(frame, (x, y), radius, color, -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Carregar o arquivo de vídeo
input_filename = 'aula3/video_original.mp4'
cap = cv2.VideoCapture(input_filename)

# Obter as propriedades do vídeo
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Criar o objeto de gravação de vídeo
out = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Inicializar a janela OpenCV e definir a função de callback do mouse
cv2.namedWindow('Video com Rascunhos')
cv2.setMouseCallback('Video com Rascunhos', draw)

# Loop principal
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Exibir o frame
    cv2.imshow('Video com Rascunhos', frame)

    # Checar por teclas pressionadas
    key = cv2.waitKey(1) & 0xFF

    # Limpar os rascunhos (tecla espaço)
    if key == ord(' '):
        frame = cv2.imread('aula3/video_original.mp4')
        continue

    # Alterar a cor das marcações (tecla 'c')
    elif key == ord('c'):
        color = (0, 0, 255)  # Trocar para vermelho (BGR)

    # Adicionar o frame com as marcações ao vídeo de saída
    out.write(frame)

    # Encerrar o programa se a tecla 'q' for pressionada
    if key == ord('q'):
        break

# Liberar os recursos
cap.release()
out.release()
cv2.destroyAllWindows()