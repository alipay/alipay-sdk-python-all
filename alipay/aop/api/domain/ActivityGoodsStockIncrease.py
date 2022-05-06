#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityGoodsStockIncrease(object):

    def __init__(self):
        self._barcode = None
        self._benefit_id = None
        self._increase_stock = None

    @property
    def barcode(self):
        return self._barcode

    @barcode.setter
    def barcode(self, value):
        self._barcode = value
    @property
    def benefit_id(self):
        return self._benefit_id

    @benefit_id.setter
    def benefit_id(self, value):
        self._benefit_id = value
    @property
    def increase_stock(self):
        return self._increase_stock

    @increase_stock.setter
    def increase_stock(self, value):
        self._increase_stock = value


    def to_alipay_dict(self):
        params = dict()
        if self.barcode:
            if hasattr(self.barcode, 'to_alipay_dict'):
                params['barcode'] = self.barcode.to_alipay_dict()
            else:
                params['barcode'] = self.barcode
        if self.benefit_id:
            if hasattr(self.benefit_id, 'to_alipay_dict'):
                params['benefit_id'] = self.benefit_id.to_alipay_dict()
            else:
                params['benefit_id'] = self.benefit_id
        if self.increase_stock:
            if hasattr(self.increase_stock, 'to_alipay_dict'):
                params['increase_stock'] = self.increase_stock.to_alipay_dict()
            else:
                params['increase_stock'] = self.increase_stock
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityGoodsStockIncrease()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'increase_stock' in d:
            o.increase_stock = d['increase_stock']
        return o


