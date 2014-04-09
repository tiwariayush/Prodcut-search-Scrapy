# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class ProductItem(Item):
    # define the fields for your item here like:
    # name = Field()
    pass

class ProductDetails(Item):
   item_name=Field()
   item_price=field()
