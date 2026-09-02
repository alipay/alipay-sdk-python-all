#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentUserRiskInfo(object):

    def __init__(self):
        self._comprehensive_risk_level = None
        self._credit_ability_level = None
        self._current_renting_level = None
        self._intermediary_level = None
        self._premium_user_recommend = None

    @property
    def comprehensive_risk_level(self):
        return self._comprehensive_risk_level

    @comprehensive_risk_level.setter
    def comprehensive_risk_level(self, value):
        self._comprehensive_risk_level = value
    @property
    def credit_ability_level(self):
        return self._credit_ability_level

    @credit_ability_level.setter
    def credit_ability_level(self, value):
        self._credit_ability_level = value
    @property
    def current_renting_level(self):
        return self._current_renting_level

    @current_renting_level.setter
    def current_renting_level(self, value):
        self._current_renting_level = value
    @property
    def intermediary_level(self):
        return self._intermediary_level

    @intermediary_level.setter
    def intermediary_level(self, value):
        self._intermediary_level = value
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
        if self.credit_ability_level:
            if hasattr(self.credit_ability_level, 'to_alipay_dict'):
                params['credit_ability_level'] = self.credit_ability_level.to_alipay_dict()
            else:
                params['credit_ability_level'] = self.credit_ability_level
        if self.current_renting_level:
            if hasattr(self.current_renting_level, 'to_alipay_dict'):
                params['current_renting_level'] = self.current_renting_level.to_alipay_dict()
            else:
                params['current_renting_level'] = self.current_renting_level
        if self.intermediary_level:
            if hasattr(self.intermediary_level, 'to_alipay_dict'):
                params['intermediary_level'] = self.intermediary_level.to_alipay_dict()
            else:
                params['intermediary_level'] = self.intermediary_level
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
        if 'credit_ability_level' in d:
            o.credit_ability_level = d['credit_ability_level']
        if 'current_renting_level' in d:
            o.current_renting_level = d['current_renting_level']
        if 'intermediary_level' in d:
            o.intermediary_level = d['intermediary_level']
        if 'premium_user_recommend' in d:
            o.premium_user_recommend = d['premium_user_recommend']
        return o


