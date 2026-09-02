#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HuiDuTest import HuiDuTest


class AlipayDataDataserviceHuidutestQueryModel(object):

    def __init__(self):
        self._test = None
        self._user = None

    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value):
        self._test = value
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value):
        if isinstance(value, HuiDuTest):
            self._user = value
        else:
            self._user = HuiDuTest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.test:
            if hasattr(self.test, 'to_alipay_dict'):
                params['test'] = self.test.to_alipay_dict()
            else:
                params['test'] = self.test
        if self.user:
            if hasattr(self.user, 'to_alipay_dict'):
                params['user'] = self.user.to_alipay_dict()
            else:
                params['user'] = self.user
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceHuidutestQueryModel()
        if 'test' in d:
            o.test = d['test']
        if 'user' in d:
            o.user = d['user']
        return o


