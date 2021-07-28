#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstCashPoolAllocationRuleVO import InstCashPoolAllocationRuleVO


class AlipayAccountCashpoolAllocateruleCreateModel(object):

    def __init__(self):
        self._allocation_rule = None
        self._cash_pool_id = None
        self._operator = None
        self._rule_group_id = None

    @property
    def allocation_rule(self):
        return self._allocation_rule

    @allocation_rule.setter
    def allocation_rule(self, value):
        if isinstance(value, InstCashPoolAllocationRuleVO):
            self._allocation_rule = value
        else:
            self._allocation_rule = InstCashPoolAllocationRuleVO.from_alipay_dict(value)
    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def rule_group_id(self):
        return self._rule_group_id

    @rule_group_id.setter
    def rule_group_id(self, value):
        self._rule_group_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.allocation_rule:
            if hasattr(self.allocation_rule, 'to_alipay_dict'):
                params['allocation_rule'] = self.allocation_rule.to_alipay_dict()
            else:
                params['allocation_rule'] = self.allocation_rule
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.rule_group_id:
            if hasattr(self.rule_group_id, 'to_alipay_dict'):
                params['rule_group_id'] = self.rule_group_id.to_alipay_dict()
            else:
                params['rule_group_id'] = self.rule_group_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolAllocateruleCreateModel()
        if 'allocation_rule' in d:
            o.allocation_rule = d['allocation_rule']
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'operator' in d:
            o.operator = d['operator']
        if 'rule_group_id' in d:
            o.rule_group_id = d['rule_group_id']
        return o


