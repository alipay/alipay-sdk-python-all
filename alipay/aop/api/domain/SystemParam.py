#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SystemParam(object):

    def __init__(self):
        self._function = None
        self._partner = None
        self._request_id = None

    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, value):
        self._function = value
    @property
    def partner(self):
        return self._partner

    @partner.setter
    def partner(self, value):
        self._partner = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.function:
            if hasattr(self.function, 'to_alipay_dict'):
                params['function'] = self.function.to_alipay_dict()
            else:
                params['function'] = self.function
        if self.partner:
            if hasattr(self.partner, 'to_alipay_dict'):
                params['partner'] = self.partner.to_alipay_dict()
            else:
                params['partner'] = self.partner
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SystemParam()
        if 'function' in d:
            o.function = d['function']
        if 'partner' in d:
            o.partner = d['partner']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


