#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class UserRiskPrediction(object):

    def __init__(self):
        self._phone_recycle_risk_leve = None
        self._refused_payment_risk_level = None

    @property
    def phone_recycle_risk_leve(self):
        return self._phone_recycle_risk_leve

    @phone_recycle_risk_leve.setter
    def phone_recycle_risk_leve(self, value):
        self._phone_recycle_risk_leve = value
    @property
    def refused_payment_risk_level(self):
        return self._refused_payment_risk_level

    @refused_payment_risk_level.setter
    def refused_payment_risk_level(self, value):
        self._refused_payment_risk_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.phone_recycle_risk_leve:
            if hasattr(self.phone_recycle_risk_leve, 'to_alipay_dict'):
                params['phone_recycle_risk_leve'] = self.phone_recycle_risk_leve.to_alipay_dict()
            else:
                params['phone_recycle_risk_leve'] = self.phone_recycle_risk_leve
        if self.refused_payment_risk_level:
            if hasattr(self.refused_payment_risk_level, 'to_alipay_dict'):
                params['refused_payment_risk_level'] = self.refused_payment_risk_level.to_alipay_dict()
            else:
                params['refused_payment_risk_level'] = self.refused_payment_risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserRiskPrediction()
        if 'phone_recycle_risk_leve' in d:
            o.phone_recycle_risk_leve = d['phone_recycle_risk_leve']
        if 'refused_payment_risk_level' in d:
            o.refused_payment_risk_level = d['refused_payment_risk_level']
        return o


