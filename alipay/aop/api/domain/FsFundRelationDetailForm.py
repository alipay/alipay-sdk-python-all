#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class FsFundRelationDetailForm(object):

    def __init__(self):
        self._allowed_float_up = None
        self._allows_skip_budget_deduction = None
        self._ceiling_amount = None
        self._fund_principal = None
        self._fund_priority = None
        self._fund_provider = None
        self._fund_ratio = None
        self._fund_type = None
        self._fund_user_id = None

    @property
    def allowed_float_up(self):
        return self._allowed_float_up

    @allowed_float_up.setter
    def allowed_float_up(self, value):
        self._allowed_float_up = value
    @property
    def allows_skip_budget_deduction(self):
        return self._allows_skip_budget_deduction

    @allows_skip_budget_deduction.setter
    def allows_skip_budget_deduction(self, value):
        self._allows_skip_budget_deduction = value
    @property
    def ceiling_amount(self):
        return self._ceiling_amount

    @ceiling_amount.setter
    def ceiling_amount(self, value):
        self._ceiling_amount = value
    @property
    def fund_principal(self):
        return self._fund_principal

    @fund_principal.setter
    def fund_principal(self, value):
        self._fund_principal = value
    @property
    def fund_priority(self):
        return self._fund_priority

    @fund_priority.setter
    def fund_priority(self, value):
        self._fund_priority = value
    @property
    def fund_provider(self):
        return self._fund_provider

    @fund_provider.setter
    def fund_provider(self, value):
        self._fund_provider = value
    @property
    def fund_ratio(self):
        return self._fund_ratio

    @fund_ratio.setter
    def fund_ratio(self, value):
        self._fund_ratio = value
    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def fund_user_id(self):
        return self._fund_user_id

    @fund_user_id.setter
    def fund_user_id(self, value):
        self._fund_user_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.allowed_float_up:
            if hasattr(self.allowed_float_up, 'to_alipay_dict'):
                params['allowed_float_up'] = self.allowed_float_up.to_alipay_dict()
            else:
                params['allowed_float_up'] = self.allowed_float_up
        if self.allows_skip_budget_deduction:
            if hasattr(self.allows_skip_budget_deduction, 'to_alipay_dict'):
                params['allows_skip_budget_deduction'] = self.allows_skip_budget_deduction.to_alipay_dict()
            else:
                params['allows_skip_budget_deduction'] = self.allows_skip_budget_deduction
        if self.ceiling_amount:
            if hasattr(self.ceiling_amount, 'to_alipay_dict'):
                params['ceiling_amount'] = self.ceiling_amount.to_alipay_dict()
            else:
                params['ceiling_amount'] = self.ceiling_amount
        if self.fund_principal:
            if hasattr(self.fund_principal, 'to_alipay_dict'):
                params['fund_principal'] = self.fund_principal.to_alipay_dict()
            else:
                params['fund_principal'] = self.fund_principal
        if self.fund_priority:
            if hasattr(self.fund_priority, 'to_alipay_dict'):
                params['fund_priority'] = self.fund_priority.to_alipay_dict()
            else:
                params['fund_priority'] = self.fund_priority
        if self.fund_provider:
            if hasattr(self.fund_provider, 'to_alipay_dict'):
                params['fund_provider'] = self.fund_provider.to_alipay_dict()
            else:
                params['fund_provider'] = self.fund_provider
        if self.fund_ratio:
            if hasattr(self.fund_ratio, 'to_alipay_dict'):
                params['fund_ratio'] = self.fund_ratio.to_alipay_dict()
            else:
                params['fund_ratio'] = self.fund_ratio
        if self.fund_type:
            if hasattr(self.fund_type, 'to_alipay_dict'):
                params['fund_type'] = self.fund_type.to_alipay_dict()
            else:
                params['fund_type'] = self.fund_type
        if self.fund_user_id:
            if hasattr(self.fund_user_id, 'to_alipay_dict'):
                params['fund_user_id'] = self.fund_user_id.to_alipay_dict()
            else:
                params['fund_user_id'] = self.fund_user_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FsFundRelationDetailForm()
        if 'allowed_float_up' in d:
            o.allowed_float_up = d['allowed_float_up']
        if 'allows_skip_budget_deduction' in d:
            o.allows_skip_budget_deduction = d['allows_skip_budget_deduction']
        if 'ceiling_amount' in d:
            o.ceiling_amount = d['ceiling_amount']
        if 'fund_principal' in d:
            o.fund_principal = d['fund_principal']
        if 'fund_priority' in d:
            o.fund_priority = d['fund_priority']
        if 'fund_provider' in d:
            o.fund_provider = d['fund_provider']
        if 'fund_ratio' in d:
            o.fund_ratio = d['fund_ratio']
        if 'fund_type' in d:
            o.fund_type = d['fund_type']
        if 'fund_user_id' in d:
            o.fund_user_id = d['fund_user_id']
        return o


