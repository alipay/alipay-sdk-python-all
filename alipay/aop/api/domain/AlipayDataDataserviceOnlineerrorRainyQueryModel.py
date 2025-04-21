#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.RainyComplexTypesTheSecond import RainyComplexTypesTheSecond
from alipay.aop.api.domain.RainyComplexTypesTheFirst import RainyComplexTypesTheFirst


class AlipayDataDataserviceOnlineerrorRainyQueryModel(object):

    def __init__(self):
        self._complex_type_twice = None
        self._test_case_complex_input = None
        self._test_case_is_must_input = None

    @property
    def complex_type_twice(self):
        return self._complex_type_twice

    @complex_type_twice.setter
    def complex_type_twice(self, value):
        if isinstance(value, RainyComplexTypesTheSecond):
            self._complex_type_twice = value
        else:
            self._complex_type_twice = RainyComplexTypesTheSecond.from_alipay_dict(value)
    @property
    def test_case_complex_input(self):
        return self._test_case_complex_input

    @test_case_complex_input.setter
    def test_case_complex_input(self, value):
        if isinstance(value, RainyComplexTypesTheFirst):
            self._test_case_complex_input = value
        else:
            self._test_case_complex_input = RainyComplexTypesTheFirst.from_alipay_dict(value)
    @property
    def test_case_is_must_input(self):
        return self._test_case_is_must_input

    @test_case_is_must_input.setter
    def test_case_is_must_input(self, value):
        self._test_case_is_must_input = value


    def to_alipay_dict(self):
        params = dict()
        if self.complex_type_twice:
            if hasattr(self.complex_type_twice, 'to_alipay_dict'):
                params['complex_type_twice'] = self.complex_type_twice.to_alipay_dict()
            else:
                params['complex_type_twice'] = self.complex_type_twice
        if self.test_case_complex_input:
            if hasattr(self.test_case_complex_input, 'to_alipay_dict'):
                params['test_case_complex_input'] = self.test_case_complex_input.to_alipay_dict()
            else:
                params['test_case_complex_input'] = self.test_case_complex_input
        if self.test_case_is_must_input:
            if hasattr(self.test_case_is_must_input, 'to_alipay_dict'):
                params['test_case_is_must_input'] = self.test_case_is_must_input.to_alipay_dict()
            else:
                params['test_case_is_must_input'] = self.test_case_is_must_input
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceOnlineerrorRainyQueryModel()
        if 'complex_type_twice' in d:
            o.complex_type_twice = d['complex_type_twice']
        if 'test_case_complex_input' in d:
            o.test_case_complex_input = d['test_case_complex_input']
        if 'test_case_is_must_input' in d:
            o.test_case_is_must_input = d['test_case_is_must_input']
        return o


