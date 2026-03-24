# Scientific Integrity and Research Misconduct

~~~
\author{Maxim Borisyak, Claude Code, Andrey Ustyuzhanin}
\institute{Constructor University Bremen}
\usepackage{booktabs}
~~~

## Science as a Collective Enterprise

### Scientific is Iterative

Each result is an input to subsequent works:
- cited as established fact in future introductions;
- reused as a baseline for comparison;
- built upon in methods, proofs, and datasets;
- research is planned based on prior results.

~~~align*
\text{Integrity violation}\quad &\Longrightarrow \quad \text{systematic pollution};\\
    &\Longrightarrow \quad \text{misguided future research};\\
    &\Longrightarrow \quad \text{wasted resources and time}.
~~~

### The Spectrum of Misconduct

~~~
{\footnotesize
\begin{tabular}{p{3.5cm} p{6.5cm}}
\toprule
\textbf{Category} & \textbf{Description} \\
\midrule
Honest error & Mistakes in analysis, code, misinterpretation \\
\addlinespace
Questionable Research Practices (QRPs) & Decisions that inflate apparent evidence without outright fabrication \\
\addlinespace
Research misconduct (FFP) & Deliberate fabrication, falsification or plagiarism \\
\bottomrule
\end{tabular}
}
~~~

## Fabrication and Falsification

### Fabrication

**Fabrication**: reporting data that were never collected.

Cases:
- **Hwang Woo-suk** (2004): fabricated human stem cell lines; two *Science* papers retracted;
- **Diederik Stapel** (2011): fabricated datasets for 55+ psychology papers;
- **Eric Poehlman** (2005): first US academic imprisoned for research fraud.

### Falsification

**Falsification**: altering data, images, or analyses to misrepresent reality.

Cases:
- **Jan Hendrik Schön** (2002): reused figures across 16 papers in *Science* and *Nature*; identical noise patterns in independent experiments.

### Plagiarism

**Plagiarism**: presenting others' intellectual work as one's own.

Forms:
- **verbatim copying**: reproducing text without proper attribution;
- **paraphrasing**: rewording ideas without citation;
- **idea theft**: using results from peer review or collaboration;
- **self-plagiarism**: republishing prior work without disclosure.

### Plagiarism

**Copying via LLMs**: using text produced by LLMs:
- LLMs can reproduce many texts almost verbatum (Ahmed~et~al.~2025, Huang~et~al.~2026):
- studies strongly suggests that LLM output is an amalgamation of others works;
- naturally, without attribution.

### Consequences

- retraction --- often years after publication;
- cascade retractions of papers that cited the work;
- loss of employment, funding, academic standing;
- criminal prosecution in extreme cases (Poehlman).

**Retraction half-life** in biomedicine: $\approx 10$ years.

## Statistical Malpractice

### The Logic of Hypothesis Testing

A frequentist test controls the **false positive rate**:
$$P(\text{reject } H_0 \mid H_0 \text{ true}) = \alpha$$

This holds only if:
1. hypothesis fixed before seeing data;
2. test performed exactly once.

Both assumptions are routinely violated.

### The Multiple Comparisons Problem

$k$ independent tests under $H_0$:
$$P(\text{at least one false positive}) = 1 - (1-\alpha)^k$$

- $k = 1$, $\alpha = 0.05$: $P = 0.05$;
- $k = 20$, $\alpha = 0.05$: $P \approx 0.64$.

### The Base Rate Fallacy

$\alpha$ controls $P(\text{reject } H_0 \mid H_0 \text{ true})$, not $P(H_0 \text{ true} \mid \text{reject } H_0)$.

Researchers routinely conflate the two — this is the **base rate fallacy**:
- $p < 0.05$ does **not** mean "5\% chance the null is true";
- the probability that a significant result reflects a real effect depends on the prior probability that $H_1$ is true.

### Positive Predictive Value

Let $\pi = P(H_1 \text{ true})$, $1 - \beta$ = power. Probability that a significant result is genuine:

$$\mathrm{PPV} = \frac{\pi(1-\beta)}{\pi(1-\beta) + (1-\pi)\alpha}$$

