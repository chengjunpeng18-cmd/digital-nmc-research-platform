"""Plot palette sampled from the team's GEMV reference figures."""

BASELINE = '#7b9aad'
BLUE = '#0072b2'
ORANGE = '#d55e00'
INK = '#444444'
INPUT = '#d9d9d9'
GENERATION = '#e0e0e0'
RANKING = '#999999'
HATCH = '///'

POLICY_LINES = {
    'unindp-compact': (INK, 'o', '-'),
    'noc-v03': (ORANGE, 's', '-'),
    'noc-v04': (BLUE, '^', '-'),
    'fixed-row': (BASELINE, 'D', '--'),
    'fixed-k': (RANKING, 'v', ':'),
}


def line_style(policy):
    color, marker, linestyle = POLICY_LINES[policy]
    return dict(color=color, marker=marker, linestyle=linestyle, markerfacecolor='white')


def bar_style(color, hatch=None):
    return dict(color=color, edgecolor=INK, linewidth=.65, hatch=hatch)


def apply_style(plt):
    plt.rcParams.update({
        'font.size': 10,
        'svg.fonttype': 'none',
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'axes.edgecolor': '#222222',
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.grid': True,
        'axes.grid.axis': 'y',
        'axes.axisbelow': True,
        'grid.color': '#ebebeb',
        'grid.linewidth': .65,
        'hatch.linewidth': .85,
        'legend.frameon': False,
    })
