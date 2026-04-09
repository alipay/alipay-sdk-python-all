#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalEventRiskAuditModel(object):

    def __init__(self):
        self._out_biz_id = None
        self._request_id = None
        self._risk_event_code = None
        self._risk_params = None

    @property
    def out_biz_id(self):
        return self._out_biz_id

    @out_biz_id.setter
    def out_biz_id(self, value):
        self._out_biz_id = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def risk_event_code(self):
        return self._risk_event_code

    @risk_event_code.setter
    def risk_event_code(self, value):
        self._risk_event_code = value
    @property
    def risk_params(self):
        return self._risk_params

    @risk_params.setter
    def risk_params(self, value):
        self._risk_params = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_biz_id:
            if hasattr(self.out_biz_id, 'to_alipay_dict'):
                params['out_biz_id'] = self.out_biz_id.to_alipay_dict()
            else:
                params['out_biz_id'] = self.out_biz_id
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.risk_event_code:
            if hasattr(self.risk_event_code, 'to_alipay_dict'):
                params['risk_event_code'] = self.risk_event_code.to_alipay_dict()
            else:
                params['risk_event_code'] = self.risk_event_code
        if self.risk_params:
            if hasattr(self.risk_params, 'to_alipay_dict'):
                params['risk_params'] = self.risk_params.to_alipay_dict()
            else:
                params['risk_params'] = self.risk_params
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalEventRiskAuditModel()
        if 'out_biz_id' in d:
            o.out_biz_id = d['out_biz_id']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'risk_event_code' in d:
            o.risk_event_code = d['risk_event_code']
        if 'risk_params' in d:
            o.risk_params = d['risk_params']
        return o


