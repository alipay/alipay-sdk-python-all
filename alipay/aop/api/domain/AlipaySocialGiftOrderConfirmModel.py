#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGiftOrderConfirmModel(object):

    def __init__(self):
        self._end_date = None
        self._mid = None
        self._order_id = None
        self._start_date = None
        self._total_price = None

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        self._end_date = value
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        self._mid = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        self._total_price = value


    def to_alipay_dict(self):
        params = dict()
        if self.end_date:
            if hasattr(self.end_date, 'to_alipay_dict'):
                params['end_date'] = self.end_date.to_alipay_dict()
            else:
                params['end_date'] = self.end_date
        if self.mid:
            if hasattr(self.mid, 'to_alipay_dict'):
                params['mid'] = self.mid.to_alipay_dict()
            else:
                params['mid'] = self.mid
        if self.order_id:
            if hasattr(self.order_id, 'to_alipay_dict'):
                params['order_id'] = self.order_id.to_alipay_dict()
            else:
                params['order_id'] = self.order_id
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.total_price:
            if hasattr(self.total_price, 'to_alipay_dict'):
                params['total_price'] = self.total_price.to_alipay_dict()
            else:
                params['total_price'] = self.total_price
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialGiftOrderConfirmModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'mid' in d:
            o.mid = d['mid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'total_price' in d:
            o.total_price = d['total_price']
        return o


