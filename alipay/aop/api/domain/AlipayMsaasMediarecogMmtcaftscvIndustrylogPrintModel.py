#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayMsaasMediarecogMmtcaftscvIndustrylogPrintModel(object):

    def __init__(self):
        self._business_type = None
        self._log_content = None

    @property
    def business_type(self):
        return self._business_type

    @business_type.setter
    def business_type(self, value):
        self._business_type = value
    @property
    def log_content(self):
        return self._log_content

    @log_content.setter
    def log_content(self, value):
        self._log_content = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_type:
            if hasattr(self.business_type, 'to_alipay_dict'):
                params['business_type'] = self.business_type.to_alipay_dict()
            else:
                params['business_type'] = self.business_type
        if self.log_content:
            if hasattr(self.log_content, 'to_alipay_dict'):
                params['log_content'] = self.log_content.to_alipay_dict()
            else:
                params['log_content'] = self.log_content
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayMsaasMediarecogMmtcaftscvIndustrylogPrintModel()
        if 'business_type' in d:
            o.business_type = d['business_type']
        if 'log_content' in d:
            o.log_content = d['log_content']
        return o


