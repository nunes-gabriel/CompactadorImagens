# Compactador de Imagens

O seguinte código tem como finalidade compactar um conjunto de imagens salvas
em uma determinada pasta da máquina, buscando diminuir o tamanho do arquivo
destas imagens até um valor determinado pelo usuário. Para que o código funcione
corretamente é necessário alterar duas variáveis definidas ao início do arquivo *main.py*,
sendo elas:

* **pasta_input** -> Uma string com o caminho para a pasta de origem de onde serão retiradas
as imagens para compactação.
* **pasta_output** -> Uma string com o caminho para a pasta de saída onde serão salvas as
imagens já compactadas.

Outras duas variáveis podem ainda ser alteradas manualmente, ou até mesmo ser
transformadas em *inputs*. Sendo elas:

* **novo_tamanho** -> Tamanho de saída das imagens compactadas em kilobytes(kb) - vale ressaltar
que há uma pequena margem de erro de 10kb, isto é, o tamanho das imagens ficará entre o novo tamanho
e o novo tamanho - 10kb.
* **fator** -> Fator de diminuição da imagem, quantos pixels serão diminuidos a cada loop
do código. Quanto menor for este valor mais preciso será o tamanho de saída da imagem, porém, mais lento
será a execução do código.
