#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SellsInfo(object):

    def __init__(self):
        self._customer_sells = None
        self._display_sells = None
        self._real_sells = None

    @property
    def customer_sells(self):
        return self._customer_sells

    @customer_sells.setter
    def customer_sells(self, value):
        self._customer_sells = value
    @property
    def display_sells(self):
        return self._display_sells

    @display_sells.setter
    def display_sells(self, value):
        self._display_sells = value
    @property
    def real_sells(self):
        return self._real_sells

    @real_sells.setter
    def real_sells(self, value):
        self._real_sells = value


    def to_alipay_dict(self):
        params = dict()
        if self.customer_sells:
            if hasattr(self.customer_sells, 'to_alipay_dict'):
                params['customer_sells'] = self.customer_sells.to_alipay_dict()
            else:
                params['customer_sells'] = self.customer_sells
        if self.display_sells:
            if hasattr(self.display_sells, 'to_alipay_dict'):
                params['display_sells'] = self.display_sells.to_alipay_dict()
            else:
                params['display_sells'] = self.display_sells
        if self.real_sells:
            if hasattr(self.real_sells, 'to_alipay_dict'):
                params['real_sells'] = self.real_sells.to_alipay_dict()
            else:
                params['real_sells'] = self.real_sells
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SellsInfo()
        if 'customer_sells' in d:
            o.customer_sells = d['customer_sells']
        if 'display_sells' in d:
            o.display_sells = d['display_sells']
        if 'real_sells' in d:
            o.real_sells = d['real_sells']
        return o


