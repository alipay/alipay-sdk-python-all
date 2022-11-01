#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceTestaaaSendModel(object):

    def __init__(self):
        self._tes_1 = None
        self._test_2 = None

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
        if 'tes_1' in d:
            o.tes_1 = d['tes_1']
        if 'test_2' in d:
            o.test_2 = d['test_2']
        return o


