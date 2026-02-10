#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalHdfrtcConferenceAcceptModel(object):

    def __init__(self):
        self._request_data = None
        self._type = None

    @property
    def request_data(self):
        return self._request_data

    @request_data.setter
    def request_data(self, value):
        self._request_data = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_data:
            if hasattr(self.request_data, 'to_alipay_dict'):
                params['request_data'] = self.request_data.to_alipay_dict()
            else:
                params['request_data'] = self.request_data
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
        o = AlipayCommerceMedicalHdfrtcConferenceAcceptModel()
        if 'request_data' in d:
            o.request_data = d['request_data']
        if 'type' in d:
            o.type = d['type']
        return o


