#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMarketingVoucherStockQueryModel(object):

    def __init__(self):
        self._stock_id = None

    @property
    def stock_id(self):
        return self._stock_id

    @stock_id.setter
    def stock_id(self, value):
        self._stock_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.stock_id:
            if hasattr(self.stock_id, 'to_alipay_dict'):
                params['stock_id'] = self.stock_id.to_alipay_dict()
            else:
                params['stock_id'] = self.stock_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingVoucherStockQueryModel()
        if 'stock_id' in d:
            o.stock_id = d['stock_id']
        return o


