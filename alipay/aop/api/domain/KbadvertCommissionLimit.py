#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KbadvertCommissionLimit(object):

    def __init__(self):
        self._commission_user_type = None
        self._level = None
        self._max_max_amount = None
        self._max_quota_amount = None
        self._min_commission_percentage = None
        self._min_quota_amount = None

    @property
    def commission_user_type(self):
        return self._commission_user_type

    @commission_user_type.setter
    def commission_user_type(self, value):
        self._commission_user_type = value
    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
    @property
    def max_max_amount(self):
        return self._max_max_amount

    @max_max_amount.setter
    def max_max_amount(self, value):
        self._max_max_amount = value
    @property
    def max_quota_amount(self):
        return self._max_quota_amount

    @max_quota_amount.setter
    def max_quota_amount(self, value):
        self._max_quota_amount = value
    @property
    def min_commission_percentage(self):
        return self._min_commission_percentage

    @min_commission_percentage.setter
    def min_commission_percentage(self, value):
        self._min_commission_percentage = value
    @property
    def min_quota_amount(self):
        return self._min_quota_amount

    @min_quota_amount.setter
    def min_quota_amount(self, value):
        self._min_quota_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.commission_user_type:
            if hasattr(self.commission_user_type, 'to_alipay_dict'):
                params['commission_user_type'] = self.commission_user_type.to_alipay_dict()
            else:
                params['commission_user_type'] = self.commission_user_type
        if self.level:
            if hasattr(self.level, 'to_alipay_dict'):
                params['level'] = self.level.to_alipay_dict()
            else:
                params['level'] = self.level
        if self.max_max_amount:
            if hasattr(self.max_max_amount, 'to_alipay_dict'):
                params['max_max_amount'] = self.max_max_amount.to_alipay_dict()
            else:
                params['max_max_amount'] = self.max_max_amount
        if self.max_quota_amount:
            if hasattr(self.max_quota_amount, 'to_alipay_dict'):
                params['max_quota_amount'] = self.max_quota_amount.to_alipay_dict()
            else:
                params['max_quota_amount'] = self.max_quota_amount
        if self.min_commission_percentage:
            if hasattr(self.min_commission_percentage, 'to_alipay_dict'):
                params['min_commission_percentage'] = self.min_commission_percentage.to_alipay_dict()
            else:
                params['min_commission_percentage'] = self.min_commission_percentage
        if self.min_quota_amount:
            if hasattr(self.min_quota_amount, 'to_alipay_dict'):
                params['min_quota_amount'] = self.min_quota_amount.to_alipay_dict()
            else:
                params['min_quota_amount'] = self.min_quota_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KbadvertCommissionLimit()
        if 'commission_user_type' in d:
            o.commission_user_type = d['commission_user_type']
        if 'level' in d:
            o.level = d['level']
        if 'max_max_amount' in d:
            o.max_max_amount = d['max_max_amount']
        if 'max_quota_amount' in d:
            o.max_quota_amount = d['max_quota_amount']
        if 'min_commission_percentage' in d:
            o.min_commission_percentage = d['min_commission_percentage']
        if 'min_quota_amount' in d:
            o.min_quota_amount = d['min_quota_amount']
        return o


