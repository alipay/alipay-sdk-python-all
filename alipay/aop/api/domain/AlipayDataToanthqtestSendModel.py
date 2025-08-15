#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.TestHq import TestHq


class AlipayDataToanthqtestSendModel(object):

    def __init__(self):
        self._open_id = None
        self._test = None
        self._test_complex = None
        self._user_id = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def test_complex(self):
        return self._test_complex

    @test_complex.setter
    def test_complex(self, value):
        if isinstance(value, list):
            self._test_complex = list()
            for i in value:
                if isinstance(i, TestHq):
                    self._test_complex.append(i)
                else:
                    self._test_complex.append(TestHq.from_alipay_dict(i))
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        self._user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.test_complex:
            if isinstance(self.test_complex, list):
                for i in range(0, len(self.test_complex)):
                    element = self.test_complex[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.test_complex[i] = element.to_alipay_dict()
            if hasattr(self.test_complex, 'to_alipay_dict'):
                params['test_complex'] = self.test_complex.to_alipay_dict()
            else:
                params['test_complex'] = self.test_complex
        if self.user_id:
            if hasattr(self.user_id, 'to_alipay_dict'):
                params['user_id'] = self.user_id.to_alipay_dict()
            else:
                params['user_id'] = self.user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataToanthqtestSendModel()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'test' in d:
            o.test = d['test']
        if 'test_complex' in d:
            o.test_complex = d['test_complex']
        if 'user_id' in d:
            o.user_id = d['user_id']
        return o


