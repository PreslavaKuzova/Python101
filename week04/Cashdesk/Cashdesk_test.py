import unittest
from Cashdesk import Bill, BillBatch

class TestCashdesk(unittest.TestCase):
    # def test_validation_of_the_data_when_given_argument_is_not_int_then_raise_exception(self):
    #     self.assertRaises(Exception, new_bill = Bill('10'))

    # def test_when_we_use_wrong_initialization_billbatch_data_then_throw_exception(self):
    #     self.assertRaises(Exception, BillBatch(['hello']))

    def test_how_the_custom_dunder_method_is_working(self):
        new_bill = Bill(10)
        expected_result = "A $10 bill"
        self.assertEqual(Bill.__str__(new_bill), expected_result)
        #another way of running this test is using str(new_bill)
    
    def test_how_the_custom_int_dunder_method_is_working(self):
        new_bill = Bill(5)
        expected_result = 5
        self.assertEqual(Bill.__int__(new_bill), expected_result)
    
    def test_how_the_custom_equal_dunder_method_is_working(self):
        bill1 = Bill(5)
        bill2 = Bill(5)
        self.assertTrue(bill1 == bill2)
    
    def test_how_the_custom_repr_method_is_working(self):
        new_bill = Bill(10)
        expected_result = "A $10 bill"
        self.assertEqual(Bill.__repr__(new_bill), expected_result)

if __name__ == '__main__':
    unittest.main()
