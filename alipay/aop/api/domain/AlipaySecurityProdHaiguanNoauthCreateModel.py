#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdHaiguanNoauthCreateModel(object):

    def __init__(self):
        self._haha = None
        self._test = None

    @property
    def haha(self):
        return self._haha

    @haha.setter
    def haha(self, value):
        self._haha = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        if isinstance(value, list):
            self._test = list()
            for i in value:
                self._test.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.haha:
            if hasattr(self.haha, 'to_alipay_dict'):
                params['haha'] = self.haha.to_alipay_dict()
            else:
                params['haha'] = self.haha
        if self.test:
            if isinstance(self.test, list):
                for i in range(0, len(self.test)):
                    element = self.test[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test[i] = element.to_alipay_dict()
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdHaiguanNoauthCreateModel()
        if 'haha' in d:
            o.haha = d['haha']
        if 'test' in d:
            o.test = d['test']
        return o


