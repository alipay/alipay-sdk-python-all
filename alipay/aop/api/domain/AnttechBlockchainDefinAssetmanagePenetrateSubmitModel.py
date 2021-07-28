#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainDefinAssetmanagePenetrateSubmitModel(object):

    def __init__(self):
        self._biz_params = None
        self._function = None
        self._request_id = None

    @property
    def biz_params(self):
        return self._biz_params

    @biz_params.setter
    def biz_params(self, value):
        self._biz_params = value
    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, value):
        self._function = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_params:
            if hasattr(self.biz_params, 'to_alipay_dict'):
                params['biz_params'] = self.biz_params.to_alipay_dict()
            else:
                params['biz_params'] = self.biz_params
        if self.function:
            if hasattr(self.function, 'to_alipay_dict'):
                params['function'] = self.function.to_alipay_dict()
            else:
                params['function'] = self.function
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
        o = AnttechBlockchainDefinAssetmanagePenetrateSubmitModel()
        if 'biz_params' in d:
            o.biz_params = d['biz_params']
        if 'function' in d:
            o.function = d['function']
        if 'request_id' in d:
            o.request_id = d['request_id']
        return o


