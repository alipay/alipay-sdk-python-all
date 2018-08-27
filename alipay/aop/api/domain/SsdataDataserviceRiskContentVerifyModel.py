#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SsdataDataserviceRiskContentVerifyModel(object):

    def __init__(self):
        self._content = None
        self._risk_type = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def risk_type(self):
        return self._risk_type

    @risk_type.setter
    def risk_type(self, value):
        self._risk_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.content:
            if hasattr(self.content, 'to_alipay_dict'):
                params['content'] = self.content.to_alipay_dict()
            else:
                params['content'] = self.content
        if self.risk_type:
            if hasattr(self.risk_type, 'to_alipay_dict'):
                params['risk_type'] = self.risk_type.to_alipay_dict()
            else:
                params['risk_type'] = self.risk_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SsdataDataserviceRiskContentVerifyModel()
        if 'content' in d:
            o.content = d['content']
        if 'risk_type' in d:
            o.risk_type = d['risk_type']
        return o


