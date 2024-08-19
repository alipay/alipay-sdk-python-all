#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiAnalysisCommonRequest import OpenApiAnalysisCommonRequest


class AlipayCloudCloudpromoAnalysisoverviewApplistQueryModel(object):

    def __init__(self):
        self._common_request = None
        self._hit_app_id = None
        self._merchant_id = None

    @property
    def common_request(self):
        return self._common_request

    @common_request.setter
    def common_request(self, value):
        if isinstance(value, OpenApiAnalysisCommonRequest):
            self._common_request = value
        else:
            self._common_request = OpenApiAnalysisCommonRequest.from_alipay_dict(value)
    @property
    def hit_app_id(self):
        return self._hit_app_id

    @hit_app_id.setter
    def hit_app_id(self, value):
        self._hit_app_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.common_request:
            if hasattr(self.common_request, 'to_alipay_dict'):
                params['common_request'] = self.common_request.to_alipay_dict()
            else:
                params['common_request'] = self.common_request
        if self.hit_app_id:
            if hasattr(self.hit_app_id, 'to_alipay_dict'):
                params['hit_app_id'] = self.hit_app_id.to_alipay_dict()
            else:
                params['hit_app_id'] = self.hit_app_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCloudCloudpromoAnalysisoverviewApplistQueryModel()
        if 'common_request' in d:
            o.common_request = d['common_request']
        if 'hit_app_id' in d:
            o.hit_app_id = d['hit_app_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


