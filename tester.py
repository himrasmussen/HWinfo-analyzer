import unittest
import os
<<<<<<< HEAD
from hwinfo_analyze import main
=======
from app.hwinfo_analyze import main
>>>>>>> 75916ad651dea5af819c8e12dab1ed29d5662b69

class MainTestCase(unittest.TestCase):
    """Test if the analyzer works without fails."""

    def test_ALL_THE_CSVS(self):
        """Test all the csv files."""
        for csv in os.listdir("testfiles"):
            main(os.path.join("testfiles", csv))



unittest.main()
