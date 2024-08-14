import unittest
import subprocess

class TestNumberClassification(unittest.TestCase):
    def run_script(self, *args):
        """Run the Python script and capture its output."""
        result = subprocess.run(['python3', 'number_classification.py'],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                text=True)
        return result.stdout.strip()

    def test_output(self):
        expected_output = "\n".join([
            "Number 1 is Odd",
            "Number 2 is Even",
            "Number 3 is Odd",
            "Number 4 is Even",
            "Number 5 is Odd",
            "Number 6 is Even",
            "Number 7 is Odd",
            "Number 8 is Even",
            "Number 9 is Odd",
            "Number 10 is Even"
        ])
        output = self.run_script()
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
