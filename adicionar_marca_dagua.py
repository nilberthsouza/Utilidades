from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# recebe o endereço do vídeo
endereco_video = input("Digite o endereço do vídeo: ")

# carrega o vídeo
video = VideoFileClip(endereco_video)

# pede ao usuário o texto da marca d'água
texto = input("Digite o texto da marca d'água: ")

# calcula a largura e a altura da marca d'água
largura, altura = video.size
tamanho_marca_dagua = 0.05 # 5% da área total do vídeo
largura_marca_dagua = int(largura * tamanho_marca_dagua)
altura_marca_dagua = int(altura * tamanho_marca_dagua)

# cria o clip de texto para a marca d'água
clip_texto = TextClip(texto, fontsize=50, color='white', font='Arial', bg_color='transparent')

# posiciona o clip de texto no canto esquerdo da tela
clip_texto = clip_texto.set_pos(('left', 'top'))

# redimensiona o clip de texto para a largura e a altura da marca d'água
clip_texto = clip_texto.resize((largura_marca_dagua, altura_marca_dagua))

# cria o clip de marca d'água composto pelo vídeo original e pelo clip de texto
clip_marca_dagua = CompositeVideoClip([video, clip_texto])

# salva o vídeo com a marca d'água em um novo arquivo
endereco_saida = "video_com_marca_dagua.mp4"
clip_marca_dagua.write_videofile(endereco_saida, audio_codec='aac')

# fecha o objeto VideoFileClip
video.close()
