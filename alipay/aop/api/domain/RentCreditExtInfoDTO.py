#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentCreditExtInfoDTO(object):

    def __init__(self):
        self._fee_risk_model = None

    @property
    def fee_risk_model(self):
        return self._fee_risk_model

    @fee_risk_model.setter
    def fee_risk_model(self, value):
        self._fee_risk_model = value


    def to_alipay_dict(self):
        params = dict()
        if self.fee_risk_model:
            if hasattr(self.fee_risk_model, 'to_alipay_dict'):
                params['fee_risk_model'] = self.fee_risk_model.to_alipay_dict()
            else:
                params['fee_risk_model'] = self.fee_risk_model
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentCreditExtInfoDTO()
        if 'fee_risk_model' in d:
            o.fee_risk_model = d['fee_risk_model']
        return o


