#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class DatadigitalAnttechAmpAigcQueryModel(object):

    def __init__(self):
        self._param_data = None
        self._request_id = None
        self._social_code = None

    @property
    def param_data(self):
        return self._param_data

    @param_data.setter
    def param_data(self, value):
        self._param_data = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def social_code(self):
        return self._social_code

    @social_code.setter
    def social_code(self, value):
        self._social_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.param_data:
            if hasattr(self.param_data, 'to_alipay_dict'):
                params['param_data'] = self.param_data.to_alipay_dict()
            else:
                params['param_data'] = self.param_data
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.social_code:
            if hasattr(self.social_code, 'to_alipay_dict'):
                params['social_code'] = self.social_code.to_alipay_dict()
            else:
                params['social_code'] = self.social_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = DatadigitalAnttechAmpAigcQueryModel()
        if 'param_data' in d:
            o.param_data = d['param_data']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'social_code' in d:
            o.social_code = d['social_code']
        return o


