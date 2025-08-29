#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesRefWeakFirst import RainyComplexTypesRefWeakFirst
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataexchangeTreetoantoneRainystestSyncModel(object):

    def __init__(self):
        self._demo_boolean = None
        self._demo_date = None
        self._demo_num = None
        self._demo_price = None
        self._demo_ref_copy = None
        self._demo_ref_fieldcopy = None
        self._deno_ref = None
        self._open_id = None
        self._user_id = None

    @property
    def demo_boolean(self):
        return self._demo_boolean

    @demo_boolean.setter
    def demo_boolean(self, value):
        self._demo_boolean = value
    @property
    def demo_date(self):
        return self._demo_date

    @demo_date.setter
    def demo_date(self, value):
        self._demo_date = value
    @property
    def demo_num(self):
        return self._demo_num

    @demo_num.setter
    def demo_num(self, value):
        self._demo_num = value
    @property
    def demo_price(self):
        return self._demo_price

    @demo_price.setter
    def demo_price(self, value):
        self._demo_price = value
    @property
    def demo_ref_copy(self):
        return self._demo_ref_copy

    @demo_ref_copy.setter
    def demo_ref_copy(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._demo_ref_copy = value
        else:
            self._demo_ref_copy = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def demo_ref_fieldcopy(self):
        return self._demo_ref_fieldcopy

    @demo_ref_fieldcopy.setter
    def demo_ref_fieldcopy(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFirst):
            self._demo_ref_fieldcopy = value
        else:
            self._demo_ref_fieldcopy = RainyComplexTypesRefWeakFirst.from_alipay_dict(value)
    @property
    def deno_ref(self):
        return self._deno_ref

    @deno_ref.setter
    def deno_ref(self, value):
        if isinstance(value, list):
            self._deno_ref = list()
            for i in value:
                if isinstance(i, RainyComplexTypesTheFourth):
                    self._deno_ref.append(i)
                else:
                    self._deno_ref.append(RainyComplexTypesTheFourth.from_alipay_dict(i))
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_boolean:
            if hasattr(self.demo_boolean, 'to_alipay_dict'):
                params['demo_boolean'] = self.demo_boolean.to_alipay_dict()
            else:
                params['demo_boolean'] = self.demo_boolean
        if self.demo_date:
            if hasattr(self.demo_date, 'to_alipay_dict'):
                params['demo_date'] = self.demo_date.to_alipay_dict()
            else:
                params['demo_date'] = self.demo_date
        if self.demo_num:
            if hasattr(self.demo_num, 'to_alipay_dict'):
                params['demo_num'] = self.demo_num.to_alipay_dict()
            else:
                params['demo_num'] = self.demo_num
        if self.demo_price:
            if hasattr(self.demo_price, 'to_alipay_dict'):
                params['demo_price'] = self.demo_price.to_alipay_dict()
            else:
                params['demo_price'] = self.demo_price
        if self.demo_ref_copy:
            if hasattr(self.demo_ref_copy, 'to_alipay_dict'):
                params['demo_ref_copy'] = self.demo_ref_copy.to_alipay_dict()
            else:
                params['demo_ref_copy'] = self.demo_ref_copy
        if self.demo_ref_fieldcopy:
            if hasattr(self.demo_ref_fieldcopy, 'to_alipay_dict'):
                params['demo_ref_fieldcopy'] = self.demo_ref_fieldcopy.to_alipay_dict()
            else:
                params['demo_ref_fieldcopy'] = self.demo_ref_fieldcopy
        if self.deno_ref:
            if isinstance(self.deno_ref, list):
                for i in range(0, len(self.deno_ref)):
                    element = self.deno_ref[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.deno_ref[i] = element.to_alipay_dict()
            if hasattr(self.deno_ref, 'to_alipay_dict'):
                params['deno_ref'] = self.deno_ref.to_alipay_dict()
            else:
                params['deno_ref'] = self.deno_ref
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataexchangeTreetoantoneRainystestSyncModel()
        if 'demo_boolean' in d:
            o.demo_boolean = d['demo_boolean']
        if 'demo_date' in d:
            o.demo_date = d['demo_date']
        if 'demo_num' in d:
            o.demo_num = d['demo_num']
        if 'demo_price' in d:
            o.demo_price = d['demo_price']
        if 'demo_ref_copy' in d:
            o.demo_ref_copy = d['demo_ref_copy']
        if 'demo_ref_fieldcopy' in d:
            o.demo_ref_fieldcopy = d['demo_ref_fieldcopy']
        if 'deno_ref' in d:
            o.deno_ref = d['deno_ref']
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


