#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestLevelTwoData import ManjiangTestLevelTwoData
from alipay.aop.api.domain.ManjiangTestLevelTwoData import ManjiangTestLevelTwoData


class ManjiangTestThreeData(object):

    def __init__(self):
        self._new_field = None
        self._test_complex = None
        self._test_complex_1 = None
        self._test_level_three = None

    @property
    def new_field(self):
        return self._new_field

    @new_field.setter
    def new_field(self, value):
        self._new_field = value
    @property
    def test_complex(self):
        return self._test_complex

    @test_complex.setter
    def test_complex(self, value):
        if isinstance(value, ManjiangTestLevelTwoData):
            self._test_complex = value
        else:
            self._test_complex = ManjiangTestLevelTwoData.from_alipay_dict(value)
    @property
    def test_complex_1(self):
        return self._test_complex_1

    @test_complex_1.setter
    def test_complex_1(self, value):
        if isinstance(value, ManjiangTestLevelTwoData):
            self._test_complex_1 = value
        else:
            self._test_complex_1 = ManjiangTestLevelTwoData.from_alipay_dict(value)
    @property
    def test_level_three(self):
        return self._test_level_three

    @test_level_three.setter
    def test_level_three(self, value):
        self._test_level_three = value


    def to_alipay_dict(self):
        params = dict()
        if self.new_field:
            if hasattr(self.new_field, 'to_alipay_dict'):
                params['new_field'] = self.new_field.to_alipay_dict()
            else:
                params['new_field'] = self.new_field
        if self.test_complex:
            if hasattr(self.test_complex, 'to_alipay_dict'):
                params['test_complex'] = self.test_complex.to_alipay_dict()
            else:
                params['test_complex'] = self.test_complex
        if self.test_complex_1:
            if hasattr(self.test_complex_1, 'to_alipay_dict'):
                params['test_complex_1'] = self.test_complex_1.to_alipay_dict()
            else:
                params['test_complex_1'] = self.test_complex_1
        if self.test_level_three:
            if hasattr(self.test_level_three, 'to_alipay_dict'):
                params['test_level_three'] = self.test_level_three.to_alipay_dict()
            else:
                params['test_level_three'] = self.test_level_three
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestThreeData()
        if 'new_field' in d:
            o.new_field = d['new_field']
        if 'test_complex' in d:
            o.test_complex = d['test_complex']
        if 'test_complex_1' in d:
            o.test_complex_1 = d['test_complex_1']
        if 'test_level_three' in d:
            o.test_level_three = d['test_level_three']
        return o


