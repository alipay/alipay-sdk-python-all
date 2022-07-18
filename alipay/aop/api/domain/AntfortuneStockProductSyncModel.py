#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Kv import Kv


class AntfortuneStockProductSyncModel(object):

    def __init__(self):
        self._extension = None
        self._inventory_state = None
        self._prod_code = None
        self._prod_type = None
        self._remain_inventory_amt = None
        self._remain_inventory_num = None

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        if isinstance(value, Kv):
            self._extension = value
        else:
            self._extension = Kv.from_alipay_dict(value)
    @property
    def inventory_state(self):
        return self._inventory_state

    @inventory_state.setter
    def inventory_state(self, value):
        self._inventory_state = value
    @property
    def prod_code(self):
        return self._prod_code

    @prod_code.setter
    def prod_code(self, value):
        self._prod_code = value
    @property
    def prod_type(self):
        return self._prod_type

    @prod_type.setter
    def prod_type(self, value):
        self._prod_type = value
    @property
    def remain_inventory_amt(self):
        return self._remain_inventory_amt

    @remain_inventory_amt.setter
    def remain_inventory_amt(self, value):
        self._remain_inventory_amt = value
    @property
    def remain_inventory_num(self):
        return self._remain_inventory_num

    @remain_inventory_num.setter
    def remain_inventory_num(self, value):
        self._remain_inventory_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.extension:
            if hasattr(self.extension, 'to_alipay_dict'):
                params['extension'] = self.extension.to_alipay_dict()
            else:
                params['extension'] = self.extension
        if self.inventory_state:
            if hasattr(self.inventory_state, 'to_alipay_dict'):
                params['inventory_state'] = self.inventory_state.to_alipay_dict()
            else:
                params['inventory_state'] = self.inventory_state
        if self.prod_code:
            if hasattr(self.prod_code, 'to_alipay_dict'):
                params['prod_code'] = self.prod_code.to_alipay_dict()
            else:
                params['prod_code'] = self.prod_code
        if self.prod_type:
            if hasattr(self.prod_type, 'to_alipay_dict'):
                params['prod_type'] = self.prod_type.to_alipay_dict()
            else:
                params['prod_type'] = self.prod_type
        if self.remain_inventory_amt:
            if hasattr(self.remain_inventory_amt, 'to_alipay_dict'):
                params['remain_inventory_amt'] = self.remain_inventory_amt.to_alipay_dict()
            else:
                params['remain_inventory_amt'] = self.remain_inventory_amt
        if self.remain_inventory_num:
            if hasattr(self.remain_inventory_num, 'to_alipay_dict'):
                params['remain_inventory_num'] = self.remain_inventory_num.to_alipay_dict()
            else:
                params['remain_inventory_num'] = self.remain_inventory_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfortuneStockProductSyncModel()
        if 'extension' in d:
            o.extension = d['extension']
        if 'inventory_state' in d:
            o.inventory_state = d['inventory_state']
        if 'prod_code' in d:
            o.prod_code = d['prod_code']
        if 'prod_type' in d:
            o.prod_type = d['prod_type']
        if 'remain_inventory_amt' in d:
            o.remain_inventory_amt = d['remain_inventory_amt']
        if 'remain_inventory_num' in d:
            o.remain_inventory_num = d['remain_inventory_num']
        return o


