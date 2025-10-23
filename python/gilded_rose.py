# -*- coding: utf-8 -*-

MAX_QUALITY = 50
MIN_QUALITY = 0

#Est utilise pour chaques items present sauf exception
def bornage_quality(item):
    if item.quality > MAX_QUALITY:
        item.quality = MAX_QUALITY
    elif item.quality < MIN_QUALITY:
        item.quality = MIN_QUALITY

def normal_item(item):
    item.sell_in -= 1

    if item.sell_in >= 0 :
        item.quality -= 1
    else : 
        item.quality -= 2
    bornage_quality(item)

def aged_brie_item(item):
    item.sell_in -= 1

    if item.sell_in >= 0: 
        item.quality += 1 
    else : 
        item.quality += 2
    bornage_quality(item)

def sulfuras_item(item):
    item.quality = 80

def backstage_item(item):
    if item.sell_in > 10 :
        item.quality += 1 
    elif item.sell_in > 5:
        item.quality += 2 
    else :
        item.quality += 3 
    
    item.sell_in -= 1

    if item.sell_in < 0:
        item.quality = 0
    else: 
        bornage_quality(item)


def conjured_item(item):
    item.sell_in -= 1

    if item.sell_in >= 0 :
        item.quality -= 2
    else : 
        item.quality -= 4
    bornage_quality(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                sulfuras_item(item)
            elif item.name == "Aged Brie":
                aged_brie_item(item)  
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                backstage_item(item)
            elif "Conjured" in item.name:
                conjured_item(item) 
            else:
                normal_item(item)     

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
