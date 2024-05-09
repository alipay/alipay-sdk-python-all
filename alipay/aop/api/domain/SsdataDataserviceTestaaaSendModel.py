#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DumTestFFAA import DumTestFFAA


class SsdataDataserviceTestaaaSendModel(object):

    def __init__(self):
        self._body_a = None
        self._tes_1 = None
        self._test_2 = None

    @property
    def body_a(self):
        return self._body_a

    @body_a.setter
    def body_a(self, value):
        if isinstance(value, DumTestFFAA):
            self._body_a = value
        else:
            self._body_a = DumTestFFAA.from_alipay_dict(value)
    @property
    def tes_1(self):
        return self._tes_1

    @tes_1.setter
    def tes_1(self, value):
        self._tes_1 = value
    @property
    def test_2(self):
        return self._test_2

    @test_2.setter
    def test_2(self, value):
        self._test_2 = value


    def to_alipay_dict(self):
        params = dict()
        if self.body_a:
            if hasattr(self.body_a, 'to_alipay_dict'):
                params['body_a'] = self.body_a.to_alipay_dict()
            else:
                params['body_a'] = self.body_a
        if self.tes_1:
            if hasattr(self.tes_1, 'to_alipay_dict'):
                params['tes_1'] = self.tes_1.to_alipay_dict()
            else:
                params['tes_1'] = self.tes_1
        if self.test_2:
            if hasattr(self.test_2, 'to_alipay_dict'):
                params['test_2'] = self.test_2.to_alipay_dict()
            else:
                params['test_2'] = self.test_2
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceTestaaaSendModel()
        if 'body_a' in d:
            o.body_a = d['body_a']
        if 'tes_1' in d:
            o.tes_1 = d['tes_1']
        if 'test_2' in d:
            o.test_2 = d['test_2']
        return o


