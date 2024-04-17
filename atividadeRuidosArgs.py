# Programa desenvolvido para a disciplina de Visão Computacional.
# Professor: Dr. Hemerson Pistori
# Atividade: Ruídos - Implementar um programa que aplique ruídos, suavize e detecte bordas em uma imagem.
#
# Autor: Vinícius Maeda (viniciusmaeda@gmail.com)
#
# Exemplo de uso:
# $ python atividadeRuidosArgs.py -i lenna.png -r gauss -pr 9 -s gauss -ps 5 -b sobel -pb 5

# Bibliotecas utilizadas
from argparse import ArgumentParser
from skimage import io
from skimage import filters, feature
from skimage.restoration import denoise_tv_bregman
from skimage.util import img_as_ubyte, random_noise
import matplotlib.pyplot as plt
import cv2 as cv




# função para aplicar ruído na imagem
def aplicarRuido(img, ruido, parametro):
  if (ruido == 'gauss'):
    # caso não seja fornecido o parâmetro, será definido como 0.01 (padrão)
    parametro = 0.01 if parametro == None else parametro
    # aplica ruído gaussiano na imagem
    imgRuido = random_noise(img, mode = 'gaussian', var = parametro/100)
  elif (ruido == 'sep'):
    # caso não seja fornecido o parâmetro, será definido como 0.05 (padrão)
    parametro = 0.05 if parametro == None else parametro
    # aplica ruído sal e pimenta na imagem
    imgRuido = random_noise(img, mode = 's&p', amount = parametro/100)
  elif (ruido == 'poisson'):
    # aplica ruído de poisson na imagem
    imgRuido = random_noise(img, mode = 'poisson')

  return imgRuido



def aplicarSuavizacao(img, filtro, parametro):
  if (filtro == 'mean'):
    # aplica um filtro de média para suavizar a imagem
    imgSuavizada = cv.blur(img, (parametro, parametro))
  elif (filtro == 'median'):
    # aplica um filtro de mediana para suavizar a imagem
    imgSuavizada = cv.medianBlur(img_as_ubyte(img), parametro)
  elif (filtro == 'gauss'):
    # aplica um filtro Gaussiano para suavizar a imagem
    imgSuavizada = cv.GaussianBlur(imagemComRuido, (parametro, parametro), cv.BORDER_DEFAULT)
  elif (filtro == 'anisotropico'):
    # aplicar o filtro anisotrópico
    imgSuavizada = denoise_tv_bregman(img, weight = parametro/100)

  return imgSuavizada   



def extrairBordas(img, borda, parametro):
  if (borda == 'sobel'):
    imgBordas = filters.sobel(img)
  elif (borda == 'scharr'):
    imgBordas = filters.scharr(img)
  elif (borda == 'canny'):
    imgBordas = feature.canny(img, sigma = parametro)

  return imgBordas



def leituraDosArgumentos():
  # Lê os parâmetros passados na linha de comando
  # Falta implementar as opções para detectores de borda
  parser = ArgumentParser()
  parser.add_argument("-i", "--imagem", default="exemplo.jpg",
                      help="Imagem a ser processada")
  parser.add_argument("-r", "--ruido", default="gauss",
                      help="Tipo de ruído. Pode ser gauss, sep ou poisson")
  parser.add_argument("-pr", "--pruido", type=int,
                      help="Parâmetro do ruído. Depende do tipo do ruído")
  parser.add_argument("-s", "--suavizador", default="gauss",
                      help="Tipo de suavizador. Pode ser mean, median ou gauss")
  parser.add_argument("-ps", "--psuavizador", default=5,type=int,
                      help="Parâmetro do suavizador. Depende do tipo do ruído")
  parser.add_argument("-b", "--borda", default="sobel",
                      help="Tipo de detector de borda. Pode ser sobel, scharr ou canny")
  parser.add_argument("-pb", "--pborda", default=5,type=int,
                      help="Parâmetro do detector de borda. Depende do tipo de detector")
  parser.add_argument("-ig", "--interface", default="sim",
                      help="Parâmetro do suavizador. Depende do tipo do ruído")

  args = parser.parse_args()

  # Mostra os parâmetros lidos
  print("\n<><><><><><><><><><><><><><><><><><>\n")
  print("Executando sequência com:")
  print("Imagem  = ", args.imagem)
  print("Ruído = ", args.ruido)
  print("Parâmetro do ruído = ", args.pruido)
  print("Suavizador = ", args.suavizador)
  print("Parâmetro do suavizador = ", args.psuavizador)
  print("Detector de bordas = ", args.borda)
  print("Parâmetro da borda = ", args.pborda)
  print("\n<><><><><><><><><><><><><><><><><><>\n")

  return args



