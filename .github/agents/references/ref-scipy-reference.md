# Scipy Reference — MacroeconomicsGrowthMonetaryEquilibrium

> Quick-reference for **Scipy** in MacroeconomicsGrowthMonetaryEquilibrium.
> This is a lightweight reference file, not a full agent.

---

## Official Documentation

https://docs.scipy.org/doc/scipy/reference/

## Key API Surface

scipy.stats — probability distributions (norm, t, f, chi2, binom), hypothesis tests (ttest_ind, ttest_rel, mannwhitneyu, chi2_contingency, f_oneway), descriptive stats (describe, skew, kurtosis); scipy.optimize — minimize, curve_fit, root_scalar; scipy.linalg — solve, inv, det, eig

## Common Patterns & Pitfalls

scipy.stats.norm.cdf/ppf for z-score and critical-value lookups. ttest_ind(a, b, equal_var=False) (Welch t-test) unless variances are verified equal. f_oneway(*groups) for one-way ANOVA. Pitfall: most distribution objects use scale (not variance) as the second parameter.

## Key Conventions

- Follow project style rules when using Scipy
- Refer to authority sources for API contract accuracy

## Related Agents

- `@technical-validator` — verify technical accuracy of Scipy usage
- `@primary-producer` — implements code that depends on Scipy
