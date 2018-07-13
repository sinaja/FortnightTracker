import unittest
from .context import source
from source.FortniteTrackerAPIClass import FortniteTrackerAPI

myTestFortniteTrackerAPI = source.FortniteTrackerAPIClass.FortniteTrackerAPI('xbl','AarashJ')
class Test_FortniteTrackerAPI(unittest.TestCase) :
    def test_SetUrl(self) :
        self.assertEqual(myTestFortniteTrackerAPI.SetUrl(), 'https://api.fortnitetracker.com/v1/profile/xbl/AarashJ')
        
    def test_GetUsername(self) :
        self.assertEqual(myTestFortniteTrackerAPI.GetUsername('./tests/TestStatistics.txt'), 'AarashJ')

    def test_ValidateStats(self) :
        self.assertTrue(myTestFortniteTrackerAPI.ValidateStats('./tests/TestStatistics.txt'))
        self.assertFalse(myTestFortniteTrackerAPI.ValidateStats('./tests/TestStatistics2.txt'))

    def test_GetSoloWins(self) :
        self.assertEqual(int(source.FortniteTrackerAPIClass.FortniteTrackerAPI.GetSoloWins(source.FortniteTrackerAPIClass.FortniteTrackerAPI.GetSoloWins, './tests/TestStatistics.txt')), 110)
    
    def test_GetSoloTops(self) :
        self.assertEqual(int(source.FortniteTrackerAPIClass.FortniteTrackerAPI.GetSoloTops(source.FortniteTrackerAPIClass.FortniteTrackerAPI.GetSoloWins, './tests/TestStatistics.txt')), 831)

        