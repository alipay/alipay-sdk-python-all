#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenAppQqwAaatestConfirmModel(object):

    def __init__(self):
        self._json = None

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value


    def to_alipay_dict(self):
        params = dict()
        if self.json:
            if hasattr(self.json, 'to_alipay_dict'):
                params['json'] = self.json.to_alipay_dict()
            else:
                params['json'] = self.json
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenAppQqwAaatestConfirmModel()
        if 'json' in d:
            o.json = d['json']
        return o


