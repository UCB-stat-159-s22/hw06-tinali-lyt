#whiten, write_wavfile, reqshift
import numpy as np
import os
import fnmatch
from scipy.io import wavfile
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def whiten(strain, interp_psd, dt):
    Nt = len(strain)
    freqs = np.fft.rfftfreq(Nt, dt)
    freqs1 = np.linspace(0,2048.,Nt/2+1)

    # whitening: transform to freq domain, divide by asd, then transform back, 
    # taking care to get normalization right.
    hf = np.fft.rfft(strain)
    norm = 1./np.sqrt(1./(dt*2))
    white_hf = hf / np.sqrt(interp_psd(freqs)) * norm
    white_ht = np.fft.irfft(white_hf, n=Nt)
    return white_ht

def write_wavfile(filename,fs,data):
    d = np.int16(data/np.max(np.abs(data)) * 32767 * 0.9)
    wavfile.write(filename,int(fs), d)
	

def reqshift(data,fshift=100,sample_rate=4096):
    """Frequency shift the signal by constant
    """
    x = np.fft.rfft(data)
    T = len(data)/float(sample_rate)
    df = 1.0/T
    nbins = int(fshift/df)
    # print T,df,nbins,x.real.shape
    y = np.roll(x.real,nbins) + 1j*np.roll(x.imag,nbins)
    y[0:nbins]=0.
    z = np.fft.irfft(y)
    return z

def plotgraph(subplot, time, SNR, pcolor, label, grid, xlabel, ylabel, legend, title=False, xlim=False, savefig=False, figsize=False):
	if figsize != False:
		plt.figure(figsize=figsize)
	plt.subplot(subplot[0],subplot[1],subplot[2])
	plt.plot(time, SNR, pcolor,label=label)
	plt.grid(grid)
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	if xlim != False:
		plt.xlim(xlim)
	plt.legend(loc=legend)
	if title != False:
		plt.title(title)
	if savefig != False:
		plt.savefig(savefig)