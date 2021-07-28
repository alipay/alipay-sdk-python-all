#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IntentQueryRequest import IntentQueryRequest


class AlipayIserviceIotIntentQueryModel(object):

    def __init__(self):
        self._iot_request = None

    @property
    def iot_request(self):
        return self._iot_request

    @iot_request.setter
    def iot_request(self, value):
        if isinstance(value, IntentQueryRequest):
            self._iot_request = value
        else:
            self._iot_request = IntentQueryRequest.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.iot_request:
            if hasattr(self.iot_request, 'to_alipay_dict'):
                params['iot_request'] = self.iot_request.to_alipay_dict()
            else:
                params['iot_request'] = self.iot_request
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayIserviceIotIntentQueryModel()
        if 'iot_request' in d:
            o.iot_request = d['iot_request']
        return o


