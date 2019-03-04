#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndexBigbuyItem(object):

    def __init__(self):
        self._distance = None
        self._image_url = None
        self._item_detail_url = None
        self._item_field_id = None
        self._item_id = None
        self._item_name = None
        self._item_tag = None
        self._name = None
        self._original_price = None
        self._price_unit = None
        self._selling_price = None
        self._shop_field_id = None
        self._shop_id = None
        self._shop_logo = None
        self._tb_mini_shop_id = None

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, value):
        self._distance = value
    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, value):
        self._image_url = value
    @property
    def item_detail_url(self):
        return self._item_detail_url

    @item_detail_url.setter
    def item_detail_url(self, value):
        self._item_detail_url = value
    @property
    def item_field_id(self):
        return self._item_field_id

    @item_field_id.setter
    def item_field_id(self, value):
        self._item_field_id = value
    @property
    def item_id(self):
        return self._item_id

    @item_id.setter
    def item_id(self, value):
        self._item_id = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def item_tag(self):
        return self._item_tag

    @item_tag.setter
    def item_tag(self, value):
        self._item_tag = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def price_unit(self):
        return self._price_unit

    @price_unit.setter
    def price_unit(self, value):
        self._price_unit = value
    @property
    def selling_price(self):
        return self._selling_price

    @selling_price.setter
    def selling_price(self, value):
        self._selling_price = value
    @property
    def shop_field_id(self):
        return self._shop_field_id

    @shop_field_id.setter
    def shop_field_id(self, value):
        self._shop_field_id = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def shop_logo(self):
        return self._shop_logo

    @shop_logo.setter
    def shop_logo(self, value):
        self._shop_logo = value
    @property
    def tb_mini_shop_id(self):
        return self._tb_mini_shop_id

    @tb_mini_shop_id.setter
    def tb_mini_shop_id(self, value):
        self._tb_mini_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.distance:
            if hasattr(self.distance, 'to_alipay_dict'):
                params['distance'] = self.distance.to_alipay_dict()
            else:
                params['distance'] = self.distance
        if self.image_url:
            if hasattr(self.image_url, 'to_alipay_dict'):
                params['image_url'] = self.image_url.to_alipay_dict()
            else:
                params['image_url'] = self.image_url
        if self.item_detail_url:
            if hasattr(self.item_detail_url, 'to_alipay_dict'):
                params['item_detail_url'] = self.item_detail_url.to_alipay_dict()
            else:
                params['item_detail_url'] = self.item_detail_url
        if self.item_field_id:
            if hasattr(self.item_field_id, 'to_alipay_dict'):
                params['item_field_id'] = self.item_field_id.to_alipay_dict()
            else:
                params['item_field_id'] = self.item_field_id
        if self.item_id:
            if hasattr(self.item_id, 'to_alipay_dict'):
                params['item_id'] = self.item_id.to_alipay_dict()
            else:
                params['item_id'] = self.item_id
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.item_tag:
            if hasattr(self.item_tag, 'to_alipay_dict'):
                params['item_tag'] = self.item_tag.to_alipay_dict()
            else:
                params['item_tag'] = self.item_tag
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.price_unit:
            if hasattr(self.price_unit, 'to_alipay_dict'):
                params['price_unit'] = self.price_unit.to_alipay_dict()
            else:
                params['price_unit'] = self.price_unit
        if self.selling_price:
            if hasattr(self.selling_price, 'to_alipay_dict'):
                params['selling_price'] = self.selling_price.to_alipay_dict()
            else:
                params['selling_price'] = self.selling_price
        if self.shop_field_id:
            if hasattr(self.shop_field_id, 'to_alipay_dict'):
                params['shop_field_id'] = self.shop_field_id.to_alipay_dict()
            else:
                params['shop_field_id'] = self.shop_field_id
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.shop_logo:
            if hasattr(self.shop_logo, 'to_alipay_dict'):
                params['shop_logo'] = self.shop_logo.to_alipay_dict()
            else:
                params['shop_logo'] = self.shop_logo
        if self.tb_mini_shop_id:
            if hasattr(self.tb_mini_shop_id, 'to_alipay_dict'):
                params['tb_mini_shop_id'] = self.tb_mini_shop_id.to_alipay_dict()
            else:
                params['tb_mini_shop_id'] = self.tb_mini_shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndexBigbuyItem()
        if 'distance' in d:
            o.distance = d['distance']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_detail_url' in d:
            o.item_detail_url = d['item_detail_url']
        if 'item_field_id' in d:
            o.item_field_id = d['item_field_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'item_tag' in d:
            o.item_tag = d['item_tag']
        if 'name' in d:
            o.name = d['name']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'price_unit' in d:
            o.price_unit = d['price_unit']
        if 'selling_price' in d:
            o.selling_price = d['selling_price']
        if 'shop_field_id' in d:
            o.shop_field_id = d['shop_field_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_logo' in d:
            o.shop_logo = d['shop_logo']
        if 'tb_mini_shop_id' in d:
            o.tb_mini_shop_id = d['tb_mini_shop_id']
        return o


