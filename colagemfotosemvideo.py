import cv2
import numpy as np

# Defina o endereço das imagens e os tempos de transição
imagens = ["imagem1.jpg", "imagem2.jpg", "imagem3.jpg", "imagem4.jpg", "imagem5.jpg", "imagem6.jpg", "imagem7.jpg", "imagem8.jpg", "imagem9.jpg", "imagem10.jpg"]
tempos = [2, 1, 3, 4, 2, 1, 3, 4, 2, 1]  # tempos em segundos

# Crie uma lista com os quadros do vídeo
frames = []
for i, imagem in enumerate(imagens):
    img = cv2.imread(imagem)
    # Converta a imagem para o formato de quadro de vídeo
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Adicione o quadro à lista de quadros
    for j in range(tempos[i]*30):  # 30 é a taxa de quadros por segundo
        frames.append(frame)

# Crie um objeto de gravação de vídeo
video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame.shape[1], frame.shape[0]))

# Grave os quadros no vídeo
for frame in frames:
    video.write(frame)

# Feche o objeto de gravação de vídeo
video.release()