# Evaluation Harness

This package separates **activation evaluation** from **output-quality evaluation** and supports fresh-run comparisons with and without the skill.

## Static validation

```bash
python evals/run_evals.py validate
python scripts/validate_skill.py .
```

These commands validate package structure, eval definitions, referenced fixtures, Python syntax, JSON parsing, Markdown links, and deterministic partition and numeric-interval fixtures. They do not measure model behavior.

## Runtime adapter contract

Use an adapter executable for the target ChatGPT/Codex or Claude environment. The harness sends one JSON object on standard input:

```json
{
  "condition": "with_skill",
  "adapter_contract_version": "1.0",
  "case": {
    "suite": "trigger",
    "id": "explicit-make-mece",
    "query": "...",
    "skill_path": "/absolute/path/to/wyn-mece"
  }
}
```

For a trigger case, return:

```json
{
  "activated": true,
  "response": "optional captured response",
  "duration_ms": 1250,
  "input_tokens": 0,
  "output_tokens": 0
}
```

For an output case, return blinded assertion grades in the same order as the case definition:

```json
{
  "response": "captured response",
  "assertion_results": [true, true, false],
  "grader_score": 86,
  "duration_ms": 2400,
  "input_tokens": 0,
  "output_tokens": 0
}
```

The adapter receives the full evaluation record for orchestration. Keep `should_trigger`, `expected_output`, and `assertions` hidden from the task-performing model. Give that model only the user query or prompt, supplied source files, and the skill when the condition allows it. Give assertion text and expected outputs only to a separate grader after the response is frozen. A trigger run must exercise discovery rather than preloading the full skill simply because its path is present.

The adapter controls whether the skill is loaded. Honor `condition` exactly. Run every case in a fresh session and keep graders blind to condition where practical.

## Run and compare

```bash
python evals/run_evals.py run \
  --adapter "python /path/to/target_adapter.py" \
  --suite all \
  --condition with_skill \
  --results evals/artifacts/with-skill.jsonl

python evals/run_evals.py run \
  --adapter "python /path/to/target_adapter.py" \
  --suite all \
  --condition without_skill \
  --results evals/artifacts/without-skill.jsonl

python evals/run_evals.py summarize \
  evals/artifacts/with-skill.jsonl \
  evals/artifacts/without-skill.jsonl \
  --output evals/artifacts/benchmark-summary.json
```

The summary reports trigger precision, recall, and accuracy; full-assertion output pass rate; mean assertion rate; optional grader score; latency; and with-skill minus without-skill deltas.

No empirical results are bundled. Populate them only from actual target-client runs.

The summarizer reports malformed or incomplete assertion lists as `invalid_records`; they do not count as graded cases or full passes. Compare matched case sets and inspect invalid records and adapter failures before interpreting a benchmark delta.
