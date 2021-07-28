#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AnttechBlockchainFinanceRiskWarningAddModel(object):

    def __init__(self):
        self._out_risk_id = None
        self._risk_info = None

    @property
    def out_risk_id(self):
        return self._out_risk_id

    @out_risk_id.setter
    def out_risk_id(self, value):
        self._out_risk_id = value
    @property
    def risk_info(self):
        return self._risk_info

    @risk_info.setter
    def risk_info(self, value):
        self._risk_info = value


    def to_alipay_dict(self):
        params = dict()
        if self.out_risk_id:
            if hasattr(self.out_risk_id, 'to_alipay_dict'):
                params['out_risk_id'] = self.out_risk_id.to_alipay_dict()
            else:
                params['out_risk_id'] = self.out_risk_id
        if self.risk_info:
            if hasattr(self.risk_info, 'to_alipay_dict'):
                params['risk_info'] = self.risk_info.to_alipay_dict()
            else:
                params['risk_info'] = self.risk_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AnttechBlockchainFinanceRiskWarningAddModel()
        if 'out_risk_id' in d:
            o.out_risk_id = d['out_risk_id']
        if 'risk_info' in d:
            o.risk_info = d['risk_info']
        return o


