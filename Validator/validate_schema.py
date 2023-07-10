import json
import os
from jsonschema import validate, ValidationError


class JSONSchemaValidator:
    def __init__(self, schema_folder: str = "Validator/schemas") -> None:
        self.schema_folder = schema_folder

    def _load_schema(self, schema_type: str) -> dict:
        schema_file = os.path.join(self.schema_folder, f"{schema_type}.json")
        with open(schema_file, "r") as f:
            schema = json.load(f)
        return schema

    def validate_data(self, data: dict, schema_type: str) -> bool:
        schema = self._load_schema(schema_type)
        try:
            validate(instance=data, schema=schema)
            print("Validation successful. Data matches the schema.")
            return True
        except ValidationError as e:
            print("Validation failed. Data does not match the schema.")
            return False


# Usage example
validator = JSONSchemaValidator()
data = {
    "edges": [
        {
            "temp": "temp",
            "source": "1.15 Pre-mortem",
            "type": "FILLED_IN_BY",
            "target": "https://docs.google.com/spreadsheets/d/1IF8YGAKKMPrwQMP0aWMDTkkbcT44JdauRfY1-WoEj_U/edit#gid=0[[.underline]#pre-mortems spreadsheet#]"
        },
        {
            "source": "1.16 All author’s decision-supporting data",
            "type": "LINKED_TO"
        },
        {
            "source": "1.17 A spec statement",
            "type": "FACTUALLY_INCORRECT",
            "target": "Amazon Redshift uses Oracle as its underlying engine"
        },
        {
            "source": "1.18 A part of the document",
            "type": "CONTRADICTS",
            "target": "choosing one option in an ITD, then writing milestones for a different one"
        }
    ]
}

schema_type = "edges_schema"

validator.validate_data(data, schema_type)
