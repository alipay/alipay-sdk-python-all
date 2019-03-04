#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class NearbyGoods(object):

    def __init__(self):
        self._discount_desc = None
        self._distance = None
        self._image_url = None
        self._item_field_id = None
        self._item_id = None
        self._item_name = None
        self._jump_url = None
        self._original_price = None
        self._sales_icon = None
        self._selling_price = None
        self._shop_field_id = None
        self._shop_id = None
        self._shop_logo = None
        self._shop_name = None
        self._tb_mini_shop_id = None

    @property
    def discount_desc(self):
        return self._discount_desc

    @discount_desc.setter
    def discount_desc(self, value):
        self._discount_desc = value
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
    def jump_url(self):
        return self._jump_url

    @jump_url.setter
    def jump_url(self, value):
        self._jump_url = value
    @property
    def original_price(self):
        return self._original_price

    @original_price.setter
    def original_price(self, value):
        self._original_price = value
    @property
    def sales_icon(self):
        return self._sales_icon

    @sales_icon.setter
    def sales_icon(self, value):
        self._sales_icon = value
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
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value
    @property
    def tb_mini_shop_id(self):
        return self._tb_mini_shop_id

    @tb_mini_shop_id.setter
    def tb_mini_shop_id(self, value):
        self._tb_mini_shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.discount_desc:
            if hasattr(self.discount_desc, 'to_alipay_dict'):
                params['discount_desc'] = self.discount_desc.to_alipay_dict()
            else:
                params['discount_desc'] = self.discount_desc
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
        if self.jump_url:
            if hasattr(self.jump_url, 'to_alipay_dict'):
                params['jump_url'] = self.jump_url.to_alipay_dict()
            else:
                params['jump_url'] = self.jump_url
        if self.original_price:
            if hasattr(self.original_price, 'to_alipay_dict'):
                params['original_price'] = self.original_price.to_alipay_dict()
            else:
                params['original_price'] = self.original_price
        if self.sales_icon:
            if hasattr(self.sales_icon, 'to_alipay_dict'):
                params['sales_icon'] = self.sales_icon.to_alipay_dict()
            else:
                params['sales_icon'] = self.sales_icon
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
        if self.shop_name:
            if hasattr(self.shop_name, 'to_alipay_dict'):
                params['shop_name'] = self.shop_name.to_alipay_dict()
            else:
                params['shop_name'] = self.shop_name
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
        o = NearbyGoods()
        if 'discount_desc' in d:
            o.discount_desc = d['discount_desc']
        if 'distance' in d:
            o.distance = d['distance']
        if 'image_url' in d:
            o.image_url = d['image_url']
        if 'item_field_id' in d:
            o.item_field_id = d['item_field_id']
        if 'item_id' in d:
            o.item_id = d['item_id']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'jump_url' in d:
            o.jump_url = d['jump_url']
        if 'original_price' in d:
            o.original_price = d['original_price']
        if 'sales_icon' in d:
            o.sales_icon = d['sales_icon']
        if 'selling_price' in d:
            o.selling_price = d['selling_price']
        if 'shop_field_id' in d:
            o.shop_field_id = d['shop_field_id']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'shop_logo' in d:
            o.shop_logo = d['shop_logo']
        if 'shop_name' in d:
            o.shop_name = d['shop_name']
        if 'tb_mini_shop_id' in d:
            o.tb_mini_shop_id = d['tb_mini_shop_id']
        return o


