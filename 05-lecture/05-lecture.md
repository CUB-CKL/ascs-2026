# Reviewing Scientific Articles

~~~
\author{Maxim Borisyak, Claude Code, Andrey Ustyuzhanin}
\institute{Constructor University Bremen}
\usepackage{booktabs}
~~~

## The Peer Review Process

### What is Peer Review?

**Peer review**: evaluation of scientific work by experts in the same field before publication.

Occurs at:
- **conference submissions** (1-3 weeks per review);
- **journal submissions** (months to years);
- **grant applications** (funding agencies);
- **community code review** (open source).

Reviewers are typically unpaid volunteers.

### Goals of Peer Review

Reviewers assess:
1. **correctness**: are the claims true and properly justified?
2. **novelty**: does this advance the field?
3. **significance**: does this matter?
4. **clarity**: is the work well-presented?
5. **rigor**: is the methodology sound?

Peer review is not:
- **exhaustive verification** — reviewers check plausibility, not every calculation;
- **guaranteed to catch fraud** — but it catches many honest mistakes;
- **democratizing** — not all reviewers are equally competent.

### Peer Review is Imperfect

**Known limitations**:
- major errors slip through (see Hwang Woo-suk, Stapel, Schön);
- bias exists — reviewers favor citations of their own work;
- reviewer selection affects outcome (expertise, competition);
- conflicts of interest are underreported;
- publication bias — negative results rarely appear.

Despite flaws, peer review remains the best mechanism we have.

### Your Role as a Reviewer

You are a **critical reader**, not an auditor:
- catch obvious errors and inconsistencies;
- identify questionable claims that lack support;
- spot methodological red flags;
- assess clarity and organization;
- provide constructive feedback.