- high power and high $\pi$ $\Rightarrow$ most significant results are real;
- low $\pi$ (exploratory research, many hypotheses) $\Rightarrow$ most are false positives, even at $\alpha = 0.05$.

### Positive Predictive Value

![width=0.95](imgs/ppv.pdf)

~~~
{\small PPV vs.\ prior $\pi$ for three power levels. At $\alpha = 0.05$ (left), low-prior research produces mostly false positives even with 80\% power. Lowering $\alpha$ to 0.005 (right) substantially improves PPV.}
~~~

### Why Most Published Research Findings Are False

Ioannidis (2005) extended the PPV framework to account for bias:
- in most fields, $\pi$ is small — hypotheses are cheap to generate;
- studies are underpowered ($1 - \beta \approx 0.2$--$0.5$);
- bias ($p$-hacking, QRPs) inflates the effective false positive rate beyond $\alpha$.

For many research areas, a significant result has less than even odds of reflecting a true effect.

### p-Hacking in Practice

![width=0.95](imgs/phacking.pdf)

~~~
{\small Single honest test: $p$-values uniform under the null (left). Best of 20 tests: false positive rate $\approx 64\%$ at nominal $\alpha = 0.05$ (right).}
~~~

### Forms of p-Hacking

Each decision below adds an implicit test:
- **optional stopping**: collecting data until $p < 0.05$, then stop;
- **covariate fishing**: changing features based on their effect;
- **test switching**: choosing different tests;
- **outlier sculpting**: removing some outliers but not others:
  - the definition of outliers is often tied to the model;
- **outcome selection**: testing many hypotheses, reporting significant ones.

### The Garden of Forking Paths

Gelman \& Loken (2014): at every step (preprocessing, outlier criteria, covariates, outcome definition) multiple legitimate choices exist.

Selecting the path that "works" after seeing data $\rightarrow$ searching over all paths.

The resulting $p$-value is not calibrated to $\alpha$.

### HARKing

**HARKing** (Kerr, 1998): Hypothesising After Results are Known.

Mechanism:
1. collect data; explore; find a pattern;
2. rewrite the introduction as if the pattern was the original question.

Effect: exploratory analysis presented as confirmatory $\Rightarrow$ evidential value destroyed.

### Publication Bias

**Publication bias**: positive results are published; null results are not.

Consequence: the literature overestimates effect sizes.

**Funnel plot**: studies scatter symmetrically around the true effect under no bias; publication bias creates visible asymmetry by removing small null-result studies.

### Publication Bias

![width=0.95](imgs/funnel.pdf)

~~~
{\small All studies (left) vs.\ published studies only (right). Small null-result studies are absent; mean reported effect $\bar{d}$ shifts away from zero.}
~~~

### Selective Outcome Reporting

**Outcome switching**: pre-register outcome $A$; report outcome $B$ when $A$ is non-significant.

- Chan et al.\ (2004): 62\% of clinical trials changed, introduced, or omitted a primary outcome between registration and publication;
- pre-registration creates an auditable record that makes switching detectable.

## Manipulation of Methodology

### Inappropriate Baselines

Reporting a method as better than an unfair comparison is not a contribution:
- **weak baseline**: poorly tuned or outdated comparison method;
- **task asymmetry**: easier formulation for the baseline;
- **metric cherry-picking**: reporting the metric where the proposed method wins.

Tuning one method on validation data while using defaults for the baseline invalidates the comparison.

### Cherry-Picking

Selective presentation of evidence:
- reporting only conditions where the method succeeds;
- excluding runs with inconvenient results;
- evaluating on a curated subset of the test set.

Statistical effect: identical to p-hacking — reported performance does not generalise.

### Fabrication Detection: Benford's Law

**Benford's Law**: naturally occurring data obey $P(\text{leading digit} = d) = \log_{10}(1 + 1/d)$.

![width=0.95](imgs/benford.pdf)

