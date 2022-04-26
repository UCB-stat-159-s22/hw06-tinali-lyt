from ligotools import readligo as rl
	
def test_readligo_1():	
	return rl.read_hdf5(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', readstrain=True)
	assert isinstance(shortnameList, list) == True

def test_readligo_2():
	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
	assert isinstance(time, np.ndarray) == True
	
def test_readligo_3():
	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
	return dq2segs(channel=channel_dict, gps_start=time)
	assert isinstance(SegmentList(segList), list) == True
	
def test_readligo_4():
	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
	return getstrain(start=time, stop=time*2, ifo='H1', filelist=None)
	assert isinstance(meta, pd.DataFrame) == True
	
#def test_readligo_5():
#	return rl.loaddata(filename='data/H-H1_LOSC_4_V2-1126259446-32.hdf5', ifo=None, tvec=True, readstrain=True)
#	return dq_channel_to_seglist(channel=channel_dict, fs=4096)
#	assert isinstance(segment_list, list) == True