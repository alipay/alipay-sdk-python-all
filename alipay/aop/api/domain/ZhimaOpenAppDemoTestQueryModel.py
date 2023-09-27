#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PublicComplex import PublicComplex
from alipay.aop.api.domain.PublicComplex import PublicComplex


class ZhimaOpenAppDemoTestQueryModel(object):

    def __init__(self):
        self._copy_complex = None
        self._platform_a = None
        self._ref_complex = None
        self._test_1 = None
        self._test_date = None
        self._test_number = None
        self._test_price = None
        self._test_string = None
        self._test_string_open_id = None

    @property
    def copy_complex(self):
        return self._copy_complex

    @copy_complex.setter
    def copy_complex(self, value):
        if isinstance(value, list):
            self._copy_complex = list()
            for i in value:
                if isinstance(i, PublicComplex):
                    self._copy_complex.append(i)
                else:
                    self._copy_complex.append(PublicComplex.from_alipay_dict(i))
    @property
    def platform_a(self):
        return self._platform_a

    @platform_a.setter
    def platform_a(self, value):
        self._platform_a = value
    @property
    def ref_complex(self):
        return self._ref_complex

    @ref_complex.setter
    def ref_complex(self, value):
        if isinstance(value, PublicComplex):
            self._ref_complex = value
        else:
            self._ref_complex = PublicComplex.from_alipay_dict(value)
    @property
    def test_1(self):
        return self._test_1

    @test_1.setter
    def test_1(self, value):
        self._test_1 = value
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
        if self.copy_complex:
            if isinstance(self.copy_complex, list):
                for i in range(0, len(self.copy_complex)):
                    element = self.copy_complex[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.copy_complex[i] = element.to_alipay_dict()
            if hasattr(self.copy_complex, 'to_alipay_dict'):
                params['copy_complex'] = self.copy_complex.to_alipay_dict()
            else:
                params['copy_complex'] = self.copy_complex
        if self.platform_a:
            if hasattr(self.platform_a, 'to_alipay_dict'):
                params['platform_a'] = self.platform_a.to_alipay_dict()
            else:
                params['platform_a'] = self.platform_a
        if self.ref_complex:
            if hasattr(self.ref_complex, 'to_alipay_dict'):
                params['ref_complex'] = self.ref_complex.to_alipay_dict()
            else:
                params['ref_complex'] = self.ref_complex
        if self.test_1:
            if hasattr(self.test_1, 'to_alipay_dict'):
                params['test_1'] = self.test_1.to_alipay_dict()
            else:
                params['test_1'] = self.test_1
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
        o = ZhimaOpenAppDemoTestQueryModel()
        if 'copy_complex' in d:
            o.copy_complex = d['copy_complex']
        if 'platform_a' in d:
            o.platform_a = d['platform_a']
        if 'ref_complex' in d:
            o.ref_complex = d['ref_complex']
        if 'test_1' in d:
            o.test_1 = d['test_1']
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


