#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex


class AlipaySecurityOpenbizmockTestQueryModel(object):

    def __init__(self):
        self._complex = None
        self._longitude = None
        self._mobile_number = None
        self._test_boolean = None
        self._test_date = None
        self._test_number = None
        self._test_price = None
        self._test_string = None
        self._test_string_not_list = None

    @property
    def complex(self):
        return self._complex

    @complex.setter
    def complex(self, value):
        if isinstance(value, list):
            self._complex = list()
            for i in value:
                if isinstance(i, PublicComplex):
                    self._complex.append(i)
                else:
                    self._complex.append(PublicComplex.from_alipay_dict(i))
    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value
    @property
    def test_boolean(self):
        return self._test_boolean

    @test_boolean.setter
    def test_boolean(self, value):
        if isinstance(value, list):
            self._test_boolean = list()
            for i in value:
                self._test_boolean.append(i)
    @property
    def test_date(self):
        return self._test_date

    @test_date.setter
    def test_date(self, value):
        if isinstance(value, list):
            self._test_date = list()
            for i in value:
                self._test_date.append(i)
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        if isinstance(value, list):
            self._test_number = list()
            for i in value:
                self._test_number.append(i)
    @property
    def test_price(self):
        return self._test_price

    @test_price.setter
    def test_price(self, value):
        if isinstance(value, list):
            self._test_price = list()
            for i in value:
                self._test_price.append(i)
    @property
    def test_string(self):
        return self._test_string

    @test_string.setter
    def test_string(self, value):
        self._test_string = value
    @property
    def test_string_not_list(self):
        return self._test_string_not_list

    @test_string_not_list.setter
    def test_string_not_list(self, value):
        if isinstance(value, list):
            self._test_string_not_list = list()
            for i in value:
                self._test_string_not_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.complex:
            if isinstance(self.complex, list):
                for i in range(0, len(self.complex)):
                    element = self.complex[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.complex[i] = element.to_alipay_dict()
            if hasattr(self.complex, 'to_alipay_dict'):
                params['complex'] = self.complex.to_alipay_dict()
            else:
                params['complex'] = self.complex
        if self.longitude:
            if hasattr(self.longitude, 'to_alipay_dict'):
                params['longitude'] = self.longitude.to_alipay_dict()
            else:
                params['longitude'] = self.longitude
        if self.mobile_number:
            if hasattr(self.mobile_number, 'to_alipay_dict'):
                params['mobile_number'] = self.mobile_number.to_alipay_dict()
            else:
                params['mobile_number'] = self.mobile_number
        if self.test_boolean:
            if isinstance(self.test_boolean, list):
                for i in range(0, len(self.test_boolean)):
                    element = self.test_boolean[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_boolean[i] = element.to_alipay_dict()
            if hasattr(self.test_boolean, 'to_alipay_dict'):
                params['test_boolean'] = self.test_boolean.to_alipay_dict()
            else:
                params['test_boolean'] = self.test_boolean
        if self.test_date:
            if isinstance(self.test_date, list):
                for i in range(0, len(self.test_date)):
                    element = self.test_date[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_date[i] = element.to_alipay_dict()
            if hasattr(self.test_date, 'to_alipay_dict'):
                params['test_date'] = self.test_date.to_alipay_dict()
            else:
                params['test_date'] = self.test_date
        if self.test_number:
            if isinstance(self.test_number, list):
                for i in range(0, len(self.test_number)):
                    element = self.test_number[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_number[i] = element.to_alipay_dict()
            if hasattr(self.test_number, 'to_alipay_dict'):
                params['test_number'] = self.test_number.to_alipay_dict()
            else:
                params['test_number'] = self.test_number
        if self.test_price:
            if isinstance(self.test_price, list):
                for i in range(0, len(self.test_price)):
                    element = self.test_price[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_price[i] = element.to_alipay_dict()
            if hasattr(self.test_price, 'to_alipay_dict'):
                params['test_price'] = self.test_price.to_alipay_dict()
            else:
                params['test_price'] = self.test_price
        if self.test_string:
            if hasattr(self.test_string, 'to_alipay_dict'):
                params['test_string'] = self.test_string.to_alipay_dict()
            else:
                params['test_string'] = self.test_string
        if self.test_string_not_list:
            if isinstance(self.test_string_not_list, list):
                for i in range(0, len(self.test_string_not_list)):
                    element = self.test_string_not_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_string_not_list[i] = element.to_alipay_dict()
            if hasattr(self.test_string_not_list, 'to_alipay_dict'):
                params['test_string_not_list'] = self.test_string_not_list.to_alipay_dict()
            else:
                params['test_string_not_list'] = self.test_string_not_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityOpenbizmockTestQueryModel()
        if 'complex' in d:
            o.complex = d['complex']
        if 'longitude' in d:
            o.longitude = d['longitude']
        if 'mobile_number' in d:
            o.mobile_number = d['mobile_number']
        if 'test_boolean' in d:
            o.test_boolean = d['test_boolean']
        if 'test_date' in d:
            o.test_date = d['test_date']
        if 'test_number' in d:
            o.test_number = d['test_number']
        if 'test_price' in d:
            o.test_price = d['test_price']
        if 'test_string' in d:
            o.test_string = d['test_string']
        if 'test_string_not_list' in d:
            o.test_string_not_list = d['test_string_not_list']
        return o


