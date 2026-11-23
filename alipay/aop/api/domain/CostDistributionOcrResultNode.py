#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CostDistributionOcrResultNode(object):

    def __init__(self):
        self._actor_salary_ratio = None
        self._main_actor_salary_ratio = None
        self._playlet_production_cost = None

    @property
    def actor_salary_ratio(self):
        return self._actor_salary_ratio

    @actor_salary_ratio.setter
    def actor_salary_ratio(self, value):
        self._actor_salary_ratio = value
    @property
    def main_actor_salary_ratio(self):
        return self._main_actor_salary_ratio

    @main_actor_salary_ratio.setter
    def main_actor_salary_ratio(self, value):
        self._main_actor_salary_ratio = value
    @property
    def playlet_production_cost(self):
        return self._playlet_production_cost

    @playlet_production_cost.setter
    def playlet_production_cost(self, value):
        self._playlet_production_cost = value


    def to_alipay_dict(self):
        params = dict()
        if self.actor_salary_ratio:
            if hasattr(self.actor_salary_ratio, 'to_alipay_dict'):
                params['actor_salary_ratio'] = self.actor_salary_ratio.to_alipay_dict()
            else:
                params['actor_salary_ratio'] = self.actor_salary_ratio
        if self.main_actor_salary_ratio:
            if hasattr(self.main_actor_salary_ratio, 'to_alipay_dict'):
                params['main_actor_salary_ratio'] = self.main_actor_salary_ratio.to_alipay_dict()
            else:
                params['main_actor_salary_ratio'] = self.main_actor_salary_ratio
        if self.playlet_production_cost:
            if hasattr(self.playlet_production_cost, 'to_alipay_dict'):
                params['playlet_production_cost'] = self.playlet_production_cost.to_alipay_dict()
            else:
                params['playlet_production_cost'] = self.playlet_production_cost
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CostDistributionOcrResultNode()
        if 'actor_salary_ratio' in d:
            o.actor_salary_ratio = d['actor_salary_ratio']
        if 'main_actor_salary_ratio' in d:
            o.main_actor_salary_ratio = d['main_actor_salary_ratio']
        if 'playlet_production_cost' in d:
            o.playlet_production_cost = d['playlet_production_cost']
        return o


