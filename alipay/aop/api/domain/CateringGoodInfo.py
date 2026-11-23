#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AmountPartInfo import AmountPartInfo
from alipay.aop.api.domain.AmountPartInfo import AmountPartInfo


class CateringGoodInfo(object):

    def __init__(self):
        self._amount_symbol_feeds = None
        self._brand_logo = None
        self._brand_name = None
        self._camp_image = None
        self._category_name = None
        self._city_digital_poi_count = None
        self._distance_desc = None
        self._item_id = None
        self._origin_amount = None
        self._origin_amount_part = None
        self._path = None
        self._price_unit = None
        self._promo_tag = None
        self._sale_amount = None
        self._sale_amount_part = None
        self._shake_code_text = None
        self._shop_detail_url = None
        self._title = None

    @property
    def amount_symbol_feeds(self):
        return self._amount_symbol_feeds

    @amount_symbol_feeds.setter
    def amount_symbol_feeds(self, value):
        self._amount_symbol_feeds = value
    @property
    def brand_logo(self):
        return self._brand_logo

    @brand_logo.setter
    def brand_logo(self, value):
        self._brand_logo = value
    @property
    def brand_name(self):
        return self._brand_name

    @brand_name.setter
    def brand_name(self, value):
        self._brand_name = value
    @property
    def camp_image(self):
        return self._camp_image

    @camp_image.setter
    def camp_image(self, value):
        self._camp_image = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def city_digital_poi_count(self):
        return self._city_digital_poi_count

    @city_digital_poi_count.setter
    def city_digital_poi_count(self, value):
        self._city_digital_poi_count = value
    @property
    def distance_desc(self):
        return self._distance_desc

    @distance_desc.setter
    def distance_desc(self, value):
        self._distance_desc = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def origin_amount(self):
        return self._origin_amount

    @origin_amount.setter
    def origin_amount(self, value):
        self._origin_amount = value
    @property
    def origin_amount_part(self):
        return self._origin_amount_part

    @origin_amount_part.setter
    def origin_amount_part(self, value):
        if isinstance(value, AmountPartInfo):
            self._origin_amount_part = value
        else:
            self._origin_amount_part = AmountPartInfo.from_alipay_dict(value)
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def promo_tag(self):
        return self._promo_tag

    @promo_tag.setter
    def promo_tag(self, value):
        self._promo_tag = value
    @property
    def sale_amount(self):
        return self._sale_amount

    @sale_amount.setter
    def sale_amount(self, value):
        self._sale_amount = value
    @property
    def sale_amount_part(self):
        return self._sale_amount_part

    @sale_amount_part.setter
    def sale_amount_part(self, value):
        if isinstance(value, AmountPartInfo):
            self._sale_amount_part = value
        else:
            self._sale_amount_part = AmountPartInfo.from_alipay_dict(value)
    @property
    def shake_code_text(self):
        return self._shake_code_text

    @shake_code_text.setter
    def shake_code_text(self, value):
        self._shake_code_text = value
    @property
    def shop_detail_url(self):
        return self._shop_detail_url

    @shop_detail_url.setter
    def shop_detail_url(self, value):
        self._shop_detail_url = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value


    def to_alipay_dict(self):
        params = dict()
        if self.amount_symbol_feeds:
            if hasattr(self.amount_symbol_feeds, 'to_alipay_dict'):
                params['amount_symbol_feeds'] = self.amount_symbol_feeds.to_alipay_dict()
            else:
                params['amount_symbol_feeds'] = self.amount_symbol_feeds
        if self.brand_logo:
            if hasattr(self.brand_logo, 'to_alipay_dict'):
                params['brand_logo'] = self.brand_logo.to_alipay_dict()
            else:
                params['brand_logo'] = self.brand_logo
        if self.brand_name:
            if hasattr(self.brand_name, 'to_alipay_dict'):
                params['brand_name'] = self.brand_name.to_alipay_dict()
            else:
                params['brand_name'] = self.brand_name
        if self.camp_image:
            if hasattr(self.camp_image, 'to_alipay_dict'):
                params['camp_image'] = self.camp_image.to_alipay_dict()
            else:
                params['camp_image'] = self.camp_image
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.city_digital_poi_count:
            if hasattr(self.city_digital_poi_count, 'to_alipay_dict'):
                params['city_digital_poi_count'] = self.city_digital_poi_count.to_alipay_dict()
            else:
                params['city_digital_poi_count'] = self.city_digital_poi_count
        if self.distance_desc:
            if hasattr(self.distance_desc, 'to_alipay_dict'):
                params['distance_desc'] = self.distance_desc.to_alipay_dict()
            else:
                params['distance_desc'] = self.distance_desc
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.origin_amount:
            if hasattr(self.origin_amount, 'to_alipay_dict'):
                params['origin_amount'] = self.origin_amount.to_alipay_dict()
            else:
                params['origin_amount'] = self.origin_amount
        if self.origin_amount_part:
            if hasattr(self.origin_amount_part, 'to_alipay_dict'):
                params['origin_amount_part'] = self.origin_amount_part.to_alipay_dict()
            else:
                params['origin_amount_part'] = self.origin_amount_part
        if self.path:
            if hasattr(self.path, 'to_alipay_dict'):
                params['path'] = self.path.to_alipay_dict()
            else:
                params['path'] = self.path
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.promo_tag:
            if hasattr(self.promo_tag, 'to_alipay_dict'):
                params['promo_tag'] = self.promo_tag.to_alipay_dict()
            else:
                params['promo_tag'] = self.promo_tag
        if self.sale_amount:
            if hasattr(self.sale_amount, 'to_alipay_dict'):
                params['sale_amount'] = self.sale_amount.to_alipay_dict()
            else:
                params['sale_amount'] = self.sale_amount
        if self.sale_amount_part:
            if hasattr(self.sale_amount_part, 'to_alipay_dict'):
                params['sale_amount_part'] = self.sale_amount_part.to_alipay_dict()
            else:
                params['sale_amount_part'] = self.sale_amount_part
        if self.shake_code_text:
            if hasattr(self.shake_code_text, 'to_alipay_dict'):
                params['shake_code_text'] = self.shake_code_text.to_alipay_dict()
            else:
                params['shake_code_text'] = self.shake_code_text
        if self.shop_detail_url:
            if hasattr(self.shop_detail_url, 'to_alipay_dict'):
                params['shop_detail_url'] = self.shop_detail_url.to_alipay_dict()
            else:
                params['shop_detail_url'] = self.shop_detail_url
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CateringGoodInfo()
        if 'amount_symbol_feeds' in d:
            o.amount_symbol_feeds = d['amount_symbol_feeds']
        if 'brand_logo' in d:
            o.brand_logo = d['brand_logo']
        if 'brand_name' in d:
            o.brand_name = d['brand_name']
        if 'camp_image' in d:
            o.camp_image = d['camp_image']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'city_digital_poi_count' in d:
            o.city_digital_poi_count = d['city_digital_poi_count']
        if 'distance_desc' in d:
            o.distance_desc = d['distance_desc']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'origin_amount' in d:
            o.origin_amount = d['origin_amount']
        if 'origin_amount_part' in d:
            o.origin_amount_part = d['origin_amount_part']
        if 'path' in d:
            o.path = d['path']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'promo_tag' in d:
            o.promo_tag = d['promo_tag']
        if 'sale_amount' in d:
            o.sale_amount = d['sale_amount']
        if 'sale_amount_part' in d:
            o.sale_amount_part = d['sale_amount_part']
        if 'shake_code_text' in d:
            o.shake_code_text = d['shake_code_text']
        if 'shop_detail_url' in d:
            o.shop_detail_url = d['shop_detail_url']
        if 'title' in d:
            o.title = d['title']
        return o


