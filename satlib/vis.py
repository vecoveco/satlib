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
    
    gpmdprs = h5py.File(gprof_path, 'r')
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
    
def plot_dpr_PWI(dpr_path):
    """
    dpr_path ::: path to DPR data
    
    """
    
    gpmdprs = h5py.File(dpr_path, 'r')
    gpm_lat = np.array(gpmdprs['NS']['Latitude'])
    gpm_lon = np.array(gpmdprs['NS']['Longitude'])

    gpm_pwi = np.array(gpmdprs['NS']['SLV']['precipWaterIntegrated']) # in g/m^2
    print(gpm_pwi.shape)
    # Missing Values
    gpm_pwi[gpm_pwi==-9999.9]=np.nan
    
    # 0 = liquid, sum of liquid water phase >=200
    # 1 = solid, sum of non liquid water phase < 200
    gpm_lwi = gpm_pwi[:,:,0]
    gpm_swi = gpm_pwi[:,:,1]
    
    
    print (gpm_lwi.shape, gpm_lat.shape)
    
    # BoxPol Limits
    xlim = np.array([6.4, 8.1])
    ylim = np.array([49.9, 51.4])

    # g -> lg
    kg = 1000
    
    plt.figure(figsize=(14,6))
    plt.subplot(1,2,1)
    plt.pcolormesh(gpm_lon, gpm_lat, gpm_lwi/kg,
                   vmin=0, vmax=2,
                   cmap=mpl.cm.get_cmap('jet', 10))
    
    cbar = plt.colorbar()
    cbar.set_label(r'Liquid Water Integrated $g/m^2$', fontsize=20)
    cbar.ax.tick_params(labelsize=20)
    plt.scatter(7.071663, 50.73052,c='magenta',s=50, marker='+', label='BoXPol')
    plt.legend(fontsize=20)
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.xlabel('Longitude in deg', fontsize=20)
    plt.ylabel('Latitude in deg', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    
    plt.subplot(1,2,2)
    plt.pcolormesh(gpm_lon, gpm_lat, gpm_swi/kg,
                   vmin=0, vmax=4,
                   cmap=mpl.cm.get_cmap('jet', 10))
    
    cbar = plt.colorbar()
    cbar.set_label(r'Non Liquid Water Integrated $g/m^2$', fontsize=20)
    cbar.ax.tick_params(labelsize=20)
    plt.scatter(7.071663, 50.73052,c='magenta',s=50, marker='+', label='BoXPol')
    plt.legend(fontsize=20)
    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])
    plt.xlabel('Longitude in deg', fontsize=20)
    plt.ylabel('Latitude in deg', fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    
    plt.tight_layout()
    plt.show()
