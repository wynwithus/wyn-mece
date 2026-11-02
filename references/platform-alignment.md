# Package Portability Notes

These notes describe this package's design, not a certification of behavior in every assistant.

- `SKILL.md` contains the name, discovery description, core workflow, and links to supporting references.
- `agents/openai.yaml` provides optional Codex interface metadata and permits automatic selection. Other hosts may ignore it.
- `references/` provides detail loaded only when the task needs it.
- Python helpers use the standard library and require Python 3.10 or later.
- The skill's core analysis requires an assistant that can read the instructions and supporting files. Image reconstruction additionally requires access to the source image and image-reading capabilities.
- Native installation and invocation depend on the host. Keep the folder named `wyn-mece` and preserve relative paths.
- Static validation, reviewer judgments, and target-client runtime measurements are distinct evidence classes. Do not infer activation accuracy or output-quality improvements from packaging checks.

The evaluation harness separates activation cases from output assertions and supports with-skill and without-skill comparisons through a caller-supplied adapter. See [the evaluation contract](../evals/README.md).
