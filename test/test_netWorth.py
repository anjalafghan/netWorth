import unittest
from  GetNetworth import GetNetworth

class showNetworth(unittest.TestCase):

    def test_show_net_worth_returns_a_float(self):
        networth = GetNetworth()
        asset = networth.getAsset()
        liability = networth.getLiability()
        val = networth.calculateNetworth(asset,liability)
        self.assertIsInstance(val,float)
        
    def test_show_net_worth_returns_net_worth(self):
        networth = GetNetworth()
        asset = networth.getAsset()
        liability = networth.getLiability()
        val = networth.calculateNetworth(asset,liability)
        self.assertEqual(val,1.0)
        
    def test_show_net_worth_calculates_mortgage(self):
        networth = GetNetworth()
        mortgage = networth.getMortgage()
        self.assertEqual(mortgage,150.0)
    
    