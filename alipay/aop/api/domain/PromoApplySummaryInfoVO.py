#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PromoApplySummaryInfoVO(object):

    def __init__(self):
        self._apply_amount = None
        self._budget_type = None
        self._member_level = None
        self._promotion_sub_type = None
        self._promotion_type = None

    @property
    def apply_amount(self):
        return self._apply_amount

    @apply_amount.setter
    def apply_amount(self, value):
        self._apply_amount = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def member_level(self):
        return self._member_level

    @member_level.setter
    def member_level(self, value):
        self._member_level = value
    @property
    def promotion_sub_type(self):
        return self._promotion_sub_type

    @promotion_sub_type.setter
    def promotion_sub_type(self, value):
        self._promotion_sub_type = value
    @property
    def promotion_type(self):
        return self._promotion_type

    @promotion_type.setter
    def promotion_type(self, value):
        self._promotion_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amount:
            if hasattr(self.apply_amount, 'to_alipay_dict'):
                params['apply_amount'] = self.apply_amount.to_alipay_dict()
            else:
                params['apply_amount'] = self.apply_amount
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.member_level:
            if hasattr(self.member_level, 'to_alipay_dict'):
                params['member_level'] = self.member_level.to_alipay_dict()
            else:
                params['member_level'] = self.member_level
        if self.promotion_sub_type:
            if hasattr(self.promotion_sub_type, 'to_alipay_dict'):
                params['promotion_sub_type'] = self.promotion_sub_type.to_alipay_dict()
            else:
                params['promotion_sub_type'] = self.promotion_sub_type
        if self.promotion_type:
            if hasattr(self.promotion_type, 'to_alipay_dict'):
                params['promotion_type'] = self.promotion_type.to_alipay_dict()
            else:
                params['promotion_type'] = self.promotion_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PromoApplySummaryInfoVO()
        if 'apply_amount' in d:
            o.apply_amount = d['apply_amount']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'member_level' in d:
            o.member_level = d['member_level']
        if 'promotion_sub_type' in d:
            o.promotion_sub_type = d['promotion_sub_type']
        if 'promotion_type' in d:
            o.promotion_type = d['promotion_type']
        return o


