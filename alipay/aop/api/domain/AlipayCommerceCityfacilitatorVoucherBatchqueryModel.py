#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceCityfacilitatorVoucherBatchqueryModel(object):

    def __init__(self):
        self._city_code = None
        self._trade_nos = None

    @property
    def city_code(self):
        return self._city_code

    @city_code.setter
    def city_code(self, value):
        self._city_code = value
    @property
    def trade_nos(self):
        return self._trade_nos

    @trade_nos.setter
    def trade_nos(self, value):
        if isinstance(value, list):
            self._trade_nos = list()
            for i in value:
                self._trade_nos.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.city_code:
            if hasattr(self.city_code, 'to_alipay_dict'):
                params['city_code'] = self.city_code.to_alipay_dict()
            else:
                params['city_code'] = self.city_code
        if self.trade_nos:
            if isinstance(self.trade_nos, list):
                for i in range(0, len(self.trade_nos)):
                    element = self.trade_nos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.trade_nos[i] = element.to_alipay_dict()
            if hasattr(self.trade_nos, 'to_alipay_dict'):
                params['trade_nos'] = self.trade_nos.to_alipay_dict()
            else:
                params['trade_nos'] = self.trade_nos
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceCityfacilitatorVoucherBatchqueryModel()
        if 'city_code' in d:
            o.city_code = d['city_code']
        if 'trade_nos' in d:
            o.trade_nos = d['trade_nos']
        return o


