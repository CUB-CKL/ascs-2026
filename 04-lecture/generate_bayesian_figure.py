"""
Figure: Positive Predictive Value (PPV) under the Ioannidis framework.
Run from 04-lecture/:  python generate_bayesian_figure.py
"""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
})

def ppv(pi, power, alpha):
    """P(H1 true | p < alpha) = pi*(1-beta) / [pi*(1-beta) + (1-pi)*alpha]"""
    return (pi * power) / (pi * power + (1 - pi) * alpha)


pi = np.linspace(0.01, 0.5, 300)
powers = [0.20, 0.50, 0.80]
colors = ["#C44E52", "#DD8452", "#4878CF"]
alphas_panels = [0.05, 0.005]
titles = [r"$\alpha = 0.05$", r"$\alpha = 0.005$"]

fig, axes = plt.subplots(1, 2, figsize=(9, 3.8), sharey=True)

for ax, alpha, title in zip(axes, alphas_panels, titles):
    for power, color in zip(powers, colors):
        y = ppv(pi, power, alpha)
        ax.plot(pi, y, color=color, linewidth=1.8,
                label=f"power $= {power}$")
    ax.axhline(0.5, color="black", linewidth=0.8, linestyle=":",
               label="PPV $= 0.5$ (coin flip)")
    ax.set_xlabel(r"prior probability $\pi$ that $H_1$ is true")
    ax.set_ylabel("positive predictive value (PPV)")
    ax.set_title(title)
    ax.set_xlim(0, 0.5)
    ax.set_ylim(0, 1)
    ax.legend(loc="lower right")

fig.tight_layout()
fig.savefig("imgs/ppv.pdf", bbox_inches="tight")
fig.savefig("imgs/ppv.png", bbox_inches="tight", dpi=150)
plt.close(fig)
print("Saved: imgs/ppv.pdf")
