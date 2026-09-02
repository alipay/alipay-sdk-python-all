#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShipAssessmentResultVO(object):

    def __init__(self):
        self._error_reason = None
        self._ship_advice = None

    @property
    def error_reason(self):
        return self._error_reason

    @error_reason.setter
    def error_reason(self, value):
        self._error_reason = value
    @property
    def ship_advice(self):
        return self._ship_advice

    @ship_advice.setter
    def ship_advice(self, value):
        self._ship_advice = value


    def to_alipay_dict(self):
        params = dict()
        if self.error_reason:
            if hasattr(self.error_reason, 'to_alipay_dict'):
                params['error_reason'] = self.error_reason.to_alipay_dict()
            else:
                params['error_reason'] = self.error_reason
        if self.ship_advice:
            if hasattr(self.ship_advice, 'to_alipay_dict'):
                params['ship_advice'] = self.ship_advice.to_alipay_dict()
            else:
                params['ship_advice'] = self.ship_advice
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShipAssessmentResultVO()
        if 'error_reason' in d:
            o.error_reason = d['error_reason']
        if 'ship_advice' in d:
            o.ship_advice = d['ship_advice']
        return o


