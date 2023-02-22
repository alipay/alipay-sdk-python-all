#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BehaviorQueryRequest import BehaviorQueryRequest


class AlipayMerchantQipanBehaviorQueryModel(object):

    def __init__(self):
        self._request_params = None
        self._scene_code = None

    @property
    def request_params(self):
        return self._request_params

    @request_params.setter
    def request_params(self, value):
        if isinstance(value, BehaviorQueryRequest):
            self._request_params = value
        else:
            self._request_params = BehaviorQueryRequest.from_alipay_dict(value)
    @property
    def scene_code(self):
        return self._scene_code

    @scene_code.setter
    def scene_code(self, value):
        self._scene_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_params:
            if hasattr(self.request_params, 'to_alipay_dict'):
                params['request_params'] = self.request_params.to_alipay_dict()
            else:
                params['request_params'] = self.request_params
        if self.scene_code:
            if hasattr(self.scene_code, 'to_alipay_dict'):
                params['scene_code'] = self.scene_code.to_alipay_dict()
            else:
                params['scene_code'] = self.scene_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMerchantQipanBehaviorQueryModel()
        if 'request_params' in d:
            o.request_params = d['request_params']
        if 'scene_code' in d:
            o.scene_code = d['scene_code']
        return o


