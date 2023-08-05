from moviepy.editor import VideoFileClip, AudioFileClip
from datetime import datetime, timedelta

# Defina o arquivo de vídeo e o arquivo de áudio
video_file = "video.mp4"
audio_file = "audio.mp3"

# Carregue o arquivo de vídeo e extraia o áudio
video = VideoFileClip(video_file)
audio = AudioFileClip(audio_file)

# Peça ao usuário para digitar o tempo a partir do qual o áudio deve ser mesclado com o vídeo
tempo = input("Digite o tempo em que o áudio deve começar a ser mesclado no formato MM:SS: ")
tempo = datetime.strptime(tempo, "%M:%S")
tempo_total = datetime.utcfromtimestamp(audio.duration).strftime("%M:%S")
print("Duração total do áudio: ", tempo_total)

# Calcule o tempo em que o áudio deve começar a ser mesclado com o vídeo
tempo_audio = timedelta(minutes=tempo.minute, seconds=tempo.second)
print("Áudio começará a ser mesclado no tempo: ", tempo_audio)

# Extraia o áudio a partir do tempo especificado pelo usuário
audio_recortado = audio.subclip(tempo_audio)

# Adicione o áudio ao vídeo a partir do tempo especificado
video_com_audio = video.set_audio(audio_recortado)

# Salve o vídeo com o áudio mesclado
video_com_audio.write_videofile("video_com_audio.mp4")