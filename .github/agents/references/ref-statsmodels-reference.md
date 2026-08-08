<!-- AGENTTEAMS:BEGIN content v=1 -->
# statsmodels Reference — MacroeconomicsGrowthMonetaryEquilibrium

> Quick-reference for **statsmodels ** (library) in MacroeconomicsGrowthMonetaryEquilibrium.
> This is a lightweight reference file, not an agent. For operational procedures, consult the tool's reference/skill document, or escalate to `@orchestrator`.

---

## Version

`statsmodels` ``

## Configuration

**Config files:** `N/A`

## Official Documentation

https://www.statsmodels.org/stable/api.html

## Key API Surface

OLS regression (sm.OLS, smf.ols); GLM (sm.GLM); time-series models (ARIMA, SARIMAX, VAR); diagnostic tests (acf/pacf, Durbin-Watson, Breusch-Pagan, White test); summary tables (.summary(), .summary2()); formula interface (smf.ols('y ~ x1 + x2', data=df).fit())

<!-- Document the primary classes, functions, or APIs that project code depends on from statsmodels. -->

## Common Patterns & Pitfalls

Always call .fit() — the model object alone is not fitted. Use smf formula interface for clean model specification with categorical dummies. model.summary() prints LaTeX-ready tables. Use HC3 robust standard errors: .fit(cov_type='HC3'). Pitfall: sm.add_constant(X) must be called explicitly when using sm.OLS with arrays.

<!-- Document common usage patterns, best practices, and known issues for statsmodels . -->

## Key Conventions

- Follow project style rules when using statsmodels
- Refer to authority sources for API contract accuracy
- Validate changes against existing tests before committing

## Related Agents

- `@technical-validator` — verify technical accuracy of statsmodels usage
- `@primary-producer` — implements code that depends on statsmodels
<!-- AGENTTEAMS:END content -->
