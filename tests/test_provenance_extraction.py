import unittest

from stage_03_candidate_provenance_extractor.cpe_pdb import (
    parse_fields, majority_vote, extract_components, build_record,
)
from stage_04_rule_generator.rule_generator import RDB, apply_rules

LOG = """Process ID: 12
Process Name: C:\\Program Files\\app.exe
Object ID: 34
Object Name: C:\\data.txt
Accesses: WriteData
Time: 10:20:30"""
RULES = RDB["windows_file_access_4663"]


class ProvenanceTests(unittest.TestCase):
    def test_fields_preserve_colons_and_paths(self):
        fields = parse_fields(LOG)
        self.assertEqual(fields["Time"], "10:20:30")
        self.assertTrue(fields["Process Name"].startswith("C:"))

    def test_votes_and_ties(self):
        self.assertEqual(majority_vote(["a", "b", "b"]), "b")
        self.assertEqual(majority_vote(["b", "a"]), "b")
        with self.assertRaises(ValueError):
            majority_vote([])

    def test_forward_record_matches_rules(self):
        record = build_record(*extract_components(LOG, ["12->34"]))
        self.assertEqual(record, apply_rules(LOG, RULES))
        self.assertEqual(len(record), 8)
        self.assertEqual(record["Itype"], "WRITE")

    def test_reverse_direction_preserves_entity_types(self):
        record = build_record(*extract_components(LOG, ["34->12"]))
        self.assertEqual((record["Sid"], record["Stype"]), ("34", "file"))
        self.assertEqual((record["Did"], record["Dtype"]), ("12", "process"))
        with self.assertRaises(ValueError):
            extract_components(LOG, ["invalid"])

    def test_read_and_windows_newlines(self):
        log = LOG.replace("WriteData", "ReadData").replace("\n", "\r\n")
        self.assertEqual(apply_rules(log, RULES)["Itype"], "READ")
        self.assertEqual(build_record(*extract_components(log, ["12->34"]))["Itype"], "READ")

    def test_missing_blank_and_unsupported_fields(self):
        for log in [LOG.replace("Process ID: 12\n", ""),
                    LOG.replace("Process ID: 12", "Process ID:"),
                    LOG.replace("WriteData", "DeleteData"),
                    LOG.replace("Object Name: C:\\data.txt", "Object Name:   ")]:
            with self.subTest(log=log):
                self.assertIsNone(extract_components(log, ["12->34"]))
                self.assertIsNone(apply_rules(log, RULES))

    def test_rules_reject_partial_ids(self):
        self.assertIsNone(apply_rules(LOG.replace("Process ID: 12", "Process ID: 12abc"), RULES))


if __name__ == "__main__":
    unittest.main()