You are **not** expected to:
- verify every calculation by hand;
- reproduce all experiments (though you should check design);
- detect all fraud (that's nearly impossible);
- gatekeep for competitive reasons.

## Reading a Paper: Framework

### The Reading Strategy: First Pass

**First pass** (10-20 minutes):
- title, abstract, headings, conclusion;
- figures and tables (captions only);
- determine: is this relevant to me? what's the scope?

### The Reading Strategy: Detailed Passes

**Second pass** (main evaluation):
- introduction: problem and novelty;
- method: does approach make sense?
- results: are they convincing?

**Third pass** (if needed):
- proofs or calculations;
- experimental design details.

### Introduction and Motivation

**What to check**:
- **clarity of problem**: can you state what's being solved?
- **motivation**: why does this matter?
- **related work**: relevant prior art acknowledged?
- **claimed novelty**: what is genuinely new?

**Red flags**:
- problem poorly motivated;
- prior work omitted or misrepresented;
- novelty claims without citing prior work.

### The Method/Theory Section

For **empirical papers**:
- algorithm description clear and complete?
- hyperparameters fully specified?
- reproducible from description?

For **theoretical papers**:
- definitions precise and match standard notation?
- assumptions clearly stated and reasonable?
- proofs logical and complete?

**Red flags**:
- vague algorithm description;
- missing hyperparameters;
- theorems without proofs (or deferred to missing appendix).

### Experimental Setup: Baselines and Data

For ML/systems papers:

**Baselines**:
- fair comparison? (same tuning effort)
- recent and from reputable implementations?

**Datasets**:
- public/standard or custom?
- data leakage between train/test?

### Experimental Setup: Metrics and Design

**Metrics**:
- appropriate for problem?
- multiple metrics or cherry-picked?

**Design**:
- multiple runs with error bars?
- significance testing?
- complete ablations?

### Results and Claims

**What to check**:
- improvements meaningful or within noise?
- p-values, confidence intervals reported?
- all runs reported or cherry-picked?
- conclusions match the data?

**Red flags**:
- tiny improvements (0.5%) without error bars;
- inconsistent across datasets;
- "state-of-the-art" vs. outdated baselines;
- missing or incomplete ablations.

### Figures and Tables: What to Look For

**Good figures**:
- clear labels, legend, caption;
- error bars visible;
- caption explains content.

### Figures and Tables: Red Flags

**Suspicious patterns**:
- unexplained discontinuities;
- overly smooth curves (interpolation?);
- cherry-picked time windows;
- exaggerated y-axis scales;
- missing error bars;
- identical noise patterns across experiments.

### Conclusion and Discussion

**What to check**:
- claims match the results?
- limitations acknowledged (or omitted)?
- future work realistic or hand-waving?
- code/data availability addressed?

**Red flags**:
- conclusions broader than evidence;
- limitations absent or buried;
- critical validations deferred to "future work";
- reproducibility not addressed.

## Red Flags and Suspicious Practices

### Warning signs

~~~
{\scriptsize
\begin{tabular}{p{3.8cm} p{6.2cm}}
\toprule
\textbf{Pattern} & \textbf{Why suspicious} \\
All $p < 0.05$ & Multiple tests produce false positives by chance \\
Improvements only on custom data & Overfitting to domain \\
Monotonic improvement with size & May be cherry-picked curve \\
One metric wins, others don't & Metric gaming \\
Only old baselines & Recent ones might be better \\
\bottomrule
\end{tabular}
}
~~~

### Statistical Red Flags: p-Hacking

**p-hacking indicators**:
- many tests, only positive ones reported;
- $p$-values just below 0.05 (not $< 0.01$);
- no multiple comparisons correction;
- no error bars or significance tests.

### Statistical Red Flags: Misuse

**Underpowered studies**:
- small samples without power discussion;
- single runs (no replication).

**Misused language**:
- "significant" (statistical vs. practical);
- "95\% chance" (backwards probability).

### Methodological Red Flags: Leakage

**Data leakage**:
- hyperparameters tuned on test set;
- test set visible during training;
- test statistics in preprocessing;
- global preprocessing (off-the-shelf).

### Methodological Red Flags: Fairness and Robustness

**Unfair comparisons**:
- baselines not publicly available or tuned;
- different preprocessing for method vs. baselines.

**Suspicious generalization**:
- works only on specific domain;
- improvements vanish on other datasets;
- robustness not tested.

### Visual Red Flags

Watch for suspicious **figures and images**:

**Computer-generated results**:
- identical noise patterns in figures claiming independent experiments;
- pixel-perfect repetition (copy-paste);
- discontinuities that don't match stated methodology;
- too smooth or too regular (curve fitting or interpolation on test data).

**Example**: Jan Hendrik Schön's papers had identical noise patterns in plots across supposedly independent experiments.

### Visual Red Flags

**Documentation red flags**:
- captions that don't match the figure content;
- axis labels missing or inconsistent;
- figure quality that suggests poor quality control;
- legends that don't match the plotted lines.

## Computer Science and Machine Learning Specifics

### Common ML Pitfalls

**Neural networks should report**:
- architecture (layers, activations, dropout);
- initialization scheme;
- optimizer and learning rate;
- number of runs (best/mean/median?);
- how hyperparameters were chosen.

**Deep learning red flags**:
- batch size not reported;
- learning rate defaults without justification;
- single initialization;
- no ablation of architecture components.

### Benchmark Gaming

**Dataset overfitting**:
- tuning on benchmarks until saturation;
- may not generalize to similar data;
- compared on same benchmarks where tuned.

**Metric gaming**:
- metric doesn't reflect actual goal;
- accuracy up, latency down (impractical);
- ignores domain constraints (fairness, interpretability).

### Reproducibility Concerns

**Red flags**:
- code unavailable ("upon request");
- hard-coded paths in code;
- old or unavailable libraries;
- random seeds not reported;
- no documentation.

**Green flags**:
- GitHub with clear instructions;
- environment specified (requirements, Docker);
- reproduction scripts;
- hyperparameter documentation.

### Transfer Learning and Fine-tuning

**Be skeptical**:
- ImageNet pre-training on different domains;
- fine-tuning on tiny datasets;
- no ablation of pre-training benefit;
- fine-tuned vs. from-scratch comparisons.

**Standard practice**:
- compare pre-trained and from-scratch equally;
- tune fine-tuning hyperparameters carefully.

## Spotting Questionable Research Practices (QRPs)

### Common QRPs in Computer Science

**Selective reporting**:
- report only positive results;
- cherry-pick datasets where method wins;
- redefine success criteria after seeing data.

**Flexibility in analysis**:
- choose aggregation/metric that looks best;
- post-hoc grouping of data;
- threshold data after seeing results.

**HARKing** (Hypothesizing After Results are Known):
- claim results were predicted after seeing them;
- frame exploratory as confirmatory.

### Documentation of Questionable Practices

**Papers sometimes reveal their own QRPs**:
- "we ran this experiment three times and report the best result" (cherry-picking);
- "we tried many variants and chose the most stable" (HARKing);
- "ablations are in the appendix" (but appendix is missing);
- "we optimized hyperparameters for each baseline" vs. "we use default hyperparameters" (inconsistent effort).

### Questions to Ask

When something feels off:

1. Would conclusion hold with reasonable parameter variation?
2. Were hyperparameters tuned on test set?
3. Are results consistent across datasets?
4. Could improvements be implementation differences?

## Constructive Feedback

### Writing an Effective Review

**Structure**:
1. Summary (1-2 sentences);
2. Strengths (2-3 points);
3. Weaknesses (ordered by importance);
4. Questions and suggestions;
5. Recommendation.

**Tone**:
- be specific: point to exact issues;
- criticize the work, not authors;
- be constructive;
- be honest about uncertainty.

### The Reviewer's Checklist

Before submitting your review:

~~~
{\footnotesize
\begin{tabular}{p{6.5cm}p{3.5cm}}
\toprule
\textbf{Question} & \textbf{Checked} \\
\midrule
Is the contribution novel and significant? & \\
Are the claims supported by evidence? & \\
Is the method described clearly enough to reproduce? & \\
Are comparisons fair (same computational budget, tuning effort)? & \\
Are limitations acknowledged? & \\
Are there obvious statistical/methodological errors? & \\
Are there red flags for fabrication or falsification? & \\
Is the paper well-written and organized? & \\
\bottomrule
\end{tabular}
}
~~~

## Reviewing for Conferences vs. Journals

### Conference Reviews

**Timeline**: 2-4 weeks.

**Characteristics**:
- **broad scope**: papers from many areas;
- **quick turnaround**: reviewers are rushed;
- **single-blind or double-blind**: reviewer anonymity varies;
- **lower bar**: acceptance rate 15-30\%, still high volume.

**Your review is brief but must address**:
- novelty and significance;
- correctness of main claims;
- clarity;
- recommendation.

### Journal Reviews

**Timeline**: 3-6 months (often longer).

**Characteristics**:
- **specialized scope**: reviewers are experts in the domain;
- **thorough evaluation**: multiple detailed reviews;
- **typically double-blind**: identities hidden;
- **higher bar**: acceptance rate 5-20\%.

**Your review should be comprehensive**:
- detailed assessment of methodology;
- thorough examination of results;
- comparison to related work;
- constructive feedback for improvement.

### Open-Science and Preprint Review

**Preprints** (arXiv, bioRxiv, medRxiv):
- unvetted, rapid dissemination;
- **you can comment publicly** on preprints;
- valuable for catching errors before journal acceptance;
- community review complements formal peer review.

**Advantages**:
- faster feedback to authors;
- public accountability (trolling risk, but also prevents editorial bias);
- archival record of review process.

## Reviewing Your Own Work: Personal Research

### Reading Papers in Your Field

As a researcher, you read papers to:
- **keep current**: understand new methods, results, trends;
- **find prior art**: for literature reviews, novelty claims;
- **learn techniques**: understand how to apply methods;
- **evaluate claims**: decide what to build on.

Apply the same critical reading to papers you consider building on.

### Detecting Over-Claimed Results

**Common over-claims**:
- "state-of-the-art" vs. old baselines;
- "efficient" vs. naive implementation;
- "robust" on similar distributions;
- "solves" one variant of problem.

**Check**:
- what exactly was measured?
- are baselines standard?
- what limitations are acknowledged?
- does it work on your data?

### Integrating External Code

Before using an implementation:

**Check**:
- does code match described algorithm?
- results match paper numbers?
- well-documented?
- reproducibility issues?

### Building a Personal Research Notebook

As you read papers:
- record your assessment of contribution and evidence;
- note red flags and questionable claims;
- track which papers build on which;
- plan validation experiments.

This helps you avoid repeating mistakes and find improvement opportunities.

## Common Mistakes Reviewers Make

### Mistakes to Avoid: Fairness

**Being too harsh**:
- rejecting papers for incompleteness;
- expecting perfection;
- criticizing authors instead of work.

**Being too lenient**:
- accepting obvious flaws;
- not asking for evidence;
- following the herd consensus.

### Mistakes to Avoid: Bias and Scope

**Over-scoping**:
- expecting theory in empirical papers or vice versa;
- reviewing outside your expertise.

**Conflicts of interest**:
- reviewing papers citing your work;
- reviewing competitors;
- not declaring conflicts;
- promoting your own work.

### Staying Objective

**Bias mitigation**:
- review the work, not the authors or their affiliations;
- be aware of your own biases (field biases, methodological biases);
- if you're too close to the topic, consider declining the review;
- re-read your review for unfair language before submitting.

**When to decline**:
- you lack expertise in the method or domain;
- you have a conflict of interest;
- you don't have time to do a thorough review;
- you dislike the authors or their prior work (this affects objectivity).

## Summary and Practical Advice

### Key Principles

1. **be a critical reader**: scrutinize methodology, results, and claims;
2. **distinguish honest errors from manipulation**: errors are common, malice is rare;
3. **check for red flags** in statistics, methodology, and presentation;
4. **be constructive**: provide feedback that helps authors improve;
5. **stay objective**: review the work, not the authors;
6. **know your limits**: don't review outside your expertise.

### Reviewing Checklist

~~~
{\footnotesize
\begin{enumerate}
  \item Read the abstract and introduction to understand the scope
  \item Identify the main claims and evidence
  \item Check methodology for red flags (data leakage, unfair comparisons, weak baselines)
  \item Assess statistical rigor (error bars, significance tests, multiple comparisons)
  \item Look for cherry-picked results or selective reporting
  \item Verify that conclusion matches the evidence
  \item Check clarity of writing and reproducibility claims
  \item Consider whether the work is novel and significant
  \item Write a fair, constructive review
  \item Declare any conflicts of interest
\end{enumerate}
}
~~~

### Resources

**For deeper learning**:
- NIH: Guidelines for responsible conduct of research;
- Ioannidis (2005): "Why Most Published Research Findings Are False";
- Gelman and Loken (2013): "The garden of forking paths";
- open science frameworks: Open Science Foundation, FAIR data principles;
- domain-specific guidelines: ML reproducibility standards, computational science practice guides.