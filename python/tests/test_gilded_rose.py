# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, normal_item, aged_brie_item, sulfuras_item, backstage_item, conjured_item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_avant_expiration(self):
        item = Item("Normal Item", 5, 10)
        normal_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 9)
    
    def test_normal_baisse_apres_expiration(self):
        item = Item("Normal Item", 0, 10)
        normal_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 8)

    def test_normal_qualite_maximale(self):
        item = Item("Normal Item", 5, 55)
        normal_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    def test_normal_qualite_minimale(self):
        item = Item("Normal Item", 5, 0)
        normal_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 0)

###############################################

    def test_aged_brie_qualite_normale(self):
        item = Item("Aged Brie", 5,10)
        aged_brie_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 11)

    def test_aged_brie_qualite_apres_date(self):
        item = Item("Aged Brie", 0,10)
        aged_brie_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 12)
    
    def test_aged_brie_qualite_maximale(self):
        item = Item("Aged Brie", 5,60)
        aged_brie_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    def test_aged_brie_qualite_minimale(self):
        item = Item("Aged Brie", 5,-10)
        aged_brie_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 0)

##################################################

    def test_sulfuras_avant_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
        sulfuras_item(item)
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 80)

    def test_sulfuras_apres_date(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        sulfuras_item(item)
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

#############################################################

    def test_backstage_item_condition_top(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 12, 12)
        backstage_item(item)
        self.assertEqual(item.sell_in, 11)
        self.assertEqual(item.quality, 13)

    def test_backstage_item_condition_mid(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 10)
        backstage_item(item)
        self.assertEqual(item.sell_in, 8)
        self.assertEqual(item.quality, 12)

    def test_backstage_item_condition_bottom(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 4, 3)
        backstage_item(item)
        self.assertEqual(item.sell_in, 3)
        self.assertEqual(item.quality, 6)
    
    def test_backstage_date_depassee(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
        backstage_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)
    
    def test_backstage_qualite_max(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 60)
        backstage_item(item)
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 50)
    
###################################################

    def test_conjured_avant_expiration(self):
        item = Item("Conjured Mana Cake", 5, 10)
        conjured_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 8)

    def test_conjured_apres_expiration(self):
        item = Item("Conjured Mana Cake", 0, 10)
        conjured_item(item)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 6)
    
    def test_conjured_quality_max(self):
        item = Item("Conjured Mana Cake", 5, 58)
        conjured_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 50)

    def test_conjured_quality_min(self):
        item = Item("Conjured Mana Cake", 5, 0)
        conjured_item(item)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 0)

        
if __name__ == '__main__':
    unittest.main()
