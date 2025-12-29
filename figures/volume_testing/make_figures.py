# Imports from the python standard library:
import csv

# Third party imports, installable via pip:
import numpy as np
import matplotlib.pyplot as plt

# Plot functions:
def plot_fixed_volumes(filename, verbose=True, show=True):
    # import data and get variables:
    data_rows = np.genfromtxt(filename + '.csv', delimiter=',', names=True)
    flow_rate_ulps = data_rows['flow_rate_ulps'][0]     # fixed flow rate
    target_volume_ul = data_rows['target_volume_ul'][0] # fixed volume
    net_weight_mg = data_rows['net_weight_mg']          # different weights
    foldername = filename.split('\\')[0]
    # calculate stats:
    volume_ul = net_weight_mg * 1 # 1mg of water = 1ul
    n = len(volume_ul)
    hist_bins = int(round(np.sqrt(n)))
    mean = np.mean(volume_ul)
    std = np.std(volume_ul)
    rb = 100 * ((mean - target_volume_ul) / target_volume_ul)
    cv = 100 * std / mean
    # optionally print:
    if verbose:
        print('Plotting fixed volumes: %s'%foldername)
        print('n = %i'%n)
        print('hist_bins = %i'%hist_bins)
        print('mean (ul) = %0.2f'%mean)
        print('std (ul) = %0.2f'%std)
        print('rb (%%) = %0.2f'%rb)
        print('cv (%%) = %0.2f'%cv)
        print()
    # plot:
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_title('Fixed volumes: %s \n'%foldername +
                 'RB=%0.2f%%, CV=%0.2f%%, n=%i'%(rb, cv, n))
    ax.set_xlabel('Volume (ul)')
    ax.set_xlim(9, 11.5)
    ax.set_ylabel('Frequency')

    ax.hist(volume_ul, bins=hist_bins, color='skyblue', edgecolor='black')
    ax.axvline(target_volume_ul, label='target = %0.2f'%target_volume_ul,
               color='black', linestyle='--')
    ax.axvline(mean, label='mean = %0.2f'%mean,
               color='red', linestyle='-.')
    ax.axvline(mean + 3 * std, label='+3STD = %0.2f'%(mean + 3 * std),
               color='green', linestyle=':')
    ax.axvline(mean - 3 * std, label='-3STD = %0.2f'%(mean - 3 * std),
               color='green', linestyle=':')

    ax.legend(framealpha=1.0)
    plt.savefig(foldername + '_fixed_volumes.png')
    if show:
        plt.show()

def plot_random_volumes(filename, verbose=True, show=True):
    # import data and get variables:
    data_rows = np.genfromtxt(filename + '.csv', delimiter=',', names=True)
    flow_rate_ulps = data_rows['flow_rate_ulps'][0]
    target_volume_ul = data_rows['target_volume_ul']
    net_weight_mg = data_rows['net_weight_mg']
    foldername = filename.split('\\')[0]
    # calculate stats:
    volume_ul = net_weight_mg * 1 # 1mg of water = 1ul
    n = len(volume_ul)
    error = 100 * ((volume_ul - target_volume_ul) / target_volume_ul)
    mean_error = np.mean(error)
    max_error = np.max(error)
    # optionally print:
    if verbose:
        print('Plotting random volumes: %s'%foldername)
        print('n=%i'%n)
        print('mean error (%%) =%0.2f'%mean_error)
        print('max error (%%) =%0.2f'%max_error)
        print()
    # plot:
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.set_title('Random volumes: %s \n'%foldername + 
                  'mean error=%0.2f%%, max error=%0.2f%%, n=%i'%(
                      mean_error, max_error, n))
    ax.set_xlabel('Volume (ul)')
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 110, 10))
    ax.set_ylabel('Error (%)')

    ax.scatter(target_volume_ul, error)
    ax.axhline(mean_error, label='Mean = %0.2f'%mean_error,
               color='red', linestyle='-.')

    ax.legend(framealpha=1.0)
    plt.savefig(foldername + '_random_volumes.png')
    if show:
        plt.show()

filenames_fixed_volumes = (
    'idex_1568XL_PEEK_tube_media\\2025-09-29_09-43-47_volume_vs_weight',
    'idex_1568XL_PEEK_tube_water\\2025-09-26_10-14-30_volume_vs_weight',
    'zues_SWTT-30-C_PTFE_tube_media\\2025-10-08_14-31-59_volume_vs_weight',
    'zues_SWTT-30-C_PTFE_tube_water\\2025-10-07_15-53-39_volume_vs_weight',
    )

for f in filenames_fixed_volumes:
    plot_fixed_volumes(f, verbose=True, show=False)

filenames_random_volumes = (
    'idex_1568XL_PEEK_tube_media\\2025-09-29_12-41-10_volume_vs_weight',
    'zues_SWTT-30-C_PTFE_tube_media\\2025-10-08_14-45-18_volume_vs_weight',
    'zues_SWTT-30-C_PTFE_tube_water\\2025-10-07_16-03-13_volume_vs_weight',
    )

for f in filenames_random_volumes:
    plot_random_volumes(f, verbose=True, show=False)
