<!-- AGENTTEAMS:BEGIN content v=1 -->
# matplotlib Reference — MacroeconomicsGrowthMonetaryEquilibrium

> Quick-reference for **matplotlib ** (other) in MacroeconomicsGrowthMonetaryEquilibrium.
> This is a lightweight reference file, not an agent. For operational procedures, consult the tool's reference/skill document, or escalate to `@orchestrator`.

---

## Version

`matplotlib` ``

## Configuration

**Config files:** `N/A`

## Official Documentation

https://matplotlib.org/stable/api/

## Key API Surface

Functional interface (plt.plot, plt.scatter, plt.hist, plt.bar, plt.show); object-oriented interface (fig, ax = plt.subplots()); axes labels/titles/legends (ax.set_xlabel, ax.set_title, ax.legend); multiple subplots (plt.subplots(nrows, ncols)); saving figures (plt.savefig)

<!-- Document the primary classes, functions, or APIs that project code depends on from matplotlib. -->

## Common Patterns & Pitfalls

Prefer the OO interface (fig, ax = plt.subplots()) for multi-panel figures. Always set fig.tight_layout() before savefig to avoid clipped labels. Use plt.style.use('seaborn-v0_8') for publication-ready aesthetics. Pitfall: plt.show() clears the figure — call savefig before show.

<!-- Document common usage patterns, best practices, and known issues for matplotlib . -->

## Key Conventions

- Follow project style rules when using matplotlib
- Refer to authority sources for API contract accuracy
- Validate changes against existing tests before committing

## Related Agents

- `@technical-validator` — verify technical accuracy of matplotlib usage
- `@primary-producer` — implements code that depends on matplotlib
<!-- AGENTTEAMS:END content -->
