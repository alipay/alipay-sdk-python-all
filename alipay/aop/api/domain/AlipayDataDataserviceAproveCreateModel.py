#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceAproveCreateModel(object):

    def __init__(self):
        self._test_body = None
        self._test_path = None

    @property
    def test_body(self):
        return self._test_body

    @test_body.setter
    def test_body(self, value):
        self._test_body = value
    @property
    def test_path(self):
        return self._test_path

    @test_path.setter
    def test_path(self, value):
        self._test_path = value


    def to_alipay_dict(self):
        params = dict()
        if self.test_body:
            if hasattr(self.test_body, 'to_alipay_dict'):
                params['test_body'] = self.test_body.to_alipay_dict()
            else:
                params['test_body'] = self.test_body
        if self.test_path:
            if hasattr(self.test_path, 'to_alipay_dict'):
                params['test_path'] = self.test_path.to_alipay_dict()
            else:
                params['test_path'] = self.test_path
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceAproveCreateModel()
        if 'test_body' in d:
            o.test_body = d['test_body']
        if 'test_path' in d:
            o.test_path = d['test_path']
        return o


