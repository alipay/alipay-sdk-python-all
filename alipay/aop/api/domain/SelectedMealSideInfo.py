#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SelectedMealSideInfo(object):

    def __init__(self):
        self._add_price = None
        self._dish_id = None
        self._dish_name = None
        self._ext_infos = None
        self._num = None
        self._out_dish_id = None
        self._out_dish_infos = None
        self._out_sku_id = None
        self._side_price = None
        self._sku_id = None
        self._type = None
        self._unit = None

    @property
    def add_price(self):
        return self._add_price

    @add_price.setter
    def add_price(self, value):
        self._add_price = value
    @property
    def dish_id(self):
        return self._dish_id

    @dish_id.setter
    def dish_id(self, value):
        self._dish_id = value
    @property
    def dish_name(self):
        return self._dish_name

    @dish_name.setter
    def dish_name(self, value):
        self._dish_name = value
    @property
    def ext_infos(self):
        return self._ext_infos

    @ext_infos.setter
    def ext_infos(self, value):
        self._ext_infos = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def out_dish_id(self):
        return self._out_dish_id

    @out_dish_id.setter
    def out_dish_id(self, value):
        self._out_dish_id = value
    @property
    def out_dish_infos(self):
        return self._out_dish_infos

    @out_dish_infos.setter
    def out_dish_infos(self, value):
        self._out_dish_infos = value
    @property
    def out_sku_id(self):
        return self._out_sku_id

    @out_sku_id.setter
    def out_sku_id(self, value):
        self._out_sku_id = value
    @property
    def side_price(self):
        return self._side_price

    @side_price.setter
    def side_price(self, value):
        self._side_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, value):
        self._unit = value


    def to_alipay_dict(self):
        params = dict()
        if self.add_price:
            if hasattr(self.add_price, 'to_alipay_dict'):
                params['add_price'] = self.add_price.to_alipay_dict()
            else:
                params['add_price'] = self.add_price
        if self.dish_id:
            if hasattr(self.dish_id, 'to_alipay_dict'):
                params['dish_id'] = self.dish_id.to_alipay_dict()
            else:
                params['dish_id'] = self.dish_id
        if self.dish_name:
            if hasattr(self.dish_name, 'to_alipay_dict'):
                params['dish_name'] = self.dish_name.to_alipay_dict()
            else:
                params['dish_name'] = self.dish_name
        if self.ext_infos:
            if hasattr(self.ext_infos, 'to_alipay_dict'):
                params['ext_infos'] = self.ext_infos.to_alipay_dict()
            else:
                params['ext_infos'] = self.ext_infos
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
        if self.out_dish_id:
            if hasattr(self.out_dish_id, 'to_alipay_dict'):
                params['out_dish_id'] = self.out_dish_id.to_alipay_dict()
            else:
                params['out_dish_id'] = self.out_dish_id
        if self.out_dish_infos:
            if hasattr(self.out_dish_infos, 'to_alipay_dict'):
                params['out_dish_infos'] = self.out_dish_infos.to_alipay_dict()
            else:
                params['out_dish_infos'] = self.out_dish_infos
        if self.out_sku_id:
            if hasattr(self.out_sku_id, 'to_alipay_dict'):
                params['out_sku_id'] = self.out_sku_id.to_alipay_dict()
            else:
                params['out_sku_id'] = self.out_sku_id
        if self.side_price:
            if hasattr(self.side_price, 'to_alipay_dict'):
                params['side_price'] = self.side_price.to_alipay_dict()
            else:
                params['side_price'] = self.side_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
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
        o = SelectedMealSideInfo()
        if 'add_price' in d:
            o.add_price = d['add_price']
        if 'dish_id' in d:
            o.dish_id = d['dish_id']
        if 'dish_name' in d:
            o.dish_name = d['dish_name']
        if 'ext_infos' in d:
            o.ext_infos = d['ext_infos']
        if 'num' in d:
            o.num = d['num']
        if 'out_dish_id' in d:
            o.out_dish_id = d['out_dish_id']
        if 'out_dish_infos' in d:
            o.out_dish_infos = d['out_dish_infos']
        if 'out_sku_id' in d:
            o.out_sku_id = d['out_sku_id']
        if 'side_price' in d:
            o.side_price = d['side_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'type' in d:
            o.type = d['type']
        if 'unit' in d:
            o.unit = d['unit']
        return o


