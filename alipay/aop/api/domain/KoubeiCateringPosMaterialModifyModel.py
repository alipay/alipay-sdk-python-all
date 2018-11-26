#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosMaterialModifyModel(object):

    def __init__(self):
        self._material_id = None
        self._material_name = None
        self._sell_price = None
        self._shop_id = None

    @property
    def material_id(self):
        return self._material_id

    @material_id.setter
    def material_id(self, value):
        self._material_id = value
    @property
    def material_name(self):
        return self._material_name

    @material_name.setter
    def material_name(self, value):
        self._material_name = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.material_id:
            if hasattr(self.material_id, 'to_alipay_dict'):
                params['material_id'] = self.material_id.to_alipay_dict()
            else:
                params['material_id'] = self.material_id
        if self.material_name:
            if hasattr(self.material_name, 'to_alipay_dict'):
                params['material_name'] = self.material_name.to_alipay_dict()
            else:
                params['material_name'] = self.material_name
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiCateringPosMaterialModifyModel()
        if 'material_id' in d:
            o.material_id = d['material_id']
        if 'material_name' in d:
            o.material_name = d['material_name']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


