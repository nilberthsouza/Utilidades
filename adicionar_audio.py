from moviepy.video.io.VideoFileClip import VideoFileClip

endereco_video = input("Digite o endereço do vídeo: ")

clip = VideoFileClip(endereco_video)

audio = clip.audio

audio.write_audiofile("audio.mp3")

clip.close()
