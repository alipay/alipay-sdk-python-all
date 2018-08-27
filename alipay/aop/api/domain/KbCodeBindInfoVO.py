#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbCodeBindInfoVO(object):

    def __init__(self):
        self._area_name = None
        self._max_pepole_num = None
        self._min_pepole_num = None
        self._shop_id = None
        self._table_name = None
        self._table_no = None

    @property
    def area_name(self):
        return self._area_name

    @area_name.setter
    def area_name(self, value):
        self._area_name = value
    @property
    def max_pepole_num(self):
        return self._max_pepole_num

    @max_pepole_num.setter
    def max_pepole_num(self, value):
        self._max_pepole_num = value
    @property
    def min_pepole_num(self):
        return self._min_pepole_num

    @min_pepole_num.setter
    def min_pepole_num(self, value):
        self._min_pepole_num = value
    @property
    def shop_id(self):
        return self._shop_id

    @shop_id.setter
    def shop_id(self, value):
        self._shop_id = value
    @property
    def table_name(self):
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value
    @property
    def table_no(self):
        return self._table_no

    @table_no.setter
    def table_no(self, value):
        self._table_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.area_name:
            if hasattr(self.area_name, 'to_alipay_dict'):
                params['area_name'] = self.area_name.to_alipay_dict()
            else:
                params['area_name'] = self.area_name
        if self.max_pepole_num:
            if hasattr(self.max_pepole_num, 'to_alipay_dict'):
                params['max_pepole_num'] = self.max_pepole_num.to_alipay_dict()
            else:
                params['max_pepole_num'] = self.max_pepole_num
        if self.min_pepole_num:
            if hasattr(self.min_pepole_num, 'to_alipay_dict'):
                params['min_pepole_num'] = self.min_pepole_num.to_alipay_dict()
            else:
                params['min_pepole_num'] = self.min_pepole_num
        if self.shop_id:
            if hasattr(self.shop_id, 'to_alipay_dict'):
                params['shop_id'] = self.shop_id.to_alipay_dict()
            else:
                params['shop_id'] = self.shop_id
        if self.table_name:
            if hasattr(self.table_name, 'to_alipay_dict'):
                params['table_name'] = self.table_name.to_alipay_dict()
            else:
                params['table_name'] = self.table_name
        if self.table_no:
            if hasattr(self.table_no, 'to_alipay_dict'):
                params['table_no'] = self.table_no.to_alipay_dict()
            else:
                params['table_no'] = self.table_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbCodeBindInfoVO()
        if 'area_name' in d:
            o.area_name = d['area_name']
        if 'max_pepole_num' in d:
            o.max_pepole_num = d['max_pepole_num']
        if 'min_pepole_num' in d:
            o.min_pepole_num = d['min_pepole_num']
        if 'shop_id' in d:
            o.shop_id = d['shop_id']
        if 'table_name' in d:
            o.table_name = d['table_name']
        if 'table_no' in d:
            o.table_no = d['table_no']
        return o


