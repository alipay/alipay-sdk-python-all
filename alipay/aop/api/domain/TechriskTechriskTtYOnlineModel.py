#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestab import ManjiangTestab


class TechriskTechriskTtYOnlineModel(object):

    def __init__(self):
        self._test_1 = None

    @property
    def test_1(self):
        return self._test_1

    @test_1.setter
    def test_1(self, value):
        if isinstance(value, ManjiangTestab):
            self._test_1 = value
        else:
            self._test_1 = ManjiangTestab.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.test_1:
            if hasattr(self.test_1, 'to_alipay_dict'):
                params['test_1'] = self.test_1.to_alipay_dict()
            else:
                params['test_1'] = self.test_1
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TechriskTechriskTtYOnlineModel()
        if 'test_1' in d:
            o.test_1 = d['test_1']
        return o


