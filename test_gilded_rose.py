# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)
        
    

    # #First logical errors
    def test_normal_item_decreases_in_quality(self):
        items = [Item("+5 Dexterity Vest", 5, 10)]  
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 8)  
        self.assertEqual(items[0].sell_in,3)  
        
    # #Second logical errors
    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 12)  
        self.assertEqual(items[0].sell_in, 1)  
        
    # Third logical errors
    def test_backstage_passes_quality_drops_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(items[0].quality, 29)  
    
    # Fourth logical errors
    def test_conjured_mona_cake_decrease_in_quality(self):
        items = [Item("Conjured Mona Cake", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        
        self.assertEqual(items[0].quality, 25)
    
    
    #Syntax error
    def test_gilded_rose_list_all_items_again(self):
        items = [Item("Aged Brie", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Aged Brie"], all_items)
    
    #Second Syntax error
    def test_gilded_rose_conjured_mona_cake(self):
        items = [Item("Conjured Mona Cake", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.sell_item()
        self.assertEqual(["Conjured Mona Cake"], all_items)

if __name__ == '__main__':
    unittest.main()
