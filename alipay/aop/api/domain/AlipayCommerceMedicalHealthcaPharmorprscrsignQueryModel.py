#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHealthcaPharmorprscrsignQueryModel(object):

    def __init__(self):
        self._history_request_id = None
        self._sign_flow_id = None
        self._type = None

    @property
    def history_request_id(self):
        return self._history_request_id

    @history_request_id.setter
    def history_request_id(self, value):
        self._history_request_id = value
    @property
    def sign_flow_id(self):
        return self._sign_flow_id

    @sign_flow_id.setter
    def sign_flow_id(self, value):
        self._sign_flow_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.history_request_id:
            if hasattr(self.history_request_id, 'to_alipay_dict'):
                params['history_request_id'] = self.history_request_id.to_alipay_dict()
            else:
                params['history_request_id'] = self.history_request_id
        if self.sign_flow_id:
            if hasattr(self.sign_flow_id, 'to_alipay_dict'):
                params['sign_flow_id'] = self.sign_flow_id.to_alipay_dict()
            else:
                params['sign_flow_id'] = self.sign_flow_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalHealthcaPharmorprscrsignQueryModel()
        if 'history_request_id' in d:
            o.history_request_id = d['history_request_id']
        if 'sign_flow_id' in d:
            o.sign_flow_id = d['sign_flow_id']
        if 'type' in d:
            o.type = d['type']
        return o


