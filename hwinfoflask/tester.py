import unittest
import os

#from . import hwinfo_analyze

class MainTestCase(unittest.TestCase):
    """Test if the analyzer works without fails."""

    def test_ALL_THE_CSVS(self):
        """Test all the csv files."""
        for csv in os.listdir("testfiles"):
            if csv.lower().endswith(".csv"):
                print(csv)
                hwinfo_analyze.main(os.path.join("testfiles", csv))



if __name__ == "__main__":
    unittest.main()
