#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdDemoTestSetModel(object):

    def __init__(self):
        self._test_date = None
        self._test_number = None
        self._test_price = None
        self._test_string = None
        self._test_string_open_id = None

    @property
    def test_date(self):
        return self._test_date

    @test_date.setter
    def test_date(self, value):
        self._test_date = value
    @property
    def test_number(self):
        return self._test_number

    @test_number.setter
    def test_number(self, value):
        self._test_number = value
    @property
    def test_price(self):
        return self._test_price

    @test_price.setter
    def test_price(self, value):
        self._test_price = value
    @property
    def test_string(self):
        return self._test_string

    @test_string.setter
    def test_string(self, value):
        self._test_string = value
    @property
    def test_string_open_id(self):
        return self._test_string_open_id

    @test_string_open_id.setter
    def test_string_open_id(self, value):
        self._test_string_open_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_date:
            if hasattr(self.test_date, 'to_alipay_dict'):
                params['test_date'] = self.test_date.to_alipay_dict()
            else:
                params['test_date'] = self.test_date
        if self.test_number:
            if hasattr(self.test_number, 'to_alipay_dict'):
                params['test_number'] = self.test_number.to_alipay_dict()
            else:
                params['test_number'] = self.test_number
        if self.test_price:
            if hasattr(self.test_price, 'to_alipay_dict'):
                params['test_price'] = self.test_price.to_alipay_dict()
            else:
                params['test_price'] = self.test_price
        if self.test_string:
            if hasattr(self.test_string, 'to_alipay_dict'):
                params['test_string'] = self.test_string.to_alipay_dict()
            else:
                params['test_string'] = self.test_string
        if self.test_string_open_id:
            if hasattr(self.test_string_open_id, 'to_alipay_dict'):
                params['test_string_open_id'] = self.test_string_open_id.to_alipay_dict()
            else:
                params['test_string_open_id'] = self.test_string_open_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdDemoTestSetModel()
        if 'test_date' in d:
            o.test_date = d['test_date']
        if 'test_number' in d:
            o.test_number = d['test_number']
        if 'test_price' in d:
            o.test_price = d['test_price']
        if 'test_string' in d:
            o.test_string = d['test_string']
        if 'test_string_open_id' in d:
            o.test_string_open_id = d['test_string_open_id']
        return o


