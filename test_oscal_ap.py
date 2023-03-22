import json
from jsonschema import validate
import unittest

class OscalAssessmentPlanJsonSchemaTest(unittest.TestCase):
    def setUp(self):
        self.schema_path = 'oscal/json/schema/oscal_assessment-plan_schema.json'
        with open(self.schema_path) as fh:
            self.schema = json.load(fh)

    def test_empty_document(self):
        document_instance = {}
        validate(document_instance, schema=self.schema)

    def test_valid_oscal_document(self):
        pass

    def test_invalid_oscal_document(self):
        pass

if __name__ == '__main__':
    unittest.main()