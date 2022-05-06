#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZhimaCreditEpDataapiMigrationQueryModel(object):

    def __init__(self):
        self._api_method = None
        self._api_name = None
        self._api_params = None

    @property
    def api_method(self):
        return self._api_method

    @api_method.setter
    def api_method(self, value):
        self._api_method = value
    @property
    def api_name(self):
        return self._api_name

    @api_name.setter
    def api_name(self, value):
        self._api_name = value
    @property
    def api_params(self):
        return self._api_params

    @api_params.setter
    def api_params(self, value):
        self._api_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.api_method:
            if hasattr(self.api_method, 'to_alipay_dict'):
                params['api_method'] = self.api_method.to_alipay_dict()
            else:
                params['api_method'] = self.api_method
        if self.api_name:
            if hasattr(self.api_name, 'to_alipay_dict'):
                params['api_name'] = self.api_name.to_alipay_dict()
            else:
                params['api_name'] = self.api_name
        if self.api_params:
            if hasattr(self.api_params, 'to_alipay_dict'):
                params['api_params'] = self.api_params.to_alipay_dict()
            else:
                params['api_params'] = self.api_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZhimaCreditEpDataapiMigrationQueryModel()
        if 'api_method' in d:
            o.api_method = d['api_method']
        if 'api_name' in d:
            o.api_name = d['api_name']
        if 'api_params' in d:
            o.api_params = d['api_params']
        return o


