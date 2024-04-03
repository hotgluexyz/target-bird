"""Bird target sink class, which handles writing streams."""
from target_bird.client import BirdSink


class ContactsSink(BirdSink):
    """Bird target sink class."""

    endpoint = "/contacts"
    name = "contacts"

    def upsert_record(self, record: dict, context: dict):
        state_updates = dict()
        # default method is create contacts
        method = "POST"

        if record:
            # build endpoint if workspace is provided in the record
            # (in case of working with multiple workspaces on the same job)
            workspace_id = record.pop("workspace_id", None) or self.config.get(
                "workspace_id"
            )
            if not workspace_id:
                raise Exception(
                    "Error: No workspace_id was provided in the config or in the record"
                )
            endpoint = f"workspaces/{workspace_id}{self.endpoint}"

            # if identifiers are provided use method create or patch by identifier
            identifiers = record.get("identifiers")
            if identifiers or []:
                identifier_key = identifiers[0].get("key")
                identifier_value = identifiers[0].get("value")

                if identifier_key and identifier_value:
                    method = "PATCH"
                    endpoint = (
                        f"{endpoint}/identifiers/{identifier_key}/{identifier_value}"
                    )
                else:
                    raise Exception(
                        f"Error: Identifiers data is incomplete for Key {identifier_key} and Value {identifier_value}"
                    )

            response = self.request_api(method, endpoint=endpoint, request_data=record)
            res_id = response.json()["id"]
            self.logger.info(f"Contact created or updated succesfully with id {res_id}")
            return res_id, True, state_updates
