#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiCateringPosDeskCreateModel(object):

    def __init__(self):
        self._area_id = None
        self._desk_name = None
        self._max_num = None
        self._num = None
        self._shop_id = None

    @property
    def area_id(self):
        return self._area_id

    @area_id.setter
    def area_id(self, value):
        self._area_id = value
    @property
    def desk_name(self):
        return self._desk_name

    @desk_name.setter
    def desk_name(self, value):
        self._desk_name = value
    @property
    def max_num(self):
        return self._max_num

    @max_num.setter
    def max_num(self, value):
        self._max_num = value
    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, value):
        self._num = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_id:
            if hasattr(self.area_id, 'to_alipay_dict'):
                params['area_id'] = self.area_id.to_alipay_dict()
            else:
                params['area_id'] = self.area_id
        if self.desk_name:
            if hasattr(self.desk_name, 'to_alipay_dict'):
                params['desk_name'] = self.desk_name.to_alipay_dict()
            else:
                params['desk_name'] = self.desk_name
        if self.max_num:
            if hasattr(self.max_num, 'to_alipay_dict'):
                params['max_num'] = self.max_num.to_alipay_dict()
            else:
                params['max_num'] = self.max_num
        if self.num:
            if hasattr(self.num, 'to_alipay_dict'):
                params['num'] = self.num.to_alipay_dict()
            else:
                params['num'] = self.num
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
        o = KoubeiCateringPosDeskCreateModel()
        if 'area_id' in d:
            o.area_id = d['area_id']
        if 'desk_name' in d:
            o.desk_name = d['desk_name']
        if 'max_num' in d:
            o.max_num = d['max_num']
        if 'num' in d:
            o.num = d['num']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        return o


