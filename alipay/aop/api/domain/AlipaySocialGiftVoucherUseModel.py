#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySocialGiftVoucherUseModel(object):

    def __init__(self):
        self._end_date = None
        self._mid = None
        self._order_id = None
        self._price = None
        self._start_date = None
        self._use_price = None
        self._voucher_id = None

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
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def use_price(self):
        return self._use_price

    @use_price.setter
    def use_price(self, value):
        self._use_price = value
    @property
    def voucher_id(self):
        return self._voucher_id

    @voucher_id.setter
    def voucher_id(self, value):
        self._voucher_id = value


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
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.start_date:
            if hasattr(self.start_date, 'to_alipay_dict'):
                params['start_date'] = self.start_date.to_alipay_dict()
            else:
                params['start_date'] = self.start_date
        if self.use_price:
            if hasattr(self.use_price, 'to_alipay_dict'):
                params['use_price'] = self.use_price.to_alipay_dict()
            else:
                params['use_price'] = self.use_price
        if self.voucher_id:
            if hasattr(self.voucher_id, 'to_alipay_dict'):
                params['voucher_id'] = self.voucher_id.to_alipay_dict()
            else:
                params['voucher_id'] = self.voucher_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySocialGiftVoucherUseModel()
        if 'end_date' in d:
            o.end_date = d['end_date']
        if 'mid' in d:
            o.mid = d['mid']
        if 'order_id' in d:
            o.order_id = d['order_id']
        if 'price' in d:
            o.price = d['price']
        if 'start_date' in d:
            o.start_date = d['start_date']
        if 'use_price' in d:
            o.use_price = d['use_price']
        if 'voucher_id' in d:
            o.voucher_id = d['voucher_id']
        return o


