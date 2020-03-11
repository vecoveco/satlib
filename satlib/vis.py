import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import glob
import wradlib as wrl
from osgeo import osr

def plot_gprof_IWP(gprof_path):
    """
    gprof_path ::: path to gprof data
    
    """
    
    gpmdprs = h5py.File(pfad, 'r')
    gprof_lat = np.array(gpmdprs['S1']['Latitude'])
    gprof_lon = np.array(gpmdprs['S1']['Longitude'])

    gprof_iwp = np.array(gpmdprs['S1']['iceWaterPath'])
    
    # BoxPol Limits
    xlim = np.array([6.4, 8.1])
    ylim = np.array([49.9, 51.4])

    

    plt.figure(figsize=(10,8))
    plt.pcolormesh(gprof_lon, gprof_lat, gprof_iwp,
                   vmin=0, vmax=4,
                   cmap=mpl.cm.get_cmap('jet', 10))
    
    cbar = plt.colorbar()
    cbar.set_label(r'Ice Water Path $kg/m^2$', fontsize=20)
    cbar.ax.tick_params(labelsize=20)
    plt.scatter(7.071663, 50.73052,c='magenta',s=50, marker='+', label='BoXPol')
    plt.legend(fontsize=20)
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.xlabel('Longitude in deg', fontsize=20)
    plt.ylabel('Latitude in deg', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.show()
    
