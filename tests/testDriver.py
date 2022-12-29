import unittest
import sys
sys.path.append('/Users/a23135334/Documents/python-pip-starter-kit/')
from src.driver import Driver

class PaymentBalanceLoanTest(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_loanBalance(self):
        """Whether output is correct generated with only loan and balance statements"""
        input = open('tests/resources/input/loan_balance.txt', 'r').readlines()
        outputFile = open('tests/resources/output/loan_balance_output.txt','r').readlines()
        output = [line.split() for line in outputFile]
        self.assertEqual(self.driver.runApp(input),output)
        

    def test_loanOnly(self):
        """Whether output is correct generated with only loan statements"""
        input = open('tests/resources/input/loan_only.txt', 'r').readlines()
        output = []
        self.assertEqual(self.driver.runApp(input),output)
    
    def test_loanPaymentBalance(self):
        """Whether output is correct generated with loan, payment and balance statements"""
        input = open('tests/resources/input/loan_payment_balance.txt', 'r').readlines()
        outputFile = open('tests/resources/output/loan_payment_balance_output.txt','r').readlines()
        output = [line.split() for line in outputFile]
        self.assertEqual(self.driver.runApp(input),output)
    

    

if __name__ == '__main__':
    unittest.main()
