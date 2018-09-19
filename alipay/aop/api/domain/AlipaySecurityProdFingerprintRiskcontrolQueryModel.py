#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityProdFingerprintRiskcontrolQueryModel(object):

    def __init__(self):
        self._aaid = None
        self._auth_type = None
        self._build_model = None
        self._device_id = None

    @property
    def aaid(self):
        return self._aaid

    @aaid.setter
    def aaid(self, value):
        self._aaid = value
    @property
    def auth_type(self):
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        self._auth_type = value
    @property
    def build_model(self):
        return self._build_model

    @build_model.setter
    def build_model(self, value):
        self._build_model = value
    @property
    def device_id(self):
        return self._device_id

    @device_id.setter
    def device_id(self, value):
        self._device_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.aaid:
            if hasattr(self.aaid, 'to_alipay_dict'):
                params['aaid'] = self.aaid.to_alipay_dict()
            else:
                params['aaid'] = self.aaid
        if self.auth_type:
            if hasattr(self.auth_type, 'to_alipay_dict'):
                params['auth_type'] = self.auth_type.to_alipay_dict()
            else:
                params['auth_type'] = self.auth_type
        if self.build_model:
            if hasattr(self.build_model, 'to_alipay_dict'):
                params['build_model'] = self.build_model.to_alipay_dict()
            else:
                params['build_model'] = self.build_model
        if self.device_id:
            if hasattr(self.device_id, 'to_alipay_dict'):
                params['device_id'] = self.device_id.to_alipay_dict()
            else:
                params['device_id'] = self.device_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityProdFingerprintRiskcontrolQueryModel()
        if 'aaid' in d:
            o.aaid = d['aaid']
        if 'auth_type' in d:
            o.auth_type = d['auth_type']
        if 'build_model' in d:
            o.build_model = d['build_model']
        if 'device_id' in d:
            o.device_id = d['device_id']
        return o


