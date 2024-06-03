#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayIserviceComponentcontextQueryModel(object):

    def __init__(self):
        self._request_id = None
        self._source_component_code = None
        self._target_component_code = None

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def source_component_code(self):
        return self._source_component_code

    @source_component_code.setter
    def source_component_code(self, value):
        self._source_component_code = value
    @property
    def target_component_code(self):
        return self._target_component_code

    @target_component_code.setter
    def target_component_code(self, value):
        self._target_component_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.source_component_code:
            if hasattr(self.source_component_code, 'to_alipay_dict'):
                params['source_component_code'] = self.source_component_code.to_alipay_dict()
            else:
                params['source_component_code'] = self.source_component_code
        if self.target_component_code:
            if hasattr(self.target_component_code, 'to_alipay_dict'):
                params['target_component_code'] = self.target_component_code.to_alipay_dict()
            else:
                params['target_component_code'] = self.target_component_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceComponentcontextQueryModel()
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'source_component_code' in d:
            o.source_component_code = d['source_component_code']
        if 'target_component_code' in d:
            o.target_component_code = d['target_component_code']
        return o


