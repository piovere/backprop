# LIBS Data Generator

# import all needed modules
import numpy as np
import matplotlib.pyplot as plt

# set the number of lines
lines = [250,398,420,455,534,542,698] #nm
fwhm = [1,1,8,3,3,2,4]
intensity = [1,2,5,0.8,4,8,10,4]

# set data length
# start with beginning and ending wavelengths
wl_start = 400
wl_end = 800
bins = int((wl_end-wl_start)/0.001)

# setup a blank array for channel numbers
data = np.linspace(wl_start,wl_end,num=bins)

# set mean, std, and number of samples to draw from
mu, sigma, samples = lines[0],fwhm[0], 10**6
# initialize a distribution array based on number of peaks
dist = np.zeros(samples)
# create a gaussian
for i in range(0,len(lines)):
    gauss = np.random.normal(lines[i],fwhm[i],int(samples*intensity[i]))
    dist = np.concatenate((dist,gauss))

spec,bin_edges = np.histogram(dist,bins=bins,range=(wl_start,wl_end))

outarray = np.hstack((spec,bin_edges))

np.savetxt("outfile.csv",outarray,delimiter=",")

# Create the bins and histogram
plt.hist(dist, 1000, normed=True)
plt.xlim([200,800])

# Plot the distribution curve
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#     np.exp( - (bins - mu)**2 / (2 * sigma**2) ),       linewidth=3, color='y')
plt.show()