~~~
{\small Authentic data (left) conforms to Benford's Law. Fabricated data (right) deviates — humans generating numbers tend toward uniformity.}
~~~

### Other Fabrication Signatures

- **terminal digit preference**: fabricated data clusters on 0 and 5;
- **GRIM test**: certain means are arithmetically impossible for integer-valued scales.

## Graphical Misrepresentation

### Truncated Y-Axis

![width=0.95](imgs/truncated_axis.pdf)

### Cherry-Picking a Time Window

![width=0.95](imgs/cherry_time.pdf)

### Omitting Uncertainty

![width=0.95](imgs/error_bars.pdf)

### Over-Smoothing

![width=0.95](imgs/smoothing.pdf)

### Aspect Ratio Manipulation

![width=0.95](imgs/aspect_ratio.pdf)

## Machine Learning–Specific Issues

### Test Set Contamination

**Contamination**: test information leaks into training or model selection.

Forms:
- test samples included in the training set (data leakage);
- preprocessing statistics (mean, variance) computed over the full dataset;
- future information leaks into the past in time-series settings.

### Leaderboard Overfitting

![width=0.9](imgs/leaderboard.pdf)

~~~
{\small Repeated evaluation against a fixed test set inflates best-so-far accuracy even when no model improves. True accuracy (dashed) is constant.}
~~~

### Leaderboard Overfitting: Analysis

$k$ submissions, true accuracy $p$, test set size $n$, $\sigma = \sqrt{p(1-p)/n}$:

$$\mathbb{E}\!\left[\max_{i \leq k} \hat{p}_i\right] \approx p + \sigma \cdot \Phi^{-1}\!\!\left(\frac{k}{k+1}\right)$$

$n = 1000$, $p = 0.80$, $k = 80$:
- best-reported accuracy $\approx 0.815$.

### Benchmark Gaming

- **dataset-specific tuning**: hyperparameters optimised for the benchmark, not by cross-validation;
- **metric shopping**: report only the metric where the method ranks first;
- **benchmark construction bias**: benchmark designed to favour properties of one's own method;
- **selective comparison**: omit concurrent work that would narrow the gap.

### Reproducibility in ML

Pineau et al.\ (2021): a substantial fraction of ML papers do not release code, do not specify seeds, do not report variance, do not document hardware.

Henderson et al.\ (2018): deep RL results vary by up to 300\% across seeds and implementation details — never disclosed in the original papers.

## Publication Malpractice

### Salami Slicing

**Salami slicing**: dividing one body of work into multiple minimal publications.

- inflates publication count without proportional contribution;
- fragments the record — reviewers cannot see the full picture.

### Duplicate Publication

**Duplicate publication**: same work submitted to multiple venues without disclosure.

Legitimate:
- conference $\to$ journal with substantial extension (disclosed);
- preprint $\to$ peer-reviewed venue (standard practice).

Not legitimate: simultaneous submission, superficial repackaging without disclosure.

### Authorship Fraud

ICMJE criteria: each author must have made a substantial intellectual contribution, participated in drafting, approved the final version, and be accountable.

Violations:
- **gift authorship**: non-contributors added for prestige;
- **ghost authorship**: real contributors omitted (common in industry-funded trials);
- **coercive authorship**: authorship demanded in exchange for resources.

## The Replication Crisis

### Scale of the Problem

~~~
{\footnotesize
\begin{tabular}{p{5.5cm} r p{3.5cm}}
\toprule
\textbf{Study} & \textbf{Rate} & \textbf{Field} \\
\midrule
Open Science Collaboration (2015) & 36–39\% & Psychology \\
Camerer et al.\ (2018) & 62\% & Economics \\
Begley \& Ellis (2012) & 11\% & Cancer biology \\
Reprod.\ Project: Cancer Biology (2021) & 50\% & Cancer biology \\
\bottomrule
\end{tabular}
}
~~~

### Structural Causes

The crisis is driven by incentives, not primarily by fraud:
- **publication bias**: positive results published; null results filed away;
- **underpowered studies**: small $n$ inflates estimates conditional on significance;
- **researcher degrees of freedom**: legitimate choices collectively inflate false positive rate;
- **career incentives**: novel positive results rewarded; replications are not.

### The Winner's Curse

Conditioning on $p < \alpha$ in an underpowered study ($1 - \beta \ll 1$):

$$\mathbb{E}[\hat{\delta} \mid p < \alpha] > \delta_{\text{true}}$$

Published estimates are biased upward. Adequately powered replications find smaller effects — the published literature is a biased sample of all studies conducted.

## Safeguards

### Registered Reports

**Registered Reports**: peer review before data collection; acceptance contingent on question and method, not outcome.

~~~
{\footnotesize
\begin{tabular}{p{4.5cm} p{4.5cm}}
\toprule
\textbf{Standard} & \textbf{Registered Report} \\
\midrule
Idea $\to$ Data $\to$ Paper $\to$ Review & Idea $\to$ Review $\to$ Data $\to$ Paper \\
\addlinespace
Acceptance depends on results & Acceptance independent of results \\
\addlinespace
Publication bias acts & Publication bias structurally eliminated \\
\bottomrule
\end{tabular}
}
~~~

### Open Data and Code

- enables independent verification;
- allows error detection before findings propagate;
- makes the methods section verifiable, not merely aspirational.

### Practical Checklist

**Statistics:**
- pre-specify primary outcome and analysis plan;
- apply multiple comparison corrections;
- report all outcomes.

**Machine learning:**
- fix splits before any modelling decision;
- multiple seeds (5-10); compute estimate errors;
- tune all baselines equally;
- release code.

### Recognising QRPs in the Wild

When reading a paper:
- are baselines recent and competitively tuned?
- are null or negative results present?
- is the method section sufficient for reimplementation?
- **are estimate errors reported?**

## Conclusion

### Summary

~~~
{\footnotesize
\begin{tabular}{p{3.5cm} p{6cm}}
\toprule
\textbf{Category} & \textbf{Examples} \\
\midrule
Misconduct (FFP) & Fabrication, falsification, plagiarism \\
\addlinespace
Statistical QRPs & $p$-hacking, HARKing, optional stopping, outcome switching \\
\addlinespace
Methodological QRPs & Cherry-picking, inappropriate baselines, benchmark gaming \\
\addlinespace
Publication QRPs & Salami slicing, gift authorship, duplicate publication \\
\addlinespace
ML-specific QRPs & Leaderboard overfitting, test contamination, metric shopping \\
\midrule
Safeguards & Pre-registration, open data/code, registered reports \\
\bottomrule
\end{tabular}
}
~~~

## References

### References 1

~~~
{\scriptsize
\begin{itemize}
\setlength\itemsep{0.25em}
\item Begley \& Ellis (2012). Raise standards for preclinical cancer research. \textit{Nature}, 483, 531--533.
\item Camerer et al.\ (2018). Replicability of social science experiments in \textit{Nature} and \textit{Science}. \textit{Nat.\ Hum.\ Behav.}, 2, 637--644.
\item Chan et al.\ (2004). Selective reporting of outcomes in randomized trials. \textit{JAMA}, 291, 2457--2465.
\item Errington et al.\ (2021). Investigating the replicability of preclinical cancer biology. \textit{eLife}, 10, e71601.
\item Gelman \& Loken (2014). The statistical crisis in science. \textit{Am.\ Scientist}, 102, 460--465.
\item Ioannidis, J.P.A.\ (2005). Why most published research findings are false. \textit{PLOS Med.}, 2(8), e124.
\item Henderson et al.\ (2018). Deep reinforcement learning that matters. \textit{AAAI}, 3207--3214.
\item Kerr (1998). HARKing: Hypothesizing after the results are known. \textit{PSPR}, 2, 196--217.
\end{itemize}
}
~~~

### References 2

~~~
{\scriptsize
\begin{itemize}
\setlength\itemsep{0.25em}
\item Open Science Collaboration (2015). Reproducibility of psychological science. \textit{Science}, 349, aac4716.
\item Pineau et al.\ (2021). Improving reproducibility in machine learning research. \textit{JMLR}, 22(164), 1--20.
\item Ahmed, A.M. et al.\ (2026). Extracting books from production language models. ArXiv, abs/2601.02671.
\item Huang, J. et al.\ (2024). Demystifying Verbatim Memorization in Large Language Models. EMNLP 2024
\end{itemize}
}
~~~
