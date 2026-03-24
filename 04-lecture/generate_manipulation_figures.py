"""
Figures illustrating graphical data manipulation techniques.
Run from 04-lecture/:  python generate_manipulation_figures.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.ndimage import uniform_filter1d

rng = np.random.default_rng(0)

FIGSIZE = (9, 3.6)
DPI = 150

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
})


def label_axes(axes, labels):
    for ax, lbl in zip(axes, labels):
        ax.set_title(lbl, fontsize=11, pad=4)


# ─────────────────────────────────────────────────────────────────────────────
# Figure 1: Truncated y-axis
# ─────────────────────────────────────────────────────────────────────────────

groups = ["Control", "Treatment"]
means  = [0.823, 0.851]      # realistic, small effect
colors = ["#4878CF", "#C44E52"]

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)

for ax, (ymin, ymax), title in [
    (axes[0], (0.0, 1.0), "Honest (axis from zero)"),
    (axes[1], (0.80, 0.87), "Truncated axis"),
]:
    bars = ax.bar(groups, means, color=colors, width=0.45, edgecolor="white")
    ax.set_ylim(ymin, ymax)
    ax.set_ylabel("accuracy")
    ax.set_title(title)
    for bar, m in zip(bars, means):
        ax.text(bar.get_x() + bar.get_width() / 2, m + (ymax - ymin) * 0.02,
                f"{m:.3f}", ha="center", va="bottom", fontsize=9)

fig.tight_layout()
fig.savefig("imgs/truncated_axis.pdf", bbox_inches="tight")
fig.savefig("imgs/truncated_axis.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/truncated_axis.pdf")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 2: Cherry-picked time window
# ─────────────────────────────────────────────────────────────────────────────

N = 200
t = np.arange(N)
# Long-run flat trend with noise plus a short upswing near the middle
signal = 0.002 * np.sin(2 * np.pi * t / 120) + rng.normal(0, 0.04, N)
series = np.cumsum(signal) * 0.15 + 2.0
# Ensure there is a visible cherry-pick window
cherry_start, cherry_end = 80, 115

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, sharey=False)

ax = axes[0]
ax.plot(t, series, color="#4878CF", linewidth=1.2)
ax.axvspan(cherry_start, cherry_end, alpha=0.15, color="#C44E52")
ax.set_xlabel("time")
ax.set_ylabel("metric")
ax.set_title("Full record (honest)")

ax = axes[1]
ax.plot(t[cherry_start:cherry_end],
        series[cherry_start:cherry_end], color="#C44E52", linewidth=1.8)
ax.set_xlabel("time")
ax.set_ylabel("metric")
ax.set_title("Reported window only")

fig.tight_layout()
fig.savefig("imgs/cherry_time.pdf", bbox_inches="tight")
fig.savefig("imgs/cherry_time.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/cherry_time.pdf")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 3: Omitting error bars
# ─────────────────────────────────────────────────────────────────────────────

methods = ["Baseline", "Proposed"]
means2  = [0.762, 0.801]
sems    = [0.031, 0.028]        # 95% CI half-widths ≈ 1.96 * SE
ci95    = [1.96 * s for s in sems]

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)

for ax, show_err, title in [
    (axes[0], False, "Without uncertainty"),
    (axes[1], True,  "With 95\\% CI"),
]:
    yerr = ci95 if show_err else None
    bars = ax.bar(methods, means2, color=colors, width=0.45,
                  yerr=yerr, capsize=6, edgecolor="white",
                  error_kw={"elinewidth": 1.5, "ecolor": "#333333"})
    ax.set_ylim(0.68, 0.86)
    ax.set_ylabel("accuracy")
    ax.set_title(title)

fig.tight_layout()
fig.savefig("imgs/error_bars.pdf", bbox_inches="tight")
fig.savefig("imgs/error_bars.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/error_bars.pdf")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 4: Smoothing to hide variance / cycles
# ─────────────────────────────────────────────────────────────────────────────

N2 = 300
t2 = np.arange(N2)
# Underlying process: slight upward linear trend + oscillation + noise
underlying = 0.005 * t2 + 3 * np.sin(2 * np.pi * t2 / 40)
noisy = underlying + rng.normal(0, 1.5, N2)

smooth_light  = uniform_filter1d(noisy, size=5)
smooth_heavy  = uniform_filter1d(noisy, size=60)

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)

ax = axes[0]
ax.plot(t2, noisy, color="#4878CF", alpha=0.4, linewidth=0.7, label="raw data")
ax.plot(t2, smooth_light, color="#4878CF", linewidth=1.6, label="light smoothing")
ax.set_xlabel("time")
ax.set_ylabel("value")
ax.set_title("Honest: structure visible")
ax.legend(fontsize=8)

ax = axes[1]
ax.plot(t2, noisy, color="#C44E52", alpha=0.15, linewidth=0.7)
ax.plot(t2, smooth_heavy, color="#C44E52", linewidth=2.2, label="heavy smoothing")
ax.set_xlabel("time")
ax.set_ylabel("value")
ax.set_title("Manipulated: oscillation erased")
ax.legend(fontsize=8)

fig.tight_layout()
fig.savefig("imgs/smoothing.pdf", bbox_inches="tight")
fig.savefig("imgs/smoothing.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/smoothing.pdf")


# ─────────────────────────────────────────────────────────────────────────────
# Figure 5: Aspect ratio manipulation
# ─────────────────────────────────────────────────────────────────────────────

x = np.linspace(0, 10, 120)
y = 0.15 * x + rng.normal(0, 0.25, 120)   # genuine small positive trend

fig = plt.figure(figsize=FIGSIZE)
gs = gridspec.GridSpec(1, 2, figure=fig, wspace=0.35)

ax0 = fig.add_subplot(gs[0])
ax0.scatter(x, y, s=12, color="#4878CF", alpha=0.6)
ax0.set_aspect("auto")
ax0.set_xlim(0, 10)
ax0.set_ylim(-1.5, 3.5)
ax0.set_xlabel("x")
ax0.set_ylabel("y")
ax0.set_title("Honest aspect ratio")

# Compressed x-axis: squish horizontally to make slope look steeper
ax1 = fig.add_subplot(gs[1])
ax1.scatter(x, y, s=12, color="#C44E52", alpha=0.6)
ax1.set_xlim(0, 10)
ax1.set_ylim(-1.5, 3.5)
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Compressed x-axis: trend exaggerated")

# Force narrow width by adjusting the subplot position
pos = ax1.get_position()
ax1.set_position([pos.x0, pos.y0, pos.width * 0.38, pos.height])

fig.savefig("imgs/aspect_ratio.pdf", bbox_inches="tight")
fig.savefig("imgs/aspect_ratio.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/aspect_ratio.pdf")
