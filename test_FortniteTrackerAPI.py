import unittest
from FortniteTrackerAPIClass import FortniteTrackerAPI

myTestFortniteTrackerAPI = FortniteTrackerAPI('xbl','AarashJ')
class Test_FortniteTrackerAPI(unittest.TestCase) :
    def test_SetUrl(self):
        self.assertEqual(myTestFortniteTrackerAPI.SetUrl(), 'https://api.fortnitetracker.com/v1/profile/xbl/AarashJ')