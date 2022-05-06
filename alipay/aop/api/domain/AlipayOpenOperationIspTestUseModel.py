#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOperationIspTestUseModel(object):

    def __init__(self):
        self._app = None
        self._input = None

    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, value):
        self._app = value
    @property
    def input(self):
        return self._input

    @input.setter
    def input(self, value):
        self._input = value


    def to_alipay_dict(self):
        params = dict()
        if self.app:
            if hasattr(self.app, 'to_alipay_dict'):
                params['app'] = self.app.to_alipay_dict()
            else:
                params['app'] = self.app
        if self.input:
            if hasattr(self.input, 'to_alipay_dict'):
                params['input'] = self.input.to_alipay_dict()
            else:
                params['input'] = self.input
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOperationIspTestUseModel()
        if 'app' in d:
            o.app = d['app']
        if 'input' in d:
            o.input = d['input']
        return o


