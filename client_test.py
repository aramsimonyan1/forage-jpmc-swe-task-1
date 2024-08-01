import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    # test case where bid price is less than ask price
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Test for stock ABC
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 120.48)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, (120.48 + 121.2) / 2)
        
    # Test for stock DEF
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    self.assertEqual(stock, 'DEF')
    self.assertAlmostEqual(bid_price, 117.87)
    self.assertAlmostEqual(ask_price, 121.68)
    self.assertAlmostEqual(price, (117.87 + 121.68) / 2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    # Define a test case where bid price is greater than ask price
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    # Test for stock ABC
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 120.48)
    self.assertAlmostEqual(ask_price, 119.2)
    self.assertAlmostEqual(price, (120.48 + 119.2) / 2)
        
    # Test for stock DEF
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    self.assertEqual(stock, 'DEF')
    self.assertAlmostEqual(bid_price, 117.87)
    self.assertAlmostEqual(ask_price, 121.68)
    self.assertAlmostEqual(price, (117.87 + 121.68) / 2)


  def test_getDataPoint_missingFields(self):
    # Define a test case where fields are missing
    quotes = [
      {'top_ask': {'price': 121.2}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
        
    # Test for stock ABC (Expecting it to handle missing fields gracefully)
    stock, bid_price, ask_price, price = getDataPoint(quotes[0])
    self.assertEqual(stock, 'ABC')
    self.assertAlmostEqual(bid_price, 120.48)
    self.assertAlmostEqual(ask_price, 121.2)
    self.assertAlmostEqual(price, (120.48 + 121.2) / 2)
        
    # Test for stock DEF (Expecting it to handle missing fields gracefully)
    stock, bid_price, ask_price, price = getDataPoint(quotes[1])
    self.assertEqual(stock, 'DEF')
    self.assertAlmostEqual(bid_price, 117.87)
    self.assertAlmostEqual(ask_price, 121.68)
    self.assertAlmostEqual(price, (117.87 + 121.68) / 2)

  def test_getRatio(self):
    # Define a test case for getRatio function
    from client3 import getRatio
        
    # Test ratio with normal values
    ratio = getRatio(120.0, 100.0)
    self.assertAlmostEqual(ratio, 1.2)
        
    # Test ratio with zero denominator
    ratio = getRatio(120.0, 0)
    self.assertIsNone(ratio)


if __name__ == '__main__':
    unittest.main()
