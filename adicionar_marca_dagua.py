from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

endereco_video = input("Digite o endereço do vídeo: ")

video = VideoFileClip(endereco_video)

texto = input("Digite o texto da marca d'água: ")

largura, altura = video.size
tamanho_marca_dagua = 0.05 # 5% da área total do vídeo
largura_marca_dagua = int(largura * tamanho_marca_dagua)
altura_marca_dagua = int(altura * tamanho_marca_dagua)

clip_texto = TextClip(texto, fontsize=50, color='white', font='Arial', bg_color='transparent')
clip_texto = clip_texto.set_pos(('left', 'top'))
clip_texto = clip_texto.resize((largura_marca_dagua, altura_marca_dagua))
clip_marca_dagua = CompositeVideoClip([video, clip_texto])

endereco_saida = "video_com_marca_dagua.mp4"
clip_marca_dagua.write_videofile(endereco_saida, audio_codec='aac')

video.close()
