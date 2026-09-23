#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CheckItemData(object):

    def __init__(self):
        self._check_status = None
        self._item_name = None
        self._sku_code = None

    @property
    def check_status(self):
        return self._check_status

    @check_status.setter
    def check_status(self, value):
        self._check_status = value
    @property
    def item_name(self):
        return self._item_name

    @item_name.setter
    def item_name(self, value):
        self._item_name = value
    @property
    def sku_code(self):
        return self._sku_code

    @sku_code.setter
    def sku_code(self, value):
        self._sku_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.check_status:
            if hasattr(self.check_status, 'to_alipay_dict'):
                params['check_status'] = self.check_status.to_alipay_dict()
            else:
                params['check_status'] = self.check_status
        if self.item_name:
            if hasattr(self.item_name, 'to_alipay_dict'):
                params['item_name'] = self.item_name.to_alipay_dict()
            else:
                params['item_name'] = self.item_name
        if self.sku_code:
            if hasattr(self.sku_code, 'to_alipay_dict'):
                params['sku_code'] = self.sku_code.to_alipay_dict()
            else:
                params['sku_code'] = self.sku_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CheckItemData()
        if 'check_status' in d:
            o.check_status = d['check_status']
        if 'item_name' in d:
            o.item_name = d['item_name']
        if 'sku_code' in d:
            o.sku_code = d['sku_code']
        return o


