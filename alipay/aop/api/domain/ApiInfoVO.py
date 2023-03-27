#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ApiInfoVO(object):

    def __init__(self):
        self._api_desc = None
        self._api_name = None

    @property
    def api_desc(self):
        return self._api_desc

    @api_desc.setter
    def api_desc(self, value):
        self._api_desc = value
    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_desc:
            if hasattr(self.api_desc, 'to_alipay_dict'):
                params['api_desc'] = self.api_desc.to_alipay_dict()
            else:
                params['api_desc'] = self.api_desc
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ApiInfoVO()
        if 'api_desc' in d:
            o.api_desc = d['api_desc']
        if 'api_name' in d:
            o.api_name = d['api_name']
        return o


