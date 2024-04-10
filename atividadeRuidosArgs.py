# Programa desenvolvido para a disciplina de Visão Computacional.
# Professor: Dr. Hemerson Pistori
#
# Autor: Vinícius Maeda (viniciusmaeda@gmail.com)
#
# Exemplo de uso:
# $ python atividadeRuidosArgs.py -i lenna.png -r gauss -pr 9 -s gauss -ps 5 -b sobel -pb 5

# Bibliotecas utilizadas
from argparse import ArgumentParser
from skimage import io
from skimage import filters, feature
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte, random_noise
import matplotlib.pyplot as plt
import cv2 as cv




# função para aplicar ruído na imagem
def aplicarRuido(img, ruido, parametro):
  if (ruido == 'gauss'):
   # aplica ruído gaussiano na imagem
   imgRuido = random_noise(img, mode = 'gaussian')
  elif (ruido == 'sep'):
   # aplica ruído sal e pimenta na imagem
   imgRuido = random_noise(img, mode = 's&p', amount = parametro/100)
  elif (ruido == 'poisson'):
   # aplica ruído de poisson na imagem
   imgRuido = random_noise(img, mode = 'poisson')

  return imgRuido



def aplicarSuavizacao(img, filtro, ksize):
  if (filtro == 'mean'):
    # aplica um filtro de média para suavizar a imagem
    imgSuavizada = cv.blur(img, (ksize, ksize))
  elif (filtro == 'median'):
    # aplica um filtro de mediana para suavizar a imagem
    imgSuavizada = cv.medianBlur(img_as_ubyte(img), ksize)
  elif (filtro == 'gauss'):
    # aplica um filtro Gaussiano para suavizar a imagem
    imgSuavizada = cv.GaussianBlur(imagemComRuido, (ksize, ksize), cv.BORDER_DEFAULT)

  return imgSuavizada   



def extrairBordas(img, borda, parametro):
  if (borda == 'sobel'):
    imgBordas = filters.sobel(img)
  elif (borda == 'scharr'):
    imgBordas = feature.canny(img, sigma = parametro)
  elif (borda == 'canny'):
    imgBordas = filters.scharr(img)

  return imgBordas



def leituraDosArgumentos():
  # Lê os parâmetros passados na linha de comando
  # Falta implementar as opções para detectores de borda
  parser = ArgumentParser()
  parser.add_argument("-i", "--imagem", default="exemplo.jpg",
                      help="Imagem a ser processada")
  parser.add_argument("-r", "--ruido", default="gauss",
                      help="Tipo de ruído. Pode ser gauss, sep ou poisson")
  parser.add_argument("-pr", "--pruido", default=9,type=int,
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

  # Converte para tons de cinza
  imagemCinza = rgb2gray(imagemOriginal)

  # Aplica o ruído na imagem dependendo do tipo de ruído escolhido
  imagemComRuido = aplicarRuido(imagemCinza, argumentos.ruido, argumentos.pruido)

  # Aplica suavização 
  imagemSuavizada = aplicarSuavizacao(imagemComRuido, argumentos.suavizador, argumentos.psuavizador)

  # Aplica detecção de borda
  imagemBorda = extrairBordas(imagemSuavizada, argumentos.borda, argumentos.pborda)

  # Mostra as imagens com os resultados numa janela
  if argumentos.interface == "sim":

    fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 5),sharex=True, sharey=True)

    ax = axes.ravel()

    ax[0].imshow(imagemOriginal)
    ax[0].axis('off')
    ax[0].set_title('Original')

    ax[1].imshow(imagemComRuido,cmap='gray')
    ax[1].axis('off')
    ax[1].set_title('Com Ruído = ' + str(argumentos.ruido) + ' ' + str(argumentos.pruido))

    ax[2].imshow(imagemSuavizada,cmap='gray')
    ax[2].axis('off')
    ax[2].set_title('Suavizada = ' + str(argumentos.suavizador) + ' ' + str(argumentos.psuavizador))

    ax[3].imshow(imagemBorda,cmap='gray')
    ax[3].axis('off')
    ax[3].set_title('Borda = ' + str(argumentos.borda) + ' ' + str(argumentos.pborda))

    fig.tight_layout()

    fig.canvas.manager.set_window_title('Resultados para imagem '+argumentos.imagem)
    plt.show()

  # Salva no disco as imagens resultantes (falta implementar)
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_ruido.jpg", img_as_ubyte(imagemComRuido))
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_suavizada.jpg", imagemSuavizada)
  io.imsave(pastaImagem + argumentos.imagem.split('.')[0]+"_borda.jpg", img_as_ubyte(imagemBorda))
