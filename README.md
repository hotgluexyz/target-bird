# target-bird

`target-bird` is a Singer target for Bird.

## Installation

```bash
pipx install target-bird
```

## Configuration

### Accepted Config Options

A full list of supported settings and capabilities for this
target is available by running:

```bash
target-bird --about
```

### Configure using environment variables

This Singer target will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Config variables

This target needs the following fields in the config file:
- `api_key` with the api_key provided by bird.
- `workspace_id` the workspace id provided by bird. 

Note: If you want to work with multiple workspaces add the workspace to each record's payload as `workspace_id`

### Source Authentication and Authorization

- [ ] `Developer TODO:` If your target requires special access on the source system, or any special authentication requirements, provide those here.

## Usage

You can easily run `target-bird` by itself or in a pipeline.

### Executing the Target Directly

```bash
target-bird --version
target-bird --help
# Test using the "Carbon Intensity" sample:
tap-carbon-intensity | target-bird --config /path/to/target-bird-config.json
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `target_bird/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `target-bird` CLI interface directly using `poetry run`:

```bash
poetry run target-bird --help
```

