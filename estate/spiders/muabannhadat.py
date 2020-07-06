import scrapy
from scrapy.loader import ItemLoader
from estate.items import RealEstateItem
import json
import urllib
import logging

class MuaBanNhaDatSpider(scrapy.Spider):
    name = "muabannhadat"
    start_urls = ['https://www.muabannhadat.vn/mua-ban-bat-dong-san']


    def parse(self, response):
        main_url = 'https://www.muabannhadat.vn/'
        list_post_href = response.xpath('//a[@data-cy="listing-title-link"]/@href').getall()
        for url in list_post_href:
            full_url = urllib.parse.urljoin(main_url, url)
            yield scrapy.Request(full_url, callback=self.parse_post)
        
        next_link = response.xpath('//a[@aria-label="Next"]/@href').get()
        if next_link:
            # if '3' in next_link: 
            #     return
            logging.info("===> Next: %s" % next_link)
            next_link = urllib.parse.urljoin(main_url, next_link)
            yield scrapy.Request(next_link, callback=self.parse)


    def parse_post(self, response):
        # self.logger.info('Parse function called on {}'.format(response.url))
        json_text = response.xpath('//script[contains(text(), "__INITIAL_STATE__")]/text()').get()
        json_data = json.loads(json_text[25:-122])

        post_url = response.url

        try: post_title = json_data['listing']['listing']['heading']
        except: post_title = ''

        try: post_date = json_data['listing']['listing']['updated_at']
        except: post_date = ''

        try: post_detail = json_data['listing']['listing']['title'] + '\n' + json_data['listing']['listing']['description']
        except: post_detail = ''


        try: post_author_name = json_data['listing']['listing']['created_by']['name']
        except: post_author_name = ''

        try: post_author_phone = json_data['listing']['listing']['created_by']['mobile_number']
        except: post_author_phone = ''


        try: post_images = [x['public_full_url'] for x in json_data['listing']['listing']['images']]
        except: post_images = []

        try: re_type = json_data['listing']['listing']['category']['slug']
        except: re_type = ''

        try: re_price = json_data['listing']['listing']['price']
        except: re_price = ''

        try: re_width = json_data['listing']['listing']['data_properties']['width']['value']
        except: re_width = ''

        try: re_length = json_data['listing']['listing']['data_properties']['length']['value']
        except: re_length = ''

        try: re_area_to_use = json_data['listing']['listing']['data_properties']['area_value']['value']
        except: re_area_to_use = ''

        try: re_direction = json_data['listing']['listing']['data_properties']['direction']['value']
        except: re_direction = ''

        try: re_legal = json_data['listing']['listing']['data_properties']['legal_document']['value']
        except: re_legal = ''


        try: re_num_floors = json_data['listing']['listing']['data_properties']['level_count']['value']
        except: re_num_floors = ''

        try: re_bedroom = json_data['listing']['listing']['data_properties']['bedroom_count']['value']
        except: re_bedroom = ''

        try: re_bathroom = json_data['listing']['listing']['data_properties']['bathroom_count']['value']
        except: re_bathroom = ''

        try: re_addr_city = json_data['listing']['listing']['address']['city']['title']
        except: re_addr_city = ''

        try: re_addr_district = json_data['listing']['listing']['address']['district']['title']
        except: re_addr_district = ''

        try: re_addr_ward = json_data['listing']['listing']['address']['ward']['title']
        except: re_addr_ward = ''

        try: re_addr_street_name = json_data['listing']['listing']['address']['street_name']
        except: re_addr_street_name = ''

        try: re_addr_street_number = json_data['listing']['listing']['address']['street_number']
        except: re_addr_street_number = ''

        try: re_addr_building = json_data['listing']['listing']['address']['building']
        except: re_addr_building = ''

        try: re_agency = json_data['listing']['listing']['created_by']['agency']['name']
        except: re_agency = ''

        loader = ItemLoader(item=RealEstateItem())

        loader.add_value('post_url', post_url)
        loader.add_value('post_title', post_title)
        loader.add_value('post_date', post_date)
        loader.add_value('post_detail', post_detail)

        loader.add_value('post_author_name', post_author_name)
        loader.add_value('post_author_phone', post_author_phone)

        loader.add_value('post_images', post_images)

        loader.add_value('re_type', re_type)
        loader.add_value('re_price', re_price)

        loader.add_value('re_width', re_width)
        loader.add_value('re_length', re_length)
        loader.add_value('re_area_to_use', re_area_to_use)

        loader.add_value('re_direction', re_direction)
        loader.add_value('re_legal', re_legal)

        loader.add_value('re_num_floors', re_num_floors)
        loader.add_value('re_bathroom', re_bathroom)
        loader.add_value('re_bedroom', re_bedroom)
        
        loader.add_value('re_addr_city', re_addr_city)
        loader.add_value('re_addr_district', re_addr_district)
        loader.add_value('re_addr_ward', re_addr_ward)
        loader.add_value('re_addr_street_name', re_addr_street_name)
        loader.add_value('re_addr_street_number', re_addr_street_number)
        loader.add_value('re_addr_building', re_addr_building)

        loader.add_value('re_agency', re_agency)

        post_item = loader.load_item()

        yield post_item

