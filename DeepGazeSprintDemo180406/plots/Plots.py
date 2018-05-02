import numpy as np
import matplotlib.pyplot as plt

def setup_matplotlib():
    fig_width_pt = 426.79135  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inches
#    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    golden_mean = .5
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height =fig_width*golden_mean       # height in inches
    fig_size = [fig_width,fig_height]
    params = {'backend': 'ps',
             'axes.labelsize': 8,
             'text.fontsize': 8,
             'legend.fontsize': 8,
             'xtick.labelsize': 6,
             'ytick.labelsize': 6,
             'lines.markersize' : 3,
             'text.usetex': False,
             'figure.figsize': fig_size,
             'image.composite_image': False}
    plt.rcParams.update(params)

def subplot(plotA, plotB, x, xlim, ylim, labelA, labelB, title, xAxisLabel, yAxisLabel):
    plt.title(title)
    color_primary = '#852177'
    color_secondary = '#0e103e'
    color_tertiary = '#00beff'
    cool_grey = '#bcbec0'
    axes = plt.gca()
    axes.yaxis.grid(zorder=0, b=True, which='major', color=cool_grey, linestyle='-')
    plt.plot(x, plotA, 'o-', label = labelA, color = color_tertiary, fillstyle='full', markeredgewidth=0.0, zorder=3)
    plt.plot(x, plotB, 'o-', label = labelB, color = color_secondary, fillstyle='full', markeredgewidth=0.0, zorder=3)
    plt.tick_params(axis = 'x', which = 'both', bottom = 'off', top = 'off')
    axes.set_axisbelow(True)
    axes.set_xlim(xlim)
    axes.set_ylim(ylim)
    #
    axes.set_ylabel(yAxisLabel)
    axes.set_xlabel(xAxisLabel)

def plot_calibration_experiments():
    setup_matplotlib()
    plt.figure()
    epochs = [10, 20, 30, 40, 50]
    xlims = [5, 55]
    low_learning_rate = np.array([31.156, 31.096, 31.036, 30.976, 30.917])
    good_learning_rate = np.array([24.005, 24.052, 24.045,  24.033, 24.018])
    #plt.subplot(121)
    subplot(low_learning_rate, good_learning_rate, epochs, xlims, [22, 32], 'SGD (1e-5), Sorted', 'SGD (1e-2), Sorted', 'Learning rate 1e-2 Vs. 1e-5', 'Epochs', 'Error $(mm)$')
    
    adamShuffled = np.array([23.784, 24.014, 24.045, 24.050, 24.034])
    adamSorted = np.array([29.521,  27.478, 26.100,  25.301, 24.837])
    #subplot(adamSorted, adamShuffled, epochs, xlims, [22, 32], 'ADAM (1e-2), Sorted', 'ADAM (1e-2), Shuffled', 'ADAM Sorted Vs. Shuffled', 'Epochs', 'Error $(mm)$')
    plt.legend(loc = 'lower right', fontsize=7, markerscale=1)
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=0.5)
    plt.savefig('calibration_experiments_1.pgf')
    plt.savefig('calibration_experiments_1.pdf')
    
if __name__ == '__main__':
    plot_calibration_experiments()
    