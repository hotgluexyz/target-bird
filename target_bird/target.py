"""Bird target class."""

from singer_sdk import typing as th
from target_hotglue.target import TargetHotglue

from target_bird.sinks import ContactsSink


class TargetBird(TargetHotglue):
    """Sample target for Bird."""

    name = "target-bird"
    SINK_TYPES = [ContactsSink]

    config_jsonschema = th.PropertiesList(
        th.Property("api_key", th.StringType, required=True),
        th.Property(
            "workspace_id",
            th.StringType,
        ),
    ).to_dict()


if __name__ == "__main__":
    TargetBird.cli()
