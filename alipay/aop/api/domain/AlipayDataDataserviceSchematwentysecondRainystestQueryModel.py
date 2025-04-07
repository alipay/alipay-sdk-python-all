#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesRefWeakFourth import RainyComplexTypesRefWeakFourth
from alipay.aop.api.domain.RainyComplexTypesTheFourth import RainyComplexTypesTheFourth


class AlipayDataDataserviceSchematwentysecondRainystestQueryModel(object):

    def __init__(self):
        self._demo_boolean = None
        self._demo_case = None
        self._demo_date = None
        self._demo_num = None
        self._demo_price = None
        self._demo_string = None
        self._first_wink_ref = None
        self._firstlevel_ref = None
        self._firstlevel_string_1 = None
        self._firstlevel_string_1_open_id = None
        self._firstlevel_string_2 = None
        self._firstlevel_string_2_open_id = None

    @property
    def demo_boolean(self):
        return self._demo_boolean

    @demo_boolean.setter
    def demo_boolean(self, value):
        self._demo_boolean = value
    @property
    def demo_case(self):
        return self._demo_case

    @demo_case.setter
    def demo_case(self, value):
        self._demo_case = value
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
    def demo_string(self):
        return self._demo_string

    @demo_string.setter
    def demo_string(self, value):
        self._demo_string = value
    @property
    def first_wink_ref(self):
        return self._first_wink_ref

    @first_wink_ref.setter
    def first_wink_ref(self, value):
        if isinstance(value, RainyComplexTypesRefWeakFourth):
            self._first_wink_ref = value
        else:
            self._first_wink_ref = RainyComplexTypesRefWeakFourth.from_alipay_dict(value)
    @property
    def firstlevel_ref(self):
        return self._firstlevel_ref

    @firstlevel_ref.setter
    def firstlevel_ref(self, value):
        if isinstance(value, RainyComplexTypesTheFourth):
            self._firstlevel_ref = value
        else:
            self._firstlevel_ref = RainyComplexTypesTheFourth.from_alipay_dict(value)
    @property
    def firstlevel_string_1(self):
        return self._firstlevel_string_1

    @firstlevel_string_1.setter
    def firstlevel_string_1(self, value):
        self._firstlevel_string_1 = value
    @property
    def firstlevel_string_1_open_id(self):
        return self._firstlevel_string_1_open_id

    @firstlevel_string_1_open_id.setter
    def firstlevel_string_1_open_id(self, value):
        self._firstlevel_string_1_open_id = value
    @property
    def firstlevel_string_2(self):
        return self._firstlevel_string_2

    @firstlevel_string_2.setter
    def firstlevel_string_2(self, value):
        self._firstlevel_string_2 = value
    @property
    def firstlevel_string_2_open_id(self):
        return self._firstlevel_string_2_open_id

    @firstlevel_string_2_open_id.setter
    def firstlevel_string_2_open_id(self, value):
        self._firstlevel_string_2_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.demo_boolean:
            if hasattr(self.demo_boolean, 'to_alipay_dict'):
                params['demo_boolean'] = self.demo_boolean.to_alipay_dict()
            else:
                params['demo_boolean'] = self.demo_boolean
        if self.demo_case:
            if hasattr(self.demo_case, 'to_alipay_dict'):
                params['demo_case'] = self.demo_case.to_alipay_dict()
            else:
                params['demo_case'] = self.demo_case
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
        if self.demo_string:
            if hasattr(self.demo_string, 'to_alipay_dict'):
                params['demo_string'] = self.demo_string.to_alipay_dict()
            else:
                params['demo_string'] = self.demo_string
        if self.first_wink_ref:
            if hasattr(self.first_wink_ref, 'to_alipay_dict'):
                params['first_wink_ref'] = self.first_wink_ref.to_alipay_dict()
            else:
                params['first_wink_ref'] = self.first_wink_ref
        if self.firstlevel_ref:
            if hasattr(self.firstlevel_ref, 'to_alipay_dict'):
                params['firstlevel_ref'] = self.firstlevel_ref.to_alipay_dict()
            else:
                params['firstlevel_ref'] = self.firstlevel_ref
        if self.firstlevel_string_1:
            if hasattr(self.firstlevel_string_1, 'to_alipay_dict'):
                params['firstlevel_string_1'] = self.firstlevel_string_1.to_alipay_dict()
            else:
                params['firstlevel_string_1'] = self.firstlevel_string_1
        if self.firstlevel_string_1_open_id:
            if hasattr(self.firstlevel_string_1_open_id, 'to_alipay_dict'):
                params['firstlevel_string_1_open_id'] = self.firstlevel_string_1_open_id.to_alipay_dict()
            else:
                params['firstlevel_string_1_open_id'] = self.firstlevel_string_1_open_id
        if self.firstlevel_string_2:
            if hasattr(self.firstlevel_string_2, 'to_alipay_dict'):
                params['firstlevel_string_2'] = self.firstlevel_string_2.to_alipay_dict()
            else:
                params['firstlevel_string_2'] = self.firstlevel_string_2
        if self.firstlevel_string_2_open_id:
            if hasattr(self.firstlevel_string_2_open_id, 'to_alipay_dict'):
                params['firstlevel_string_2_open_id'] = self.firstlevel_string_2_open_id.to_alipay_dict()
            else:
                params['firstlevel_string_2_open_id'] = self.firstlevel_string_2_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceSchematwentysecondRainystestQueryModel()
        if 'demo_boolean' in d:
            o.demo_boolean = d['demo_boolean']
        if 'demo_case' in d:
            o.demo_case = d['demo_case']
        if 'demo_date' in d:
            o.demo_date = d['demo_date']
        if 'demo_num' in d:
            o.demo_num = d['demo_num']
        if 'demo_price' in d:
            o.demo_price = d['demo_price']
        if 'demo_string' in d:
            o.demo_string = d['demo_string']
        if 'first_wink_ref' in d:
            o.first_wink_ref = d['first_wink_ref']
        if 'firstlevel_ref' in d:
            o.firstlevel_ref = d['firstlevel_ref']
        if 'firstlevel_string_1' in d:
            o.firstlevel_string_1 = d['firstlevel_string_1']
        if 'firstlevel_string_1_open_id' in d:
            o.firstlevel_string_1_open_id = d['firstlevel_string_1_open_id']
        if 'firstlevel_string_2' in d:
            o.firstlevel_string_2 = d['firstlevel_string_2']
        if 'firstlevel_string_2_open_id' in d:
            o.firstlevel_string_2_open_id = d['firstlevel_string_2_open_id']
        return o


