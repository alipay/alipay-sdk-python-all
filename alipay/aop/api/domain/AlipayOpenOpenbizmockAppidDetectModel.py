#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenOpenbizmockAppidDetectModel(object):

    def __init__(self):
        self._app_number = None

    @property
    def app_number(self):
        return self._app_number

    @app_number.setter
    def app_number(self, value):
        self._app_number = value


    def to_alipay_dict(self):
        params = dict()
        if self.app_number:
            if hasattr(self.app_number, 'to_alipay_dict'):
                params['app_number'] = self.app_number.to_alipay_dict()
            else:
                params['app_number'] = self.app_number
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenOpenbizmockAppidDetectModel()
        if 'app_number' in d:
            o.app_number = d['app_number']
        return o


