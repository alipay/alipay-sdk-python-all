#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipaySecurityAipayProcessUploadModel(object):

    def __init__(self):
        self._device_token = None
        self._report_data = None

    @property
    def device_token(self):
        return self._device_token

    @device_token.setter
    def device_token(self, value):
        self._device_token = value
    @property
    def report_data(self):
        return self._report_data

    @report_data.setter
    def report_data(self, value):
        self._report_data = value


    def to_alipay_dict(self):
        params = dict()
        if self.device_token:
            if hasattr(self.device_token, 'to_alipay_dict'):
                params['device_token'] = self.device_token.to_alipay_dict()
            else:
                params['device_token'] = self.device_token
        if self.report_data:
            if hasattr(self.report_data, 'to_alipay_dict'):
                params['report_data'] = self.report_data.to_alipay_dict()
            else:
                params['report_data'] = self.report_data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipaySecurityAipayProcessUploadModel()
        if 'device_token' in d:
            o.device_token = d['device_token']
        if 'report_data' in d:
            o.report_data = d['report_data']
        return o


