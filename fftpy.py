'fourier analysis using scipy modules'

import argparse
import numpy
import scipy
import matplotlib
import subprocess

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument('--order', type=int, default=2, help='number of points')
    # parser.add_argument('--guess', type=float, default=1.0, help='initial guess')
    # parser.add_argument('--output', default='plot.png', help='output image file')
    args = parser.parse_args()

    np = args.order

    subprocess.check_output(['MathematicaScript','-script','teste.m'])

    t = numpy.linspace(0, 50e-6, num=25)
    print(t)

if __name__ == '__main__':
    main()
