#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentRiskInfo(object):

    def __init__(self):
        self._risk_result = None
        self._risk_result_desc = None
        self._risk_sense = None

    @property
    def risk_result(self):
        return self._risk_result

    @risk_result.setter
    def risk_result(self, value):
        self._risk_result = value
    @property
    def risk_result_desc(self):
        return self._risk_result_desc

    @risk_result_desc.setter
    def risk_result_desc(self, value):
        self._risk_result_desc = value
    @property
    def risk_sense(self):
        return self._risk_sense

    @risk_sense.setter
    def risk_sense(self, value):
        self._risk_sense = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_result:
            if hasattr(self.risk_result, 'to_alipay_dict'):
                params['risk_result'] = self.risk_result.to_alipay_dict()
            else:
                params['risk_result'] = self.risk_result
        if self.risk_result_desc:
            if hasattr(self.risk_result_desc, 'to_alipay_dict'):
                params['risk_result_desc'] = self.risk_result_desc.to_alipay_dict()
            else:
                params['risk_result_desc'] = self.risk_result_desc
        if self.risk_sense:
            if hasattr(self.risk_sense, 'to_alipay_dict'):
                params['risk_sense'] = self.risk_sense.to_alipay_dict()
            else:
                params['risk_sense'] = self.risk_sense
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentRiskInfo()
        if 'risk_result' in d:
            o.risk_result = d['risk_result']
        if 'risk_result_desc' in d:
            o.risk_result_desc = d['risk_result_desc']
        if 'risk_sense' in d:
            o.risk_sense = d['risk_sense']
        return o


