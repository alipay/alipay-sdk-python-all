#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestLevelTwoData import ManjiangTestLevelTwoData


class ManjiangTestThreeData(object):

    def __init__(self):
        self._test_complex = None
        self._test_level_three = None

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
    def test_level_three(self):
        return self._test_level_three

    @test_level_three.setter
    def test_level_three(self, value):
        self._test_level_three = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_complex:
            if hasattr(self.test_complex, 'to_alipay_dict'):
                params['test_complex'] = self.test_complex.to_alipay_dict()
            else:
                params['test_complex'] = self.test_complex
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
        if 'test_complex' in d:
            o.test_complex = d['test_complex']
        if 'test_level_three' in d:
            o.test_level_three = d['test_level_three']
        return o


