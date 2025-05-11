#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class JhTestResultData(object):

    def __init__(self):
        self._open_id = None
        self._test_result = None

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def test_result(self):
        return self._test_result

    @test_result.setter
    def test_result(self, value):
        self._test_result = value


    def to_alipay_dict(self):
        params = dict()
        if self.open_id:
            if hasattr(self.open_id, 'to_alipay_dict'):
                params['open_id'] = self.open_id.to_alipay_dict()
            else:
                params['open_id'] = self.open_id
        if self.test_result:
            if hasattr(self.test_result, 'to_alipay_dict'):
                params['test_result'] = self.test_result.to_alipay_dict()
            else:
                params['test_result'] = self.test_result
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = JhTestResultData()
        if 'open_id' in d:
            o.open_id = d['open_id']
        if 'test_result' in d:
            o.test_result = d['test_result']
        return o


