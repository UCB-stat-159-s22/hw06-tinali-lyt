from ligotools import utils
from ligotools import readligo as rl
	
def test_utils_1():	
	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
	return getstrain(start=time, stop=time*2, ifo='H1', filelist=None)
	return whiten(dt, strain=m_strain, interp_psd=psd_H1)
	assert isinstance(white_ht, np.ndarray) == True
	
def test_utils_2():	
	return utils.write_wavfile(filename='audio/GW150914_H1_whitenbp.wav',fs=4096,data=[0.49313468, 0.39550715, 0.24207313, -1.23917656, -0.67216917, -0.04115013])
	assert isinstance(d, np.ndarray) == True
	
def test_utils_3():	
	return utils.reqshift(data=[0.49313468, 0.39550715, 0.24207313, -1.23917656, -0.67216917, -0.04115013],fshift=100,sample_rate=4096)
	assert isinstance(z, np.ndarray) == True
	
def test_utils_4():	
	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
	return utils.plotgraph(figsize=(10,8), subplot=[2,1,1], time=time-timemax, SNR=SNR, pcolor=pcolor, label=det+' SNR(t)', 
                        grid='on', xlabel='Time since {0:.4f}'.format(timemax), ylabel='SNR', 
                        legend='upper left', title=det+' matched filter SNR around event')
	assert (SNR >= 0) == True