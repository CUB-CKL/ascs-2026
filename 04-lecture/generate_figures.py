"""
Generate figures for the Scientific Integrity lecture.
Run from the 04-lecture/ directory:
    python generate_figures.py
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy import stats

rng = np.random.default_rng(42)

FIGSIZE = (9, 4)
DPI = 150
TEXTSIZE = 12

plt.rcParams.update({
    "font.family": "serif",
    "font.size": TEXTSIZE,
    "axes.titlesize": TEXTSIZE + 1,
    "axes.labelsize": TEXTSIZE,
    "xtick.labelsize": TEXTSIZE - 1,
    "ytick.labelsize": TEXTSIZE - 1,
    "legend.fontsize": TEXTSIZE - 1,
})

# ──────────────────────────────────────────────────────────────────────────────
# Figure 1: p-hacking — the multiple comparisons problem
# ──────────────────────────────────────────────────────────────────────────────

N_SIM = 50_000
N_TESTS = 20
ALPHA = 0.05

# Single honest test: p-values under the null should be uniform
p_single = rng.uniform(0, 1, N_SIM)

# p-hacker runs N_TESTS independent tests on null data, keeps the minimum
p_all = rng.uniform(0, 1, (N_SIM, N_TESTS))
p_hacked = p_all.min(axis=1)

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, sharey=False)

bins = np.linspace(0, 1, 41)

ax = axes[0]
ax.hist(p_single, bins=bins, color="#4878CF", edgecolor="white", linewidth=0.4, density=True)
ax.axvline(ALPHA, color="#C44E52", linewidth=1.8, linestyle="--", label=rf"$\alpha = {ALPHA}$")
ax.set_xlabel("$p$-value")
ax.set_ylabel("density")
ax.set_title("Single test (honest)")
ax.legend(loc='lower right')
fp_rate_single = (p_single < ALPHA).mean()
ax.text(0.5, 0.95, f"False positive rate: {fp_rate_single:.3f}",
        transform=ax.transAxes, ha="center", va="top", fontsize=TEXTSIZE - 1,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#EEF3FB", edgecolor="#4878CF"))

ax = axes[1]
ax.hist(p_hacked, bins=bins, color="#C44E52", edgecolor="white", linewidth=0.4, density=True)
ax.axvline(ALPHA, color="#333333", linewidth=1.8, linestyle="--", label=rf"$\alpha = {ALPHA}$")
ax.set_xlabel("minimum $p$-value over 20 tests")
ax.set_title(f"Best of {N_TESTS} tests ($p$-hacking)")
ax.legend(loc='lower right')
fp_rate_hacked = (p_hacked < ALPHA).mean()
ax.text(0.5, 0.95, f"False positive rate: {fp_rate_hacked:.3f}",
        transform=ax.transAxes, ha="center", va="top", fontsize=TEXTSIZE - 1,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#FDEAEA", edgecolor="#C44E52"))

fig.tight_layout()
fig.savefig("imgs/phacking.pdf", bbox_inches="tight")
fig.savefig("imgs/phacking.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/phacking.pdf")


# ──────────────────────────────────────────────────────────────────────────────
# Figure 2: Publication bias — asymmetric funnel plot
# ──────────────────────────────────────────────────────────────────────────────

N_STUDIES = 600
true_effect = 0.0          # null world: no real effect
se_range = (0.05, 0.5)     # range of standard errors (larger SE = smaller study)

se = rng.uniform(*se_range, N_STUDIES)
effect = rng.normal(true_effect, se)      # observed effect = true + noise
z = effect / se
p_value = 2 * stats.norm.sf(np.abs(z))

# Publication model: studies are published if p < 0.05 OR large sample size
# "file drawer" effect: small, non-significant studies disappear
published = (p_value < ALPHA) | (se < 0.15)

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE)

for ax, mask, title, color in [
    (axes[0], np.ones(N_STUDIES, dtype=bool), "All studies (unbiased)", "#4878CF"),
    (axes[1], published, "Published studies (biased)", "#C44E52"),
]:
    ax.scatter(effect[mask], se[mask], alpha=0.4, s=14, color=color)
    ax.axvline(0, color="black", linewidth=1.0, linestyle="-")
    ax.axvline(2 * se[mask].mean(), color="gray", linewidth=1.0, linestyle=":")
    ax.invert_yaxis()
    ax.set_xlabel("estimated effect size")
    ax.set_ylabel("standard error (larger SE = smaller study)")
    ax.set_title(title)
    n = mask.sum()
    mean_e = effect[mask].mean()
    ax.text(0.97, 0.05, f"$n = {n}$\n$\\bar{{d}} = {mean_e:+.3f}$",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=TEXTSIZE - 2,
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.8))

fig.tight_layout()
fig.savefig("imgs/funnel.pdf", bbox_inches="tight")
fig.savefig("imgs/funnel.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/funnel.pdf")


# ──────────────────────────────────────────────────────────────────────────────
# Figure 3: Leaderboard overfitting (test-set shopping)
# ──────────────────────────────────────────────────────────────────────────────

# Simulate a fixed test set of N_TEST binary predictions.
# Each submission is a random classifier with true accuracy p_true.
# The published "best" accuracy is max(all submissions so far).

N_TEST = 1000
P_TRUE = 0.80      # actual underlying accuracy
N_SUBMISSIONS = 80
N_RUNS = 2000

accuracies_matrix = rng.binomial(N_TEST, P_TRUE, (N_RUNS, N_SUBMISSIONS)) / N_TEST

best_so_far = np.maximum.accumulate(accuracies_matrix, axis=1)

mean_best = best_so_far.mean(axis=0)
q10 = np.percentile(best_so_far, 10, axis=0)
q90 = np.percentile(best_so_far, 90, axis=0)

# Theoretical standard error for single submission
single_se = np.sqrt(P_TRUE * (1 - P_TRUE) / N_TEST)

fig, ax = plt.subplots(figsize=(7, 4))

submissions = np.arange(1, N_SUBMISSIONS + 1)
ax.plot(submissions, mean_best, color="#C44E52", linewidth=2.0, label="mean best accuracy")
ax.fill_between(submissions, q10, q90, color="#C44E52", alpha=0.15, label="10–90th percentile")
ax.axhline(P_TRUE, color="black", linewidth=1.5, linestyle="--", label=f"true accuracy ({P_TRUE:.2f})")
ax.axhline(P_TRUE + single_se, color="gray", linewidth=1.0, linestyle=":",
           label=f"true $\\pm$ 1 SE")
ax.axhline(P_TRUE - single_se, color="gray", linewidth=1.0, linestyle=":")

ax.set_xlabel("number of submissions to leaderboard")
ax.set_ylabel("best reported accuracy")
ax.set_title("Leaderboard overfitting: test-set shopping inflates apparent performance")
ax.legend(loc="lower right", fontsize=TEXTSIZE - 2)
ax.set_xlim(1, N_SUBMISSIONS)

fig.tight_layout()
fig.savefig("imgs/leaderboard.pdf", bbox_inches="tight")
fig.savefig("imgs/leaderboard.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/leaderboard.pdf")


# ──────────────────────────────────────────────────────────────────────────────
# Figure 4: Benford's Law — fabrication detection
# ──────────────────────────────────────────────────────────────────────────────

benfords = np.array([np.log10(1 + 1/d) for d in range(1, 10)])

# Authentic data: draw from a log-normal distribution
authentic_vals = rng.lognormal(mean=2.0, sigma=1.5, size=500)
authentic_first = np.array([int(str(f"{v:.6e}")[0]) for v in authentic_vals])

# Fabricated data: person picks "random-looking" integers, tends to uniform or biased
fabricated_first = rng.choice(
    np.arange(1, 10),
    size=500,
    p=[0.09, 0.12, 0.14, 0.13, 0.12, 0.12, 0.10, 0.09, 0.09]  # slightly uniform
)

digits = np.arange(1, 10)

fig, axes = plt.subplots(1, 2, figsize=FIGSIZE, sharey=True)

for ax, first_digits, title, color in [
    (axes[0], authentic_first, "Authentic data", "#4878CF"),
    (axes[1], fabricated_first, "Suspicious data", "#C44E52"),
]:
    observed = np.array([(first_digits == d).mean() for d in digits])
    ax.bar(digits, observed, color=color, alpha=0.7, label="observed", width=0.5)
    ax.plot(digits, benfords, "ko--", linewidth=1.5, markersize=5, label="Benford's law")
    ax.set_xlabel("leading digit")
    ax.set_ylabel("proportion")
    ax.set_title(title)
    ax.set_xticks(digits)
    ax.legend()

fig.tight_layout()
fig.savefig("imgs/benford.pdf", bbox_inches="tight")
fig.savefig("imgs/benford.png", bbox_inches="tight", dpi=DPI)
plt.close(fig)
print("Saved: imgs/benford.pdf")
