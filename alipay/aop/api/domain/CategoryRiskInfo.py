#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class CategoryRiskInfo(object):

    def __init__(self):
        self._category_code = None
        self._category_name = None
        self._global_orders_limit_number = None
        self._global_quota_switch = None
        self._part_deposit_switch = None
        self._risk_policy = None
        self._score = None

    @property
    def category_code(self):
        return self._category_code

    @category_code.setter
    def category_code(self, value):
        self._category_code = value
    @property
    def category_name(self):
        return self._category_name

    @category_name.setter
    def category_name(self, value):
        self._category_name = value
    @property
    def global_orders_limit_number(self):
        return self._global_orders_limit_number

    @global_orders_limit_number.setter
    def global_orders_limit_number(self, value):
        self._global_orders_limit_number = value
    @property
    def global_quota_switch(self):
        return self._global_quota_switch

    @global_quota_switch.setter
    def global_quota_switch(self, value):
        self._global_quota_switch = value
    @property
    def part_deposit_switch(self):
        return self._part_deposit_switch

    @part_deposit_switch.setter
    def part_deposit_switch(self, value):
        self._part_deposit_switch = value
    @property
    def risk_policy(self):
        return self._risk_policy

    @risk_policy.setter
    def risk_policy(self, value):
        self._risk_policy = value
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value


    def to_alipay_dict(self):
        params = dict()
        if self.category_code:
            if hasattr(self.category_code, 'to_alipay_dict'):
                params['category_code'] = self.category_code.to_alipay_dict()
            else:
                params['category_code'] = self.category_code
        if self.category_name:
            if hasattr(self.category_name, 'to_alipay_dict'):
                params['category_name'] = self.category_name.to_alipay_dict()
            else:
                params['category_name'] = self.category_name
        if self.global_orders_limit_number:
            if hasattr(self.global_orders_limit_number, 'to_alipay_dict'):
                params['global_orders_limit_number'] = self.global_orders_limit_number.to_alipay_dict()
            else:
                params['global_orders_limit_number'] = self.global_orders_limit_number
        if self.global_quota_switch:
            if hasattr(self.global_quota_switch, 'to_alipay_dict'):
                params['global_quota_switch'] = self.global_quota_switch.to_alipay_dict()
            else:
                params['global_quota_switch'] = self.global_quota_switch
        if self.part_deposit_switch:
            if hasattr(self.part_deposit_switch, 'to_alipay_dict'):
                params['part_deposit_switch'] = self.part_deposit_switch.to_alipay_dict()
            else:
                params['part_deposit_switch'] = self.part_deposit_switch
        if self.risk_policy:
            if hasattr(self.risk_policy, 'to_alipay_dict'):
                params['risk_policy'] = self.risk_policy.to_alipay_dict()
            else:
                params['risk_policy'] = self.risk_policy
        if self.score:
            if hasattr(self.score, 'to_alipay_dict'):
                params['score'] = self.score.to_alipay_dict()
            else:
                params['score'] = self.score
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = CategoryRiskInfo()
        if 'category_code' in d:
            o.category_code = d['category_code']
        if 'category_name' in d:
            o.category_name = d['category_name']
        if 'global_orders_limit_number' in d:
            o.global_orders_limit_number = d['global_orders_limit_number']
        if 'global_quota_switch' in d:
            o.global_quota_switch = d['global_quota_switch']
        if 'part_deposit_switch' in d:
            o.part_deposit_switch = d['part_deposit_switch']
        if 'risk_policy' in d:
            o.risk_policy = d['risk_policy']
        if 'score' in d:
            o.score = d['score']
        return o


