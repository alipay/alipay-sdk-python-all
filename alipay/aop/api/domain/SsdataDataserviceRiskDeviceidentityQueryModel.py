#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskDeviceidentityQueryModel(object):

    def __init__(self):
        self._device_token = None

    @property
    def device_token(self):
        return self._device_token

    @device_token.setter
    def device_token(self, value):
        self._device_token = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_token:
            if hasattr(self.device_token, 'to_alipay_dict'):
                params['device_token'] = self.device_token.to_alipay_dict()
            else:
                params['device_token'] = self.device_token
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskDeviceidentityQueryModel()
        if 'device_token' in d:
            o.device_token = d['device_token']
        return o


