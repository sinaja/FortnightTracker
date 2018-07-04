import unittest
from .context import source
from source.FortniteTrackerAPIClass import FortniteTrackerAPI

myTestFortniteTrackerAPI = source.FortniteTrackerAPIClass.FortniteTrackerAPI('xbl','AarashJ')
class Test_FortniteTrackerAPI(unittest.TestCase) :
    def test_SetUrl(self) :
        self.assertEqual(myTestFortniteTrackerAPI.SetUrl(), 'https://api.fortnitetracker.com/v1/profile/xbl/AarashJ')
        
    def test_GetUsername(self) :
        self.assertEqual(myTestFortniteTrackerAPI.GetUsername('./tests/TestStatistics.txt'), 'AarashJ')