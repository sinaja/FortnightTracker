import unittest
from FortniteTrackerAPIClass import FortniteTrackerAPI
from FortniteTrackerAPIClass import Input

class testInput(Input):
    testString = '' 
    def __init__(self, testInput) :
        self.testString = testInput

    def GetInput(self, a):
        return self.testString
        
myTestFortniteTrackerAPI = FortniteTrackerAPI()
class Test_FortniteTrackerAPI(unittest.TestCase) :
    def test_SetUrl(self):
        myTestPlatform = testInput('xbl')
        myTestUser = testInput('AarashJ')
        self.assertEqual(myTestFortniteTrackerAPI.SetUrl(myTestPlatform, myTestUser), 'https://api.fortnitetracker.com/v1/profile/xbl/AarashJ')