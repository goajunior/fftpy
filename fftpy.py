'fourier analysis using scipy modules'

import argparse
import numpy
import scipy
import matplotlib
import subprocess

def main():

    # parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--order', type=int, default=2, help='number of points')
    # parser.add_argument('--guess', type=float, default=1.0, help='initial guess')
    # parser.add_argument('--output', default='plot.png', help='output image file')
    args = parser.parse_args()

    np = args.order

    # o mathematica usara o script teste e gerara um arquivo com a funcao a ser transformada
    # o arquivo ascii data.txt sera produzido com os pontos (x,y) da funcao descrita em teste.m
    subprocess.check_output(['MathematicaScript', '-script', 'teste.m', str(np)])

    # conta a quantidade de samplings do sinal
    fdata   = open('data.txt', 'r')
    nlinhas = 0

    for i in fdata:
        nlinhas = nlinhas + 1

    data = numpy.zeros((nlinhas,2), float)

    count = 0
    fdata.seek(0) # o ponteiro do arquivo precisa ser recolocado no inicio

    # cada linha é lida como uma cadeia de caracteres
    for linha in fdata:
        linha         = linha.strip() #as linhas em branco são removidos
        colunas       = linha.split() #os numeros sao separados levando em conta o espaco em branco entre eles
        data[count,0] = float(colunas[0])
        data[count,1] = float(colunas[1])
        count         = count + 1

    print(data)

if __name__ == '__main__':
    main()
