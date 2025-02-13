# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: list[Item]):
        self.items = items
        self.updaters = {
            "Aged Brie": self.update_aged_brie,
            "Backstage passes to a TAFKAL80ETC concert": self.update_backstage_passes,
            "Sulfuras": self.update_sulfuras,
        }

    def update_quality(self):
        for item in self.items:
            updater = self.updaters.get(item.name, self.update_normal_item)
            if "Conjured" in item.name:
                updater = self.update_conjured_item  
            updater(item)

    def update_sulfuras(self, item):
        pass  
    
    def update_aged_brie(self, item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1  

    def update_backstage_passes(self, item):
        if item.quality < 50:
            item.quality += 1
            if item.sell_in <= 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in <= 5 and item.quality < 50:
                item.quality += 1
        if item.sell_in <= 0:
            item.quality = 0  
        item.sell_in -= 1

    

    def update_conjured_item(self, item):
        if item.quality > 0:
            item.quality -= 2
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2  
            
    def update_normal_item(self, item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1  

    def get_item(self):
        return [item.name for item in self.items]
