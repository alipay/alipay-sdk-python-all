#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RiskMetaData(object):

    def __init__(self):
        self._op_type = None
        self._risk_meta_data_content = None
        self._risk_meta_data_type = None

    @property
    def op_type(self):
        return self._op_type

    @op_type.setter
    def op_type(self, value):
        self._op_type = value
    @property
    def risk_meta_data_content(self):
        return self._risk_meta_data_content

    @risk_meta_data_content.setter
    def risk_meta_data_content(self, value):
        self._risk_meta_data_content = value
    @property
    def risk_meta_data_type(self):
        return self._risk_meta_data_type

    @risk_meta_data_type.setter
    def risk_meta_data_type(self, value):
        self._risk_meta_data_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.op_type:
            if hasattr(self.op_type, 'to_alipay_dict'):
                params['op_type'] = self.op_type.to_alipay_dict()
            else:
                params['op_type'] = self.op_type
        if self.risk_meta_data_content:
            if hasattr(self.risk_meta_data_content, 'to_alipay_dict'):
                params['risk_meta_data_content'] = self.risk_meta_data_content.to_alipay_dict()
            else:
                params['risk_meta_data_content'] = self.risk_meta_data_content
        if self.risk_meta_data_type:
            if hasattr(self.risk_meta_data_type, 'to_alipay_dict'):
                params['risk_meta_data_type'] = self.risk_meta_data_type.to_alipay_dict()
            else:
                params['risk_meta_data_type'] = self.risk_meta_data_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RiskMetaData()
        if 'op_type' in d:
            o.op_type = d['op_type']
        if 'risk_meta_data_content' in d:
            o.risk_meta_data_content = d['risk_meta_data_content']
        if 'risk_meta_data_type' in d:
            o.risk_meta_data_type = d['risk_meta_data_type']
        return o


