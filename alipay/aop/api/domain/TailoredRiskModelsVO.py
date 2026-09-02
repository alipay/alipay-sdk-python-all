#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class TailoredRiskModelsVO(object):

    def __init__(self):
        self._tailored_risk_level = None

    @property
    def tailored_risk_level(self):
        return self._tailored_risk_level

    @tailored_risk_level.setter
    def tailored_risk_level(self, value):
        self._tailored_risk_level = value


    def to_alipay_dict(self):
        params = dict()
        if self.tailored_risk_level:
            if hasattr(self.tailored_risk_level, 'to_alipay_dict'):
                params['tailored_risk_level'] = self.tailored_risk_level.to_alipay_dict()
            else:
                params['tailored_risk_level'] = self.tailored_risk_level
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = TailoredRiskModelsVO()
        if 'tailored_risk_level' in d:
            o.tailored_risk_level = d['tailored_risk_level']
        return o


