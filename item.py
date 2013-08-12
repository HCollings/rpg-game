#!/usr/bin/env python

try:
    import os
    import sys
except ImportError, err:
    print "cannot load module(s)"
    sys.exit(2)

class Item:

    count = 0
    
    def __init__(self, name, item_type):
        self.name = name
        self.item_type = item_type
        Item.count += 1

    def get_item_type(self):
        return self.item_type

    def destroy(self):
        Item.count -= 1

    def get_item_count():
        return Item.count
    get_item_count = staticmethod(get_item_count)

class Weapon(Item):

    def __init__(self, item):
        self.name = item["name"]
        Item.__init__(self, self.name, "weapon")

class Consumable(Item):

    def __init__(self, item):  
        self.name = item["name"]
        Item.__init__(self, self.name, "consumable")
        self.health_modifier = item["health_modifier"]
        self.mana_modifier = item["mana_modifier"]

    def get_health_modifier(self):
        return self.health_modifier

    def get_mana_modifier(self):
        return self.mana_modifier
