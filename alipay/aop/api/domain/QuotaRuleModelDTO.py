#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FundRuleModelDTO import FundRuleModelDTO
from alipay.aop.api.domain.QuotaLimitModelDTO import QuotaLimitModelDTO


class QuotaRuleModelDTO(object):

    def __init__(self):
        self._available_amount = None
        self._excepted_amount = None
        self._fund_rule_list = None
        self._quota_limit_list = None
        self._validity_period = None

    @property
    def available_amount(self):
        return self._available_amount

    @available_amount.setter
    def available_amount(self, value):
        self._available_amount = value
    @property
    def excepted_amount(self):
        return self._excepted_amount

    @excepted_amount.setter
    def excepted_amount(self, value):
        self._excepted_amount = value
    @property
    def fund_rule_list(self):
        return self._fund_rule_list

    @fund_rule_list.setter
    def fund_rule_list(self, value):
        if isinstance(value, list):
            self._fund_rule_list = list()
            for i in value:
                if isinstance(i, FundRuleModelDTO):
                    self._fund_rule_list.append(i)
                else:
                    self._fund_rule_list.append(FundRuleModelDTO.from_alipay_dict(i))
    @property
    def quota_limit_list(self):
        return self._quota_limit_list

    @quota_limit_list.setter
    def quota_limit_list(self, value):
        if isinstance(value, list):
            self._quota_limit_list = list()
            for i in value:
                if isinstance(i, QuotaLimitModelDTO):
                    self._quota_limit_list.append(i)
                else:
                    self._quota_limit_list.append(QuotaLimitModelDTO.from_alipay_dict(i))
    @property
    def validity_period(self):
        return self._validity_period

    @validity_period.setter
    def validity_period(self, value):
        self._validity_period = value


    def to_alipay_dict(self):
        params = dict()
        if self.available_amount:
            if hasattr(self.available_amount, 'to_alipay_dict'):
                params['available_amount'] = self.available_amount.to_alipay_dict()
            else:
                params['available_amount'] = self.available_amount
        if self.excepted_amount:
            if hasattr(self.excepted_amount, 'to_alipay_dict'):
                params['excepted_amount'] = self.excepted_amount.to_alipay_dict()
            else:
                params['excepted_amount'] = self.excepted_amount
        if self.fund_rule_list:
            if isinstance(self.fund_rule_list, list):
                for i in range(0, len(self.fund_rule_list)):
                    element = self.fund_rule_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.fund_rule_list[i] = element.to_alipay_dict()
            if hasattr(self.fund_rule_list, 'to_alipay_dict'):
                params['fund_rule_list'] = self.fund_rule_list.to_alipay_dict()
            else:
                params['fund_rule_list'] = self.fund_rule_list
        if self.quota_limit_list:
            if isinstance(self.quota_limit_list, list):
                for i in range(0, len(self.quota_limit_list)):
                    element = self.quota_limit_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.quota_limit_list[i] = element.to_alipay_dict()
            if hasattr(self.quota_limit_list, 'to_alipay_dict'):
                params['quota_limit_list'] = self.quota_limit_list.to_alipay_dict()
            else:
                params['quota_limit_list'] = self.quota_limit_list
        if self.validity_period:
            if hasattr(self.validity_period, 'to_alipay_dict'):
                params['validity_period'] = self.validity_period.to_alipay_dict()
            else:
                params['validity_period'] = self.validity_period
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = QuotaRuleModelDTO()
        if 'available_amount' in d:
            o.available_amount = d['available_amount']
        if 'excepted_amount' in d:
            o.excepted_amount = d['excepted_amount']
        if 'fund_rule_list' in d:
            o.fund_rule_list = d['fund_rule_list']
        if 'quota_limit_list' in d:
            o.quota_limit_list = d['quota_limit_list']
        if 'validity_period' in d:
            o.validity_period = d['validity_period']
        return o


