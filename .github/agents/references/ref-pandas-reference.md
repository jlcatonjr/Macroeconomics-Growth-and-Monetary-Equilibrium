<!-- AGENTTEAMS:BEGIN content v=1 -->
# pandas Reference — MacroeconomicsGrowthMonetaryEquilibrium

> Quick-reference for **pandas ** (other) in MacroeconomicsGrowthMonetaryEquilibrium.
> This is a lightweight reference file, not an agent. For operational procedures, consult the tool's reference/skill document, or escalate to `@orchestrator`.

---

## Version

`pandas` ``

## Configuration

**Config files:** `N/A`

## Official Documentation

https://pandas.pydata.org/docs/reference/

## Key API Surface

DataFrame/Series creation and I/O (pd.read_csv, pd.read_excel, to_csv); indexing (.loc, .iloc, boolean indexing); groupby, merge/join, pivot_table; time-series (DatetimeIndex, resample, rolling); string methods (.str.*); missing data (dropna, fillna, isna)

<!-- Document the primary classes, functions, or APIs that project code depends on from pandas. -->

## Common Patterns & Pitfalls

Always set index explicitly after loading CSVs when a natural key exists. Use .copy() when slicing to avoid SettingWithCopyWarning. groupby().agg() for multi-stat summaries. pd.to_datetime() + dt accessor for time-series manipulation. Pitfall: chained indexing silently creates copies — use .loc.

<!-- Document common usage patterns, best practices, and known issues for pandas . -->

## Key Conventions

- Follow project style rules when using pandas
- Refer to authority sources for API contract accuracy
- Validate changes against existing tests before committing

## Related Agents

- `@technical-validator` — verify technical accuracy of pandas usage
- `@primary-producer` — implements code that depends on pandas
<!-- AGENTTEAMS:END content -->
