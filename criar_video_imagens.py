import cv2
import numpy as np

imagens = ["imagem1.jpg", "imagem2.jpg", "imagem3.jpg", "imagem4.jpg", "imagem5.jpg", "imagem6.jpg", "imagem7.jpg", "imagem8.jpg", "imagem9.jpg", "imagem10.jpg"]
tempos = [2, 1, 3, 4, 2, 1, 3, 4, 2, 1]  # tempos em segundos

frames = []
for i, imagem in enumerate(imagens):
    img = cv2.imread(imagem)
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    for j in range(tempos[i]*30):  # 30 é a taxa de quadros por segundo
        frames.append(frame)

video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame.shape[1], frame.shape[0]))

for frame in frames:
    video.write(frame)

video.release()
