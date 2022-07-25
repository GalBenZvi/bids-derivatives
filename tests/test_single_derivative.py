from pathlib import Path
from unittest import TestCase

from bids_derivatives.derivative import SingleSubjectDerivative
from bids_derivatives.utils.templates.bids import SUBJECT_TEMPLATE
from tests.fixtures import TEST_DERIVATIVES_PATH, TEST_SUBJECTS


class SingleDerivativeTestCase(TestCase):
    TEST_DATA_PATH = TEST_DERIVATIVES_PATH
    TEST_SUBJECTS = TEST_SUBJECTS

    def setUp(self) -> None:
        return super().setUp()

    def test_base_directory(self):
        """
        Test that the base directory is set correctly.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("valid")
            for subject in subjects:
                derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key, subject
                )
                self.assertTrue(
                    derivative.base_directory
                    == Path(self.TEST_DATA_PATH) / key
                )

    def test_valid_subjects(self):
        """
        Test that the subjects in the test data are valid.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("valid")
            for subject, info in subjects.items():
                derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key, subject
                )
            self.assertTrue(derivative.participant_label == subject)
            self.assertTrue(
                derivative.path
                == Path(self.TEST_DATA_PATH) / key / f"sub-{subject}"
            )

            self.assertTrue(
                len(derivative.sessions) == info.get("num_sessions")
            )

    def test_full_subject_identfier(self):
        """
        Test that the full subject identifier is set correctly.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("valid")
            for subject, info in subjects.items():
                derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key,
                    SUBJECT_TEMPLATE.format(subject=subject),
                )
                self.assertTrue(derivative.participant_label == subject)

    def test_invalid_subjects(self):
        """
        Test that the subjects in the test data are invalid.
        """
        for key, available_subjects in self.TEST_SUBJECTS.items():
            subjects = available_subjects.get("invalid")
            for subject in subjects:
                single_derivative = SingleSubjectDerivative(
                    Path(self.TEST_DATA_PATH) / key,
                    subject,
                )
                with self.assertRaises(ValueError):
                    single_derivative.get_participant_path()
                with self.assertRaises(ValueError):
                    single_derivative.get_available_sessions()
