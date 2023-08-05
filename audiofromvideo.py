from moviepy.video.io.VideoFileClip import VideoFileClip

# recebe o endereço do vídeo
endereco_video = input("Digite o endereço do vídeo: ")

# cria um objeto do tipo VideoFileClip
clip = VideoFileClip(endereco_video)

# extrai o áudio do vídeo
audio = clip.audio

# salva o áudio em um arquivo .mp3
audio.write_audiofile("audio.mp3")

# fecha o objeto VideoFileClip
clip.close()