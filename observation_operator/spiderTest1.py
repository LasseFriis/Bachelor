import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import glob
import numpy as np
import sys, os
import netCDF4 as nc
import xarray as xr
from IPython import display

from mpl_toolkits.basemap import Basemap
from pyresample import kd_tree,geometry
from pyresample import load_area, save_quicklook, SwathDefinition

directory = '../Data/'
files = glob.glob(directory + 'iceh.*.nc')

ds = nc.Dataset(files[0])

lat = ds.variables["TLAT"]
lon = ds.variables["TLON"]



Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

freqs = np.array([7,10,18,37,89])
ice_type = 'firstyear'
iceConc = 1


TbV,TbH, smrtV,smrtH = [np.empty([len(files),len(freqs),888, 781]) for _ in range(4)]
# load numpy array from csv file
from numpy import loadtxt
# load array
smrtV[0,0,:,:] = loadtxt(directory + 'smrtRunV.csv', delimiter=',')
TbV[0,0,:,:] = loadtxt(directory + 'TieRunV.csv', delimiter=',')
smrtH[0,0,:,:] = loadtxt(directory + 'smrtRunH.csv', delimiter=',')
TbH[0,0,:,:] = loadtxt(directory + 'TieRunH.csv', delimiter=',')

mins = 250
maks = 350

d = smrtV[0,0,mins:maks,mins:maks]


lats = np.ma.array(lat[mins:maks,mins:maks], mask=d < .2)
lons = np.ma.array(lon[mins:maks,mins:maks], mask=d < .2)
d = np.ma.array(d, mask=d < .2)



plt.contourf(lats,lons,d)
plt.colorbar()
plt.show()
