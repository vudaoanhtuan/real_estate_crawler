# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime


def strip_text(text):
    try: text = str.strip(text)
    except: pass
    return text

def convert_float(text):
    try: text = float(text)
    except: pass
    return text

def convert_int(text):
    try: text = int(text)
    except: pass
    return text


class RealEstateItem(Item):
    post_url = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    post_title = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    post_date = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    post_detail = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())

    post_author_url = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    post_author_name = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())  
    post_author_phone = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())

    post_images = Field()

    re_type = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_price = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())

    re_width = Field(input_processor=MapCompose(convert_float), output_processor=TakeFirst())
    re_length = Field(input_processor=MapCompose(convert_float), output_processor=TakeFirst())
    re_area = Field(input_processor=MapCompose(convert_float), output_processor=TakeFirst())
    re_area_to_use = Field(input_processor=MapCompose(convert_float), output_processor=TakeFirst())

    re_direction = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_legal = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())

    re_num_floors = Field(input_processor=MapCompose(convert_int), output_processor=TakeFirst())
    re_bathroom = Field(input_processor=MapCompose(convert_int), output_processor=TakeFirst())
    re_bedroom = Field(input_processor=MapCompose(convert_int), output_processor=TakeFirst())
    
    re_addr_full = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_city = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_district = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_ward = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_street_name = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_street_number = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
    re_addr_building = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())

    re_agency = Field(input_processor=MapCompose(strip_text), output_processor=TakeFirst())
