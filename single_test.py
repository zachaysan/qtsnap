import unittest
from tests.test_user import Test_retrieve_user
from tests.test_photo_stream import Test_photo_stream

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test_photo_stream('test_photo_is_actually_popular'))
    return suite


def main():
    s = suite()
    all_tests = unittest.TestSuite([s])
    unittest.TextTestRunner().run(all_tests)

if __name__ == '__main__':
    main()
