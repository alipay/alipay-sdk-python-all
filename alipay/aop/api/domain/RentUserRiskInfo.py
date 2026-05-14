#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentUserRiskInfo(object):

    def __init__(self):
        self._comprehensive_risk_level = None
        self._premium_user_recommend = None

    @property
    def comprehensive_risk_level(self):
        return self._comprehensive_risk_level

    @comprehensive_risk_level.setter
    def comprehensive_risk_level(self, value):
        self._comprehensive_risk_level = value
    @property
    def premium_user_recommend(self):
        return self._premium_user_recommend

    @premium_user_recommend.setter
    def premium_user_recommend(self, value):
        self._premium_user_recommend = value


    def to_alipay_dict(self):
        params = dict()
        if self.comprehensive_risk_level:
            if hasattr(self.comprehensive_risk_level, 'to_alipay_dict'):
                params['comprehensive_risk_level'] = self.comprehensive_risk_level.to_alipay_dict()
            else:
                params['comprehensive_risk_level'] = self.comprehensive_risk_level
        if self.premium_user_recommend:
            if hasattr(self.premium_user_recommend, 'to_alipay_dict'):
                params['premium_user_recommend'] = self.premium_user_recommend.to_alipay_dict()
            else:
                params['premium_user_recommend'] = self.premium_user_recommend
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentUserRiskInfo()
        if 'comprehensive_risk_level' in d:
            o.comprehensive_risk_level = d['comprehensive_risk_level']
        if 'premium_user_recommend' in d:
            o.premium_user_recommend = d['premium_user_recommend']
        return o


