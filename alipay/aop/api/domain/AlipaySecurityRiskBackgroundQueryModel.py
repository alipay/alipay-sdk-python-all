#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityRiskBackgroundQueryModel(object):

    def __init__(self):
        self._params = None
        self._partner_name = None

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, value):
        self._params = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.params:
            if hasattr(self.params, 'to_alipay_dict'):
                params['params'] = self.params.to_alipay_dict()
            else:
                params['params'] = self.params
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityRiskBackgroundQueryModel()
        if 'params' in d:
            o.params = d['params']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        return o


