# Programa para aplicar Ruídos, Suavizações e Detecção de Bordas em imagens
## Autor: Vinícius de Araújo Maeda

## Resumo
Programa desenvolvido para uma atividade da disciplina de Visão Computacional (turma 2024-1) ofertada pelo professor Dr. Hemerson Pistori. A disciplina é oferecida para os estudantes de graduação e pós-graduação da Universidade Católica Dom Bosco.

O programa tem por objetivo aplicar ruídos, filtros de suavizações e detecções de bordas em imagens. Para cada uma delas, foram implementadas 3 funcionalidades, da seguinte forma:
Ruído
- Gauss
- São e pimenta
- Poisson

Suavização
- Média
- Mediana
- Gauss

Detecção de borda
- Sobel
- Scharr
- Canny

## Versões das bibliotecas
- Argparse: 1.1
- Skimage: 0.22.0
- Matplotlib: 3.8.3
- OpenCV: 4.9.0

## Execução do programa
Para executar o programa, deve-se salvar uma imagem na pasta assets/ e utilizar o comando abaixo.

$ python atividadeRuidosArgs.py -i imagem.png -r gauss -pr 9 -s gauss -ps 5 -b sobel -pb 5 -ig sim

O programa espera por 8 (oito) parâmetros, sendo eles:
- '-i' - o nome da imagem (string), incluindo a extensão do arquivo, exemplo: imagem.jpg
- '-r' - o ruído aplicado (string), podendo ser: 'gauss', 'sep' e 'poison'
- '-pr' - parâmetro (número inteiro) para utilizar no ruído. O valor default é 9
- '-s' - o filtro de suavização (string), podendo ser: 'mean', 'median' e 'gauss'
- '-ps' - parâmetro (número inteiro) para utilizar na suavização. O valor default é 5
- '-b' - o filtro para a detecção da borda (string), podendo ser: 'sobel', 'scharr' e 'canny'
- '-pb' - parâmetro (número inteiro) para utilizar na detecção da borda. O valor default é 5
- '-ig' - caso não queira mostrar os resultados na janela, basta fornecer qualquer valor (string) para este parâmetro. O valor default é 'sim".

## Resultado esperado
Ao executar o programa através do terminal, o programa irá realizar as funcionalidades sobre a imagem. O resultado será apresentado na janela, caso o parâmetro '-ig' for igual a 'sim'. Na janela mostrará 4 imagens, a imagem original, com ruído, suavizada e com as bordas detectadas, respectivamente.

O resultado das 3 operações serão armazenadas na mesma pasta da imagem original.
