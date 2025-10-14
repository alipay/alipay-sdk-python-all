#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaSignQueryModel(object):

    def __init__(self):
        self._biz_type = None
        self._request_id = None
        self._sign_flow_id = None

    @property
    def biz_type(self):
        return self._biz_type

    @biz_type.setter
    def biz_type(self, value):
        self._biz_type = value
    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        self._request_id = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.biz_type:
            if hasattr(self.biz_type, 'to_alipay_dict'):
                params['biz_type'] = self.biz_type.to_alipay_dict()
            else:
                params['biz_type'] = self.biz_type
        if self.request_id:
            if hasattr(self.request_id, 'to_alipay_dict'):
                params['request_id'] = self.request_id.to_alipay_dict()
            else:
                params['request_id'] = self.request_id
        if self.sign_flow_id:
            if hasattr(self.sign_flow_id, 'to_alipay_dict'):
                params['sign_flow_id'] = self.sign_flow_id.to_alipay_dict()
            else:
                params['sign_flow_id'] = self.sign_flow_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthcaSignQueryModel()
        if 'biz_type' in d:
            o.biz_type = d['biz_type']
        if 'request_id' in d:
            o.request_id = d['request_id']
        if 'sign_flow_id' in d:
            o.sign_flow_id = d['sign_flow_id']
        return o


