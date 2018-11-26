#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PosSkuModel(object):

    def __init__(self):
        self._box_price = None
        self._sell_price = None
        self._sku_id = None
        self._sku_sort = None
        self._spec_code_01 = None
        self._spec_name_01 = None
        self._status = None

    @property
    def box_price(self):
        return self._box_price

    @box_price.setter
    def box_price(self, value):
        self._box_price = value
    @property
    def sell_price(self):
        return self._sell_price

    @sell_price.setter
    def sell_price(self, value):
        self._sell_price = value
    @property
    def sku_id(self):
        return self._sku_id

    @sku_id.setter
    def sku_id(self, value):
        self._sku_id = value
    @property
    def sku_sort(self):
        return self._sku_sort

    @sku_sort.setter
    def sku_sort(self, value):
        self._sku_sort = value
    @property
    def spec_code_01(self):
        return self._spec_code_01

    @spec_code_01.setter
    def spec_code_01(self, value):
        self._spec_code_01 = value
    @property
    def spec_name_01(self):
        return self._spec_name_01

    @spec_name_01.setter
    def spec_name_01(self, value):
        self._spec_name_01 = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_price:
            if hasattr(self.box_price, 'to_alipay_dict'):
                params['box_price'] = self.box_price.to_alipay_dict()
            else:
                params['box_price'] = self.box_price
        if self.sell_price:
            if hasattr(self.sell_price, 'to_alipay_dict'):
                params['sell_price'] = self.sell_price.to_alipay_dict()
            else:
                params['sell_price'] = self.sell_price
        if self.sku_id:
            if hasattr(self.sku_id, 'to_alipay_dict'):
                params['sku_id'] = self.sku_id.to_alipay_dict()
            else:
                params['sku_id'] = self.sku_id
        if self.sku_sort:
            if hasattr(self.sku_sort, 'to_alipay_dict'):
                params['sku_sort'] = self.sku_sort.to_alipay_dict()
            else:
                params['sku_sort'] = self.sku_sort
        if self.spec_code_01:
            if hasattr(self.spec_code_01, 'to_alipay_dict'):
                params['spec_code_01'] = self.spec_code_01.to_alipay_dict()
            else:
                params['spec_code_01'] = self.spec_code_01
        if self.spec_name_01:
            if hasattr(self.spec_name_01, 'to_alipay_dict'):
                params['spec_name_01'] = self.spec_name_01.to_alipay_dict()
            else:
                params['spec_name_01'] = self.spec_name_01
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PosSkuModel()
        if 'box_price' in d:
            o.box_price = d['box_price']
        if 'sell_price' in d:
            o.sell_price = d['sell_price']
        if 'sku_id' in d:
            o.sku_id = d['sku_id']
        if 'sku_sort' in d:
            o.sku_sort = d['sku_sort']
        if 'spec_code_01' in d:
            o.spec_code_01 = d['spec_code_01']
        if 'spec_name_01' in d:
            o.spec_name_01 = d['spec_name_01']
        if 'status' in d:
            o.status = d['status']
        return o


