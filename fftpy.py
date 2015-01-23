'fourier analysis using scipy modules'

import argparse
import numpy
import scipy
import scipy.fftpack
import matplotlib.pyplot as plt
import subprocess

def fftscipy(np, data):

    FFT = abs(scipy.fft(data[:,1]))
    freqs = scipy.fftpack.fftfreq(np, data[1,0] - data[0,0])

    plt.subplot(2, 1, 1)
    plt.plot(data[:,0], data[:,1], '-')
    plt.title('Análise de Fourier')
    plt.ylabel('Sinal no tempo')

    plt.subplot(2, 1, 2)
    plt.plot(freqs[0:np/2], (2/np)*FFT[0:np/2], '-')
    plt.ylabel('Sinal no dom. da frequência')
    plt.grid()
    plt.savefig('plot.png', dpi=512)
    plt.show()

    return

def main():

    # parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--script', action='store_true')
    parser.add_argument('--order', type=int,  default=2, help='number of points')
    parser.add_argument('--data', default='data.txt', help='initial guess')
    args = parser.parse_args()


    # o mathematica usara o script teste e gerara um arquivo com a funcao a ser transformada
    # o arquivo ascii data.txt sera produzido com os pontos (x,y) da funcao descrita em teste.m
    if args.script:
        np = args.order
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

    fftscipy(nlinhas, data)

if __name__ == '__main__':
    main()
