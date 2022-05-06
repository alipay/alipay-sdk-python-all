#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PickUpInfo(object):

    def __init__(self):
        self._pick_up_address = None
        self._pick_up_code = None
        self._pick_up_shop_name = None
        self._pick_up_type = None
        self._table_num = None

    @property
    def pick_up_address(self):
        return self._pick_up_address

    @pick_up_address.setter
    def pick_up_address(self, value):
        self._pick_up_address = value
    @property
    def pick_up_code(self):
        return self._pick_up_code

    @pick_up_code.setter
    def pick_up_code(self, value):
        self._pick_up_code = value
    @property
    def pick_up_shop_name(self):
        return self._pick_up_shop_name

    @pick_up_shop_name.setter
    def pick_up_shop_name(self, value):
        self._pick_up_shop_name = value
    @property
    def pick_up_type(self):
        return self._pick_up_type

    @pick_up_type.setter
    def pick_up_type(self, value):
        self._pick_up_type = value
    @property
    def table_num(self):
        return self._table_num

    @table_num.setter
    def table_num(self, value):
        self._table_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.pick_up_address:
            if hasattr(self.pick_up_address, 'to_alipay_dict'):
                params['pick_up_address'] = self.pick_up_address.to_alipay_dict()
            else:
                params['pick_up_address'] = self.pick_up_address
        if self.pick_up_code:
            if hasattr(self.pick_up_code, 'to_alipay_dict'):
                params['pick_up_code'] = self.pick_up_code.to_alipay_dict()
            else:
                params['pick_up_code'] = self.pick_up_code
        if self.pick_up_shop_name:
            if hasattr(self.pick_up_shop_name, 'to_alipay_dict'):
                params['pick_up_shop_name'] = self.pick_up_shop_name.to_alipay_dict()
            else:
                params['pick_up_shop_name'] = self.pick_up_shop_name
        if self.pick_up_type:
            if hasattr(self.pick_up_type, 'to_alipay_dict'):
                params['pick_up_type'] = self.pick_up_type.to_alipay_dict()
            else:
                params['pick_up_type'] = self.pick_up_type
        if self.table_num:
            if hasattr(self.table_num, 'to_alipay_dict'):
                params['table_num'] = self.table_num.to_alipay_dict()
            else:
                params['table_num'] = self.table_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PickUpInfo()
        if 'pick_up_address' in d:
            o.pick_up_address = d['pick_up_address']
        if 'pick_up_code' in d:
            o.pick_up_code = d['pick_up_code']
        if 'pick_up_shop_name' in d:
            o.pick_up_shop_name = d['pick_up_shop_name']
        if 'pick_up_type' in d:
            o.pick_up_type = d['pick_up_type']
        if 'table_num' in d:
            o.table_num = d['table_num']
        return o


