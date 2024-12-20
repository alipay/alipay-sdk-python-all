#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ApiScheameOne import ApiScheameOne


class AlipayDataDataserviceProdtestQueryModel(object):

    def __init__(self):
        self._date_test = None
        self._name = None
        self._price = None
        self._test_array = None

    @property
    def date_test(self):
        return self._date_test

    @date_test.setter
    def date_test(self, value):
        self._date_test = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
    @property
    def test_array(self):
        return self._test_array

    @test_array.setter
    def test_array(self, value):
        if isinstance(value, list):
            self._test_array = list()
            for i in value:
                if isinstance(i, ApiScheameOne):
                    self._test_array.append(i)
                else:
                    self._test_array.append(ApiScheameOne.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.date_test:
            if hasattr(self.date_test, 'to_alipay_dict'):
                params['date_test'] = self.date_test.to_alipay_dict()
            else:
                params['date_test'] = self.date_test
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.price:
            if hasattr(self.price, 'to_alipay_dict'):
                params['price'] = self.price.to_alipay_dict()
            else:
                params['price'] = self.price
        if self.test_array:
            if isinstance(self.test_array, list):
                for i in range(0, len(self.test_array)):
                    element = self.test_array[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_array[i] = element.to_alipay_dict()
            if hasattr(self.test_array, 'to_alipay_dict'):
                params['test_array'] = self.test_array.to_alipay_dict()
            else:
                params['test_array'] = self.test_array
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceProdtestQueryModel()
        if 'date_test' in d:
            o.date_test = d['date_test']
        if 'name' in d:
            o.name = d['name']
        if 'price' in d:
            o.price = d['price']
        if 'test_array' in d:
            o.test_array = d['test_array']
        return o


