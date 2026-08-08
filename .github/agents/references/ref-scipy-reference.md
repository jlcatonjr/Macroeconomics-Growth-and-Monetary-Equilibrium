<!-- AGENTTEAMS:BEGIN content v=1 -->
# scipy Reference — MacroeconomicsGrowthMonetaryEquilibrium

> Quick-reference for **scipy ** (library) in MacroeconomicsGrowthMonetaryEquilibrium.
> This is a lightweight reference file, not an agent. For operational procedures, consult the tool's reference/skill document, or escalate to `@orchestrator`.

---

## Version

`scipy` ``

## Configuration

**Config files:** `N/A`

## Official Documentation

https://docs.scipy.org/doc/scipy/reference/

## Key API Surface

scipy.stats — probability distributions (norm, t, f, chi2, binom), hypothesis tests (ttest_ind, ttest_rel, mannwhitneyu, chi2_contingency, f_oneway), descriptive stats (describe, skew, kurtosis); scipy.optimize — minimize, curve_fit, root_scalar; scipy.linalg — solve, inv, det, eig

<!-- Document the primary classes, functions, or APIs that project code depends on from scipy. -->

## Common Patterns & Pitfalls

scipy.stats.norm.cdf/ppf for z-score and critical-value lookups. ttest_ind(a, b, equal_var=False) (Welch t-test) unless variances are verified equal. f_oneway(*groups) for one-way ANOVA. Pitfall: most distribution objects use scale (not variance) as the second parameter.

<!-- Document common usage patterns, best practices, and known issues for scipy . -->

## Key Conventions

- Follow project style rules when using scipy
- Refer to authority sources for API contract accuracy
- Validate changes against existing tests before committing

## Related Agents

- `@technical-validator` — verify technical accuracy of scipy usage
- `@primary-producer` — implements code that depends on scipy
<!-- AGENTTEAMS:END content -->
