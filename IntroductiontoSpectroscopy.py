#GROUP MEMBERS: LUKA VUJEVA, DONG UK KIM, PIERCE BALKO, CAMERON STOCKTON

#the necessary libraries were imported
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import find_peaks




#the data was imported for each data group
sun_spectra = np.loadtxt('sunspectra.txt', skiprows = 17)
bb_spectra = np.loadtxt('BBspectra.txt', skiprows = 17)
neon_spectra = np.loadtxt('Nespectra.txt', skiprows = 17)
h_spectra = np.loadtxt('Hspectra.txt', skiprows = 17)

###############################################################################
############################## PROBLEM 1 ######################################
###############################################################################

#the data was spliced into its values of measurement number and intensity

sun_count = np.ndarray.flatten(sun_spectra[:, 0:1])
sun_intensity = np.ndarray.flatten(sun_spectra[:, 1:2])

bb_count = np.ndarray.flatten(bb_spectra[:, 0:1])
bb_intensity = np.ndarray.flatten(bb_spectra[:, 1:2])

neon_count = np.ndarray.flatten(neon_spectra[:, 0:1])
neon_intensity = np.ndarray.flatten(neon_spectra[:, 1:2])

h_count = np.ndarray.flatten(h_spectra[:, 0:1])
h_intensity = np.ndarray.flatten(h_spectra[:, 1:2])


################################# SUN #########################################

#The sun spectrum data was plotted
plt.plot(sun_count, sun_intensity, linestyle = '-', color = 'red')
plt.xlabel('Count')
plt.ylabel('Intensity')
plt.title('Sun Spectrum')
plt.savefig('sun_spectra.pdf')
plt.show()

############################## BLACK BODY #####################################

#The black body spectrum data was plotted
plt.plot(bb_count, bb_intensity, linestyle = '-', color = 'red')
plt.xlabel('Count')
plt.ylabel('Intensity')
plt.title('Black Body Spectrum')
plt.savefig('bb_spectra.pdf')
plt.show()

################################# NEON ########################################

#the pixel at which the main neon peak is was found, then matched to the peak wavelength found in data
#neon_max = np.argmax(neon_intensity[0:1300])
#peak_neon = neon_count[neon_max]
#print(peak_neon)
#neon_wavelengths = peak_neon / 585.25

#The neon spectrum data was plotted

plt.plot(neon_count, np.log(neon_intensity), linestyle = '-', color = 'red')

plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Neon Spectrum')
plt.savefig('neon_spectra.pdf')
plt.show()

############################### HYDROGEN ######################################

#the pixel at which the main neon peak is was found, then matched to the peak wavelength found in data
#h_max = np.argmax(h_intensity)
#peak_h = h_count[h_max]

h_peaks = find_peaks(h_intensity, height = 1000)
#h_wavelengths = peak_h / 656


#The hydrogen spectrum data was plotted
#plt.plot(h_count / h_wavelengths,np.log(h_intensity), linestyle = '-', color = 'red', label = 'count data')
plt.xlim(400)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Hydrogen Spectrum')
plt.savefig('h_spectra.pdf')
plt.legend()
plt.show()



