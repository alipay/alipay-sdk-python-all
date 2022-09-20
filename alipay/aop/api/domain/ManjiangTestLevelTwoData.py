#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestComplexOneData import ManjiangTestComplexOneData


class ManjiangTestLevelTwoData(object):

    def __init__(self):
        self._open_json = None
        self._test_comple_2 = None
        self._tets_level_2 = None

    @property
    def open_json(self):
        return self._open_json

    @open_json.setter
    def open_json(self, value):
        self._open_json = value
    @property
    def test_comple_2(self):
        return self._test_comple_2

    @test_comple_2.setter
    def test_comple_2(self, value):
        if isinstance(value, ManjiangTestComplexOneData):
            self._test_comple_2 = value
        else:
            self._test_comple_2 = ManjiangTestComplexOneData.from_alipay_dict(value)
    @property
    def tets_level_2(self):
        return self._tets_level_2

    @tets_level_2.setter
    def tets_level_2(self, value):
        self._tets_level_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_json:
            if hasattr(self.open_json, 'to_alipay_dict'):
                params['open_json'] = self.open_json.to_alipay_dict()
            else:
                params['open_json'] = self.open_json
        if self.test_comple_2:
            if hasattr(self.test_comple_2, 'to_alipay_dict'):
                params['test_comple_2'] = self.test_comple_2.to_alipay_dict()
            else:
                params['test_comple_2'] = self.test_comple_2
        if self.tets_level_2:
            if hasattr(self.tets_level_2, 'to_alipay_dict'):
                params['tets_level_2'] = self.tets_level_2.to_alipay_dict()
            else:
                params['tets_level_2'] = self.tets_level_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestLevelTwoData()
        if 'open_json' in d:
            o.open_json = d['open_json']
        if 'test_comple_2' in d:
            o.test_comple_2 = d['test_comple_2']
        if 'tets_level_2' in d:
            o.tets_level_2 = d['tets_level_2']
        return o


