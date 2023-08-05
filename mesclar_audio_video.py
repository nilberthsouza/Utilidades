from moviepy.editor import VideoFileClip, AudioFileClip
from datetime import datetime, timedelta

video_file = "video.mp4"
audio_file = "audio.mp3"

video = VideoFileClip(video_file)
audio = AudioFileClip(audio_file)

tempo = input("Digite o tempo em que o áudio deve começar a ser mesclado no formato MM:SS: ")
tempo = datetime.strptime(tempo, "%M:%S")
tempo_total = datetime.utcfromtimestamp(audio.duration).strftime("%M:%S")
print("Duração total do áudio: ", tempo_total)

tempo_audio = timedelta(minutes=tempo.minute, seconds=tempo.second)
print("Áudio começará a ser mesclado no tempo: ", tempo_audio)

audio_recortado = audio.subclip(tempo_audio)

video_com_audio = video.set_audio(audio_recortado)

video_com_audio.write_videofile("video_com_audio.mp4")
