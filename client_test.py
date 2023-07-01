import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      bid = quote['top_bid']['price']
      ask = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid + ask) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      bid = quote['top_bid']['price']
      ask = quote['top_ask']['price']
      self.assertEqual(getDataPoint(quote), (quote['stock'], bid, ask, (bid + ask) / 2))

  def test_getRatio_invalid_price(self):
    second_prices = [0, 'a', True]

    self.assertIsNone(getRatio(1, [second_price for second_price in second_prices]))

  def test_getRatio_valid_prices(self):
    prices = {(1, 2): 0.5, (3, 29): 3/29}

    for price in prices:
      self.assertEqual(getRatio(*price), prices[price])


if __name__ == '__main__':
    unittest.main()
