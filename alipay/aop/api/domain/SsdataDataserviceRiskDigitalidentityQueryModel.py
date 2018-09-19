#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskDigitalidentityQueryModel(object):

    def __init__(self):
        self._device_code = None

    @property
    def device_code(self):
        return self._device_code

    @device_code.setter
    def device_code(self, value):
        self._device_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_code:
            if hasattr(self.device_code, 'to_alipay_dict'):
                params['device_code'] = self.device_code.to_alipay_dict()
            else:
                params['device_code'] = self.device_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskDigitalidentityQueryModel()
        if 'device_code' in d:
            o.device_code = d['device_code']
        return o


