#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenDanielTestQueryModel(object):

    def __init__(self):
        self._body_str = None
        self._strig_dtest = None

    @property
    def body_str(self):
        return self._body_str

    @body_str.setter
    def body_str(self, value):
        self._body_str = value
    @property
    def strig_dtest(self):
        return self._strig_dtest

    @strig_dtest.setter
    def strig_dtest(self, value):
        self._strig_dtest = value


    def to_alipay_dict(self):
        params = dict()
        if self.body_str:
            if hasattr(self.body_str, 'to_alipay_dict'):
                params['body_str'] = self.body_str.to_alipay_dict()
            else:
                params['body_str'] = self.body_str
        if self.strig_dtest:
            if hasattr(self.strig_dtest, 'to_alipay_dict'):
                params['strig_dtest'] = self.strig_dtest.to_alipay_dict()
            else:
                params['strig_dtest'] = self.strig_dtest
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenDanielTestQueryModel()
        if 'body_str' in d:
            o.body_str = d['body_str']
        if 'strig_dtest' in d:
            o.strig_dtest = d['strig_dtest']
        return o


