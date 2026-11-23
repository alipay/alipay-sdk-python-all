#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TransferBillkey(object):

    def __init__(self):
        self._bill_key = None
        self._inst_id = None
        self._second_level_keys = None

    @property
    def bill_key(self):
        return self._bill_key

    @bill_key.setter
    def bill_key(self, value):
        self._bill_key = value
    @property
    def inst_id(self):
        return self._inst_id

    @inst_id.setter
    def inst_id(self, value):
        self._inst_id = value
    @property
    def second_level_keys(self):
        return self._second_level_keys

    @second_level_keys.setter
    def second_level_keys(self, value):
        self._second_level_keys = value


    def to_alipay_dict(self):
        params = dict()
        if self.bill_key:
            if hasattr(self.bill_key, 'to_alipay_dict'):
                params['bill_key'] = self.bill_key.to_alipay_dict()
            else:
                params['bill_key'] = self.bill_key
        if self.inst_id:
            if hasattr(self.inst_id, 'to_alipay_dict'):
                params['inst_id'] = self.inst_id.to_alipay_dict()
            else:
                params['inst_id'] = self.inst_id
        if self.second_level_keys:
            if hasattr(self.second_level_keys, 'to_alipay_dict'):
                params['second_level_keys'] = self.second_level_keys.to_alipay_dict()
            else:
                params['second_level_keys'] = self.second_level_keys
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TransferBillkey()
        if 'bill_key' in d:
            o.bill_key = d['bill_key']
        if 'inst_id' in d:
            o.inst_id = d['inst_id']
        if 'second_level_keys' in d:
            o.second_level_keys = d['second_level_keys']
        return o


