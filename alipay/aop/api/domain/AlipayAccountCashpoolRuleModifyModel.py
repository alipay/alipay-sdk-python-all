#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstRuleCustomMemoVO import InstRuleCustomMemoVO


class AlipayAccountCashpoolRuleModifyModel(object):

    def __init__(self):
        self._cash_pool_id = None
        self._inst_rule_custom_memo = None
        self._limit_walter_line = None
        self._need_custom_memo = None
        self._operator = None
        self._rule_id = None
        self._rule_status = None
        self._rule_type = None
        self._target_walter_line = None

    @property
    def cash_pool_id(self):
        return self._cash_pool_id

    @cash_pool_id.setter
    def cash_pool_id(self, value):
        self._cash_pool_id = value
    @property
    def inst_rule_custom_memo(self):
        return self._inst_rule_custom_memo

    @inst_rule_custom_memo.setter
    def inst_rule_custom_memo(self, value):
        if isinstance(value, InstRuleCustomMemoVO):
            self._inst_rule_custom_memo = value
        else:
            self._inst_rule_custom_memo = InstRuleCustomMemoVO.from_alipay_dict(value)
    @property
    def limit_walter_line(self):
        return self._limit_walter_line

    @limit_walter_line.setter
    def limit_walter_line(self, value):
        self._limit_walter_line = value
    @property
    def need_custom_memo(self):
        return self._need_custom_memo

    @need_custom_memo.setter
    def need_custom_memo(self, value):
        self._need_custom_memo = value
    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        self._operator = value
    @property
    def rule_id(self):
        return self._rule_id

    @rule_id.setter
    def rule_id(self, value):
        self._rule_id = value
    @property
    def rule_status(self):
        return self._rule_status

    @rule_status.setter
    def rule_status(self, value):
        self._rule_status = value
    @property
    def rule_type(self):
        return self._rule_type

    @rule_type.setter
    def rule_type(self, value):
        self._rule_type = value
    @property
    def target_walter_line(self):
        return self._target_walter_line

    @target_walter_line.setter
    def target_walter_line(self, value):
        self._target_walter_line = value


    def to_alipay_dict(self):
        params = dict()
        if self.cash_pool_id:
            if hasattr(self.cash_pool_id, 'to_alipay_dict'):
                params['cash_pool_id'] = self.cash_pool_id.to_alipay_dict()
            else:
                params['cash_pool_id'] = self.cash_pool_id
        if self.inst_rule_custom_memo:
            if hasattr(self.inst_rule_custom_memo, 'to_alipay_dict'):
                params['inst_rule_custom_memo'] = self.inst_rule_custom_memo.to_alipay_dict()
            else:
                params['inst_rule_custom_memo'] = self.inst_rule_custom_memo
        if self.limit_walter_line:
            if hasattr(self.limit_walter_line, 'to_alipay_dict'):
                params['limit_walter_line'] = self.limit_walter_line.to_alipay_dict()
            else:
                params['limit_walter_line'] = self.limit_walter_line
        if self.need_custom_memo:
            if hasattr(self.need_custom_memo, 'to_alipay_dict'):
                params['need_custom_memo'] = self.need_custom_memo.to_alipay_dict()
            else:
                params['need_custom_memo'] = self.need_custom_memo
        if self.operator:
            if hasattr(self.operator, 'to_alipay_dict'):
                params['operator'] = self.operator.to_alipay_dict()
            else:
                params['operator'] = self.operator
        if self.rule_id:
            if hasattr(self.rule_id, 'to_alipay_dict'):
                params['rule_id'] = self.rule_id.to_alipay_dict()
            else:
                params['rule_id'] = self.rule_id
        if self.rule_status:
            if hasattr(self.rule_status, 'to_alipay_dict'):
                params['rule_status'] = self.rule_status.to_alipay_dict()
            else:
                params['rule_status'] = self.rule_status
        if self.rule_type:
            if hasattr(self.rule_type, 'to_alipay_dict'):
                params['rule_type'] = self.rule_type.to_alipay_dict()
            else:
                params['rule_type'] = self.rule_type
        if self.target_walter_line:
            if hasattr(self.target_walter_line, 'to_alipay_dict'):
                params['target_walter_line'] = self.target_walter_line.to_alipay_dict()
            else:
                params['target_walter_line'] = self.target_walter_line
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayAccountCashpoolRuleModifyModel()
        if 'cash_pool_id' in d:
            o.cash_pool_id = d['cash_pool_id']
        if 'inst_rule_custom_memo' in d:
            o.inst_rule_custom_memo = d['inst_rule_custom_memo']
        if 'limit_walter_line' in d:
            o.limit_walter_line = d['limit_walter_line']
        if 'need_custom_memo' in d:
            o.need_custom_memo = d['need_custom_memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'rule_id' in d:
            o.rule_id = d['rule_id']
        if 'rule_status' in d:
            o.rule_status = d['rule_status']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'target_walter_line' in d:
            o.target_walter_line = d['target_walter_line']
        return o


