#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TransferResultInfo import TransferResultInfo


class AlipayMarketingToolXuanyitestCreateModel(object):

    def __init__(self):
        self._test_12 = None

    @property
    def test_12(self):
        return self._test_12

    @test_12.setter
    def test_12(self, value):
        if isinstance(value, list):
            self._test_12 = list()
            for i in value:
                if isinstance(i, TransferResultInfo):
                    self._test_12.append(i)
                else:
                    self._test_12.append(TransferResultInfo.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.test_12:
            if isinstance(self.test_12, list):
                for i in range(0, len(self.test_12)):
                    element = self.test_12[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_12[i] = element.to_alipay_dict()
            if hasattr(self.test_12, 'to_alipay_dict'):
                params['test_12'] = self.test_12.to_alipay_dict()
            else:
                params['test_12'] = self.test_12
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMarketingToolXuanyitestCreateModel()
        if 'test_12' in d:
            o.test_12 = d['test_12']
        return o


