#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalInsuranceQhinsplatSigninModel(object):

    def __init__(self):
        self._request_str = None

    @property
    def request_str(self):
        return self._request_str

    @request_str.setter
    def request_str(self, value):
        self._request_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.request_str:
            if hasattr(self.request_str, 'to_alipay_dict'):
                params['request_str'] = self.request_str.to_alipay_dict()
            else:
                params['request_str'] = self.request_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalInsuranceQhinsplatSigninModel()
        if 'request_str' in d:
            o.request_str = d['request_str']
        return o


