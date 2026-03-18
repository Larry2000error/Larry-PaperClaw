# Contributing

Thanks for your interest in improving this project.

## Quick rules

- Keep secrets out of code (use env vars only).
- Keep changes small and focused.
- Preserve output compatibility when possible.
- Add a short test/repro step in PR description.

## Development flow

1. Fork and create a feature branch.
2. Make your changes.
3. Run a local sanity check:
   - `python3 scripts/cli.py doctor`
   - `python3 scripts/cli.py filter --dry-run --date YYYYMMDD`
   - `python3 scripts/cli.py digest --date YYYYMMDD --stats-json memory/rs_daily_stats_YYYYMMDD.json`
4. Update docs if behavior changed.
5. Open a PR with:
   - What changed
   - Why it changed
   - How you tested

## Suggested areas

- Better filtering quality
- Better filter configuration and prompt assets
- More robust LLM parsing/retries
- Digest quality checks
- Better observability/logging

## Security

If you find a security issue, please report privately before opening a public issue.
