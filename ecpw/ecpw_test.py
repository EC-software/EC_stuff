import unittest
import ecpw

class ecpwTestCase(unittest.TestCase):
    """ Tests for ecpw.py """

    # def test_something_hopefully_succeeding(self):
    #     """ Is xxx really succeeding? """
    #     self.assertTrue(ecpw.some_function('some_value') == 'some_other_value')


    def test_ECPW_DATATYPE(self):
        """ Is ECPW_DATATYPE corect? """
        ecs = ecpw.Store()
        self.assertTrue(ecs.ECPW_DATATYPE == "ECPW")

if __name__ == '__main__':
    unittest.main()
