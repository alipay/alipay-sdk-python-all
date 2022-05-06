#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ActivityGoods(object):

    def __init__(self):
        self._barcode = None
        self._benefit_id = None
        self._benefit_name = None
        self._stock = None

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
    def benefit_name(self):
        return self._benefit_name

    @benefit_name.setter
    def benefit_name(self, value):
        self._benefit_name = value
    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = value


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
        if self.benefit_name:
            if hasattr(self.benefit_name, 'to_alipay_dict'):
                params['benefit_name'] = self.benefit_name.to_alipay_dict()
            else:
                params['benefit_name'] = self.benefit_name
        if self.stock:
            if hasattr(self.stock, 'to_alipay_dict'):
                params['stock'] = self.stock.to_alipay_dict()
            else:
                params['stock'] = self.stock
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ActivityGoods()
        if 'barcode' in d:
            o.barcode = d['barcode']
        if 'benefit_id' in d:
            o.benefit_id = d['benefit_id']
        if 'benefit_name' in d:
            o.benefit_name = d['benefit_name']
        if 'stock' in d:
            o.stock = d['stock']
        return o