if (__name__ == "__main__"):
  # Lê os argumentos passados na linha de comando
  argumentos = leituraDosArgumentos()

  # Caminho da imagem
  pastaImagem = "./assets/"
  # Abre a imagem de entrada
  imagemOriginal = io.imread(pastaImagem + argumentos.imagem)

  # # Converte para tons de cinza
  imagemCinza = cv.cvtColor(imagemOriginal, cv.COLOR_BGR2GRAY)

  # Aplica o ruído na imagem dependendo do tipo de ruído escolhido
  imagemComRuido = aplicarRuido(imagemCinza, argumentos.ruido, argumentos.pruido)

  # Aplica suavização 
  imagemSuavizada = aplicarSuavizacao(imagemComRuido, argumentos.suavizador, argumentos.psuavizador)

  # Aplica detecção de borda
  imagemBorda = extrairBordas(imagemSuavizada, argumentos.borda, argumentos.pborda)

  # Dicionário para traduzir os termos
  dicionarioTermos = {
    'gauss': 'Gaussiano',
    'sep': 'Sal e Pimenta',
    'poisson': 'Poisson',
    'mean': 'Média',
    'median': 'Mediana',
    'anisotropico': 'Anisotrópica',
    'sobel': 'Sobel',
    'scharr': 'Scharr',
    'canny': 'Canny'
  }

  # Mostra as imagens com os resultados numa janela
  if argumentos.interface == "sim":

    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(14, 5), sharex=True, sharey=True)

    ax = axes.ravel()

    ax[0].imshow(imagemOriginal)
    ax[0].axis('off')
    ax[0].set_title('Original')

    ax[1].imshow(imagemComRuido,cmap='gray')
    ax[1].axis('off')
    tituloRuido = 'Ruído = ' + dicionarioTermos[argumentos.ruido]
    tituloRuido += '\nParâmetro: ' + (str(argumentos.pruido) if (argumentos.ruido == 'sep' or argumentos.ruido == 'gauss') else '-')
    ax[1].set_title(tituloRuido)

    ax[2].imshow(imagemSuavizada,cmap='gray')
    ax[2].axis('off')
    ax[2].set_title('Suavização = ' + str(dicionarioTermos[argumentos.suavizador]) + '\nParâmetro: ' + str(argumentos.psuavizador))

    ax[3].imshow(imagemBorda,cmap='gray')
    ax[3].axis('off')
    tituloBorda = 'Borda = ' + str(dicionarioTermos[argumentos.borda])
    tituloBorda += '\nParâmetro: ' + (str(argumentos.pborda) if (argumentos.borda == 'canny') else '-')
    ax[3].set_title(tituloBorda)

    fig.tight_layout()

    fig.canvas.manager.set_window_title('Resultados para imagem '+argumentos.imagem)
    plt.show()

  # Salva no disco as imagens resultantes (falta implementar)
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_ruido.jpg", img_as_ubyte(imagemComRuido))
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_suavizada.jpg", img_as_ubyte(imagemSuavizada))
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_borda.jpg", img_as_ubyte(imagemBorda))