#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TourStockInfo(object):

    def __init__(self):
        self._stock_date = None
        self._stock_status = None

    @property
    def stock_date(self):
        return self._stock_date

    @stock_date.setter
    def stock_date(self, value):
        self._stock_date = value
    @property
    def stock_status(self):
        return self._stock_status

    @stock_status.setter
    def stock_status(self, value):
        self._stock_status = value


    def to_alipay_dict(self):
        params = dict()
        if self.stock_date:
            if hasattr(self.stock_date, 'to_alipay_dict'):
                params['stock_date'] = self.stock_date.to_alipay_dict()
            else:
                params['stock_date'] = self.stock_date
        if self.stock_status:
            if hasattr(self.stock_status, 'to_alipay_dict'):
                params['stock_status'] = self.stock_status.to_alipay_dict()
            else:
                params['stock_status'] = self.stock_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TourStockInfo()
        if 'stock_date' in d:
            o.stock_date = d['stock_date']
        if 'stock_status' in d:
            o.stock_status = d['stock_status']
        return o


