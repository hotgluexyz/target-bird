# target-bird

`target-bird` is a Singer target for Bird.

Build with the `Hotglue Target SDK`.

## Configuration

### Configure using environment variables

This Singer target will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

Config file can also be created inside `.secrets` folder as a json file.

example:

``` json
{
    "workspace_id": "000000-0000-0000-0000-000000000",
    "api_key": "your_api_key"
}
```

### Config variables

This target needs the following fields in the config file:
- `api_key` with the api_key provided by bird.
- `workspace_id` the workspace id provided by bird. 

Note: If you want to work with multiple workspaces add the workspace to each record's payload as `workspace_id`

## Usage

You can easily run `target-bird` by itself or in a pipeline.

### Executing the Target Directly

```bash
target-bird --version
target-bird --help
```

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Input data

Input data can be put in a singer or txt file inside `.secrets` folder. A sample payload is in `sample_payload` folder.


### Create and Run Tests

You can test the `target-bird` CLI interface directly using `poetry run`:

```bash
poetry run target-bird --config ./.secrets/config.json < ./.secrets/data.singer > ./.secrets/target-state.json
```

Note:
- The command above needs both `config.json` and `data.singer` file inside `.secrets` folder.
- The state of the target (count of succesful or failed records) will be written to `target-state` json file.

