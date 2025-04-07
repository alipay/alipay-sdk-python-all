#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyComplexTypesRefWeakFourth(object):

    def __init__(self):
        self._seconde_demo_boolean = None
        self._seconde_demo_date = None
        self._seconde_demo_num = None
        self._seconde_demo_price = None
        self._seconde_demo_string = None

    @property
    def seconde_demo_boolean(self):
        return self._seconde_demo_boolean

    @seconde_demo_boolean.setter
    def seconde_demo_boolean(self, value):
        self._seconde_demo_boolean = value
    @property
    def seconde_demo_date(self):
        return self._seconde_demo_date

    @seconde_demo_date.setter
    def seconde_demo_date(self, value):
        self._seconde_demo_date = value
    @property
    def seconde_demo_num(self):
        return self._seconde_demo_num

    @seconde_demo_num.setter
    def seconde_demo_num(self, value):
        self._seconde_demo_num = value
    @property
    def seconde_demo_price(self):
        return self._seconde_demo_price

    @seconde_demo_price.setter
    def seconde_demo_price(self, value):
        self._seconde_demo_price = value
    @property
    def seconde_demo_string(self):
        return self._seconde_demo_string

    @seconde_demo_string.setter
    def seconde_demo_string(self, value):
        self._seconde_demo_string = value


    def to_alipay_dict(self):
        params = dict()
        if self.seconde_demo_boolean:
            if hasattr(self.seconde_demo_boolean, 'to_alipay_dict'):
                params['seconde_demo_boolean'] = self.seconde_demo_boolean.to_alipay_dict()
            else:
                params['seconde_demo_boolean'] = self.seconde_demo_boolean
        if self.seconde_demo_date:
            if hasattr(self.seconde_demo_date, 'to_alipay_dict'):
                params['seconde_demo_date'] = self.seconde_demo_date.to_alipay_dict()
            else:
                params['seconde_demo_date'] = self.seconde_demo_date
        if self.seconde_demo_num:
            if hasattr(self.seconde_demo_num, 'to_alipay_dict'):
                params['seconde_demo_num'] = self.seconde_demo_num.to_alipay_dict()
            else:
                params['seconde_demo_num'] = self.seconde_demo_num
        if self.seconde_demo_price:
            if hasattr(self.seconde_demo_price, 'to_alipay_dict'):
                params['seconde_demo_price'] = self.seconde_demo_price.to_alipay_dict()
            else:
                params['seconde_demo_price'] = self.seconde_demo_price
        if self.seconde_demo_string:
            if hasattr(self.seconde_demo_string, 'to_alipay_dict'):
                params['seconde_demo_string'] = self.seconde_demo_string.to_alipay_dict()
            else:
                params['seconde_demo_string'] = self.seconde_demo_string
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyComplexTypesRefWeakFourth()
        if 'seconde_demo_boolean' in d:
            o.seconde_demo_boolean = d['seconde_demo_boolean']
        if 'seconde_demo_date' in d:
            o.seconde_demo_date = d['seconde_demo_date']
        if 'seconde_demo_num' in d:
            o.seconde_demo_num = d['seconde_demo_num']
        if 'seconde_demo_price' in d:
            o.seconde_demo_price = d['seconde_demo_price']
        if 'seconde_demo_string' in d:
            o.seconde_demo_string = d['seconde_demo_string']
        return o


