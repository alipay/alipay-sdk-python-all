#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApmobileAppUsedApiDTO(object):

    def __init__(self):
        self._api_desc = None
        self._bundle = None
        self._method_info = None
        self._stmt = None

    @property
    def api_desc(self):
        return self._api_desc

    @api_desc.setter
    def api_desc(self, value):
        self._api_desc = value
    @property
    def bundle(self):
        return self._bundle

    @bundle.setter
    def bundle(self, value):
        self._bundle = value
    @property
    def method_info(self):
        return self._method_info

    @method_info.setter
    def method_info(self, value):
        self._method_info = value
    @property
    def stmt(self):
        return self._stmt

    @stmt.setter
    def stmt(self, value):
        self._stmt = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_desc:
            if hasattr(self.api_desc, 'to_alipay_dict'):
                params['api_desc'] = self.api_desc.to_alipay_dict()
            else:
                params['api_desc'] = self.api_desc
        if self.bundle:
            if hasattr(self.bundle, 'to_alipay_dict'):
                params['bundle'] = self.bundle.to_alipay_dict()
            else:
                params['bundle'] = self.bundle
        if self.method_info:
            if hasattr(self.method_info, 'to_alipay_dict'):
                params['method_info'] = self.method_info.to_alipay_dict()
            else:
                params['method_info'] = self.method_info
        if self.stmt:
            if hasattr(self.stmt, 'to_alipay_dict'):
                params['stmt'] = self.stmt.to_alipay_dict()
            else:
                params['stmt'] = self.stmt
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApmobileAppUsedApiDTO()
        if 'api_desc' in d:
            o.api_desc = d['api_desc']
        if 'bundle' in d:
            o.bundle = d['bundle']
        if 'method_info' in d:
            o.method_info = d['method_info']
        if 'stmt' in d:
            o.stmt = d['stmt']
        return o


