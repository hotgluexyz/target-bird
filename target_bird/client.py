import ast
import json

from target_hotglue.client import HotglueSink


class BirdSink(HotglueSink):

    api_version = "v23_1"
    base_url = "https://api.bird.com/"

    @property
    def http_headers(self):
        auth_credentials = {"Authorization": f"AccessKey {self.config.get('api_key')}"}
        return auth_credentials

    def validate_input(self, record: dict):
        return self.unified_schema(**record).dict()

    def parse_objs(self, obj):
        try:
            try:
                return ast.literal_eval(obj)
            except:
                return json.loads(obj)
        except:
            return obj

    def clean_data(self, value):
        try:
            value = self.convert_date(value)
        except:
            if isinstance(value, str) and (
                value.startswith("[") or value.startswith("{")
            ):
                value = self.parse_objs(value)
        return value

    def preprocess_record(self, record: dict, context: dict) -> None:
        """Process the record."""
        for key, value in record.items():
            record[key] = self.clean_data(value)
        return record
