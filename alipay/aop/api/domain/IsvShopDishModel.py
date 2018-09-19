#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IsvShopDishModel(object):

    def __init__(self):
        self._content = None
        self._dish_type_id = None
        self._dish_type_name = None
        self._good_level = None
        self._merchant_sold_cnt_seven_d = None
        self._merchant_sold_cnt_thirty_d = None
        self._merchant_sold_reusercnt_thirty_d = None
        self._merchant_sold_usercnt_thirty_d = None
        self._name = None
        self._outer_dish_id = None
        self._pict = None
        self._platform = None
        self._price = None
        self._quantity = None
        self._shop_id = None
        self._sold_cnt_seven_d = None
        self._sold_cnt_thirty_d = None
        self._sold_reusercnt_thirty_d = None
        self._sold_usercnt_thirty_d = None
        self._sort_col = None
        self._unit = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def dish_type_id(self):
        return self._dish_type_id

    @dish_type_id.setter
    def dish_type_id(self, value):
        self._dish_type_id = value
    @property
    def dish_type_name(self):
        return self._dish_type_name

    @dish_type_name.setter
    def dish_type_name(self, value):
        self._dish_type_name = value
    @property
    def good_level(self):
        return self._good_level

    @good_level.setter
    def good_level(self, value):
        self._good_level = value
    @property
    def merchant_sold_cnt_seven_d(self):
        return self._merchant_sold_cnt_seven_d

    @merchant_sold_cnt_seven_d.setter
    def merchant_sold_cnt_seven_d(self, value):
        self._merchant_sold_cnt_seven_d = value
    @property
    def merchant_sold_cnt_thirty_d(self):
        return self._merchant_sold_cnt_thirty_d

    @merchant_sold_cnt_thirty_d.setter
    def merchant_sold_cnt_thirty_d(self, value):
        self._merchant_sold_cnt_thirty_d = value
    @property
    def merchant_sold_reusercnt_thirty_d(self):
        return self._merchant_sold_reusercnt_thirty_d

    @merchant_sold_reusercnt_thirty_d.setter
    def merchant_sold_reusercnt_thirty_d(self, value):
        self._merchant_sold_reusercnt_thirty_d = value
    @property
    def merchant_sold_usercnt_thirty_d(self):
        return self._merchant_sold_usercnt_thirty_d

    @merchant_sold_usercnt_thirty_d.setter
    def merchant_sold_usercnt_thirty_d(self, value):
        self._merchant_sold_usercnt_thirty_d = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def outer_dish_id(self):
        return self._outer_dish_id

    @outer_dish_id.setter
    def outer_dish_id(self, value):
        self._outer_dish_id = value
    @property
    def pict(self):
        return self._pict

    @pict.setter
    def pict(self, value):
        self._pict = value
    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, value):
        self._platform = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def sold_cnt_seven_d(self):
        return self._sold_cnt_seven_d

    @sold_cnt_seven_d.setter
    def sold_cnt_seven_d(self, value):
        self._sold_cnt_seven_d = value
    @property
    def sold_cnt_thirty_d(self):
        return self._sold_cnt_thirty_d

    @sold_cnt_thirty_d.setter
    def sold_cnt_thirty_d(self, value):
        self._sold_cnt_thirty_d = value
    @property
    def sold_reusercnt_thirty_d(self):
        return self._sold_reusercnt_thirty_d

    @sold_reusercnt_thirty_d.setter
    def sold_reusercnt_thirty_d(self, value):
        self._sold_reusercnt_thirty_d = value
    @property
    def sold_usercnt_thirty_d(self):
        return self._sold_usercnt_thirty_d

    @sold_usercnt_thirty_d.setter
    def sold_usercnt_thirty_d(self, value):
        self._sold_usercnt_thirty_d = value
    @property
    def sort_col(self):
        return self._sort_col

    @sort_col.setter
    def sort_col(self, value):
        if isinstance(value, list):
            self._sort_col = list()
            for i in value:
                self._sort_col.append(i)
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.dish_type_id:
            if hasattr(self.dish_type_id, 'to_alipay_dict'):
                params['dish_type_id'] = self.dish_type_id.to_alipay_dict()
            else:
                params['dish_type_id'] = self.dish_type_id
        if self.dish_type_name:
            if hasattr(self.dish_type_name, 'to_alipay_dict'):
                params['dish_type_name'] = self.dish_type_name.to_alipay_dict()
            else:
                params['dish_type_name'] = self.dish_type_name
        if self.good_level:
            if hasattr(self.good_level, 'to_alipay_dict'):
                params['good_level'] = self.good_level.to_alipay_dict()
            else:
                params['good_level'] = self.good_level
        if self.merchant_sold_cnt_seven_d:
            if hasattr(self.merchant_sold_cnt_seven_d, 'to_alipay_dict'):
                params['merchant_sold_cnt_seven_d'] = self.merchant_sold_cnt_seven_d.to_alipay_dict()
            else:
                params['merchant_sold_cnt_seven_d'] = self.merchant_sold_cnt_seven_d
        if self.merchant_sold_cnt_thirty_d:
            if hasattr(self.merchant_sold_cnt_thirty_d, 'to_alipay_dict'):
                params['merchant_sold_cnt_thirty_d'] = self.merchant_sold_cnt_thirty_d.to_alipay_dict()
            else:
                params['merchant_sold_cnt_thirty_d'] = self.merchant_sold_cnt_thirty_d
        if self.merchant_sold_reusercnt_thirty_d:
            if hasattr(self.merchant_sold_reusercnt_thirty_d, 'to_alipay_dict'):
                params['merchant_sold_reusercnt_thirty_d'] = self.merchant_sold_reusercnt_thirty_d.to_alipay_dict()
            else:
                params['merchant_sold_reusercnt_thirty_d'] = self.merchant_sold_reusercnt_thirty_d
        if self.merchant_sold_usercnt_thirty_d:
            if hasattr(self.merchant_sold_usercnt_thirty_d, 'to_alipay_dict'):
                params['merchant_sold_usercnt_thirty_d'] = self.merchant_sold_usercnt_thirty_d.to_alipay_dict()
            else:
                params['merchant_sold_usercnt_thirty_d'] = self.merchant_sold_usercnt_thirty_d
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.outer_dish_id:
            if hasattr(self.outer_dish_id, 'to_alipay_dict'):
                params['outer_dish_id'] = self.outer_dish_id.to_alipay_dict()
            else:
                params['outer_dish_id'] = self.outer_dish_id
        if self.pict:
            if hasattr(self.pict, 'to_alipay_dict'):
                params['pict'] = self.pict.to_alipay_dict()
            else:
                params['pict'] = self.pict
        if self.platform:
            if hasattr(self.platform, 'to_alipay_dict'):
                params['platform'] = self.platform.to_alipay_dict()
            else:
                params['platform'] = self.platform
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.quantity:
            if hasattr(self.quantity, 'to_alipay_dict'):
                params['quantity'] = self.quantity.to_alipay_dict()
            else:
                params['quantity'] = self.quantity
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.sold_cnt_seven_d:
            if hasattr(self.sold_cnt_seven_d, 'to_alipay_dict'):
                params['sold_cnt_seven_d'] = self.sold_cnt_seven_d.to_alipay_dict()
            else:
                params['sold_cnt_seven_d'] = self.sold_cnt_seven_d
        if self.sold_cnt_thirty_d:
            if hasattr(self.sold_cnt_thirty_d, 'to_alipay_dict'):
                params['sold_cnt_thirty_d'] = self.sold_cnt_thirty_d.to_alipay_dict()
            else:
                params['sold_cnt_thirty_d'] = self.sold_cnt_thirty_d
        if self.sold_reusercnt_thirty_d:
            if hasattr(self.sold_reusercnt_thirty_d, 'to_alipay_dict'):
                params['sold_reusercnt_thirty_d'] = self.sold_reusercnt_thirty_d.to_alipay_dict()
            else:
                params['sold_reusercnt_thirty_d'] = self.sold_reusercnt_thirty_d
        if self.sold_usercnt_thirty_d:
            if hasattr(self.sold_usercnt_thirty_d, 'to_alipay_dict'):
                params['sold_usercnt_thirty_d'] = self.sold_usercnt_thirty_d.to_alipay_dict()
            else:
                params['sold_usercnt_thirty_d'] = self.sold_usercnt_thirty_d
        if self.sort_col:
            if isinstance(self.sort_col, list):
                for i in range(0, len(self.sort_col)):
                    element = self.sort_col[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sort_col[i] = element.to_alipay_dict()
            if hasattr(self.sort_col, 'to_alipay_dict'):
                params['sort_col'] = self.sort_col.to_alipay_dict()
            else:
                params['sort_col'] = self.sort_col
        if self.unit:
            if hasattr(self.unit, 'to_alipay_dict'):
                params['unit'] = self.unit.to_alipay_dict()
            else:
                params['unit'] = self.unit
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IsvShopDishModel()
        if 'content' in d:
            o.content = d['content']
        if 'dish_type_id' in d:
            o.dish_type_id = d['dish_type_id']
        if 'dish_type_name' in d:
            o.dish_type_name = d['dish_type_name']
        if 'good_level' in d:
            o.good_level = d['good_level']
        if 'merchant_sold_cnt_seven_d' in d:
            o.merchant_sold_cnt_seven_d = d['merchant_sold_cnt_seven_d']
        if 'merchant_sold_cnt_thirty_d' in d:
            o.merchant_sold_cnt_thirty_d = d['merchant_sold_cnt_thirty_d']
        if 'merchant_sold_reusercnt_thirty_d' in d:
            o.merchant_sold_reusercnt_thirty_d = d['merchant_sold_reusercnt_thirty_d']
        if 'merchant_sold_usercnt_thirty_d' in d:
            o.merchant_sold_usercnt_thirty_d = d['merchant_sold_usercnt_thirty_d']
        if 'name' in d:
            o.name = d['name']
        if 'outer_dish_id' in d:
            o.outer_dish_id = d['outer_dish_id']
        if 'pict' in d:
            o.pict = d['pict']
        if 'platform' in d:
            o.platform = d['platform']
        if 'price' in d:
            o.price = d['price']
        if 'quantity' in d:
            o.quantity = d['quantity']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'sold_cnt_seven_d' in d:
            o.sold_cnt_seven_d = d['sold_cnt_seven_d']
        if 'sold_cnt_thirty_d' in d:
            o.sold_cnt_thirty_d = d['sold_cnt_thirty_d']
        if 'sold_reusercnt_thirty_d' in d:
            o.sold_reusercnt_thirty_d = d['sold_reusercnt_thirty_d']
        if 'sold_usercnt_thirty_d' in d:
            o.sold_usercnt_thirty_d = d['sold_usercnt_thirty_d']
        if 'sort_col' in d:
            o.sort_col = d['sort_col']
        if 'unit' in d:
            o.unit = d['unit']
        return o


