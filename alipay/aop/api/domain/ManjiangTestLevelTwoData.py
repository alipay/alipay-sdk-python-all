#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestabc import ManjiangTestabc
from alipay.aop.api.domain.ManjiangTestComplexOneData import ManjiangTestComplexOneData


class ManjiangTestLevelTwoData(object):

    def __init__(self):
        self._open_json = None
        self._sss = None
        self._test_comple_2 = None
        self._test_open_id = None
        self._tets_level_2 = None

    @property
    def open_json(self):
        return self._open_json

    @open_json.setter
    def open_json(self, value):
        self._open_json = value
    @property
    def sss(self):
        return self._sss

    @sss.setter
    def sss(self, value):
        if isinstance(value, ManjiangTestabc):
            self._sss = value
        else:
            self._sss = ManjiangTestabc.from_alipay_dict(value)
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
    def test_open_id(self):
        return self._test_open_id

    @test_open_id.setter
    def test_open_id(self, value):
        self._test_open_id = value
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
        if self.sss:
            if hasattr(self.sss, 'to_alipay_dict'):
                params['sss'] = self.sss.to_alipay_dict()
            else:
                params['sss'] = self.sss
        if self.test_comple_2:
            if hasattr(self.test_comple_2, 'to_alipay_dict'):
                params['test_comple_2'] = self.test_comple_2.to_alipay_dict()
            else:
                params['test_comple_2'] = self.test_comple_2
        if self.test_open_id:
            if hasattr(self.test_open_id, 'to_alipay_dict'):
                params['test_open_id'] = self.test_open_id.to_alipay_dict()
            else:
                params['test_open_id'] = self.test_open_id
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
        if 'sss' in d:
            o.sss = d['sss']
        if 'test_comple_2' in d:
            o.test_comple_2 = d['test_comple_2']
        if 'test_open_id' in d:
            o.test_open_id = d['test_open_id']
        if 'tets_level_2' in d:
            o.tets_level_2 = d['tets_level_2']
        return o


