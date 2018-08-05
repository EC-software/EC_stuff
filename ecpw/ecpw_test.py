import unittest
import os.path

import ecpw


class EcpwTestCase(unittest.TestCase):
    """ Tests for ecpw.py """

    # def test_something_hopefully_succeeding(self):
    #     """ Is xxx really succeeding? """
    #     self.assertTrue(ecpw.some_func('some_value') == 'some_other_value')

    # Module global variables

    def test_ECPW_DATATYPE(self):
        """ Is ECPW_DATATYPE corect? """
        ecs = ecpw.Store()
        self.assertTrue(ecs.ECPW_DATATYPE == "ECPW")
        self.assertTrue(ecs.ECPW_VERSION == "0.1")

    # Module __init__()

    def test_init_w_empty_input(self):
        """ Is the __init__() working as expected? """
        ecs = ecpw.Store()
        self.assertTrue(ecs._filen == os.path.expanduser("~")+"/.ecpw")
        self.assertTrue(ecs._crypt == None)
        self.assertTrue(isinstance(ecs._base, dict))


if __name__ == '__main__':
    unittest.main()
