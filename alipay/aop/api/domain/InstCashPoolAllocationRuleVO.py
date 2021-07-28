#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.InstAccountDTO import InstAccountDTO
from alipay.aop.api.domain.InstRuleCustomMemoVO import InstRuleCustomMemoVO
from alipay.aop.api.domain.InstAccountDTO import InstAccountDTO


class InstCashPoolAllocationRuleVO(object):

    def __init__(self):
        self._inst_account = None
        self._inst_rule_custom_memo = None
        self._limit_water_line = None
        self._memo = None
        self._need_custom_memo = None
        self._operator = None
        self._parent_inst_account = None
        self._rule_name = None
        self._rule_order = None
        self._rule_status = None
        self._rule_type = None
        self._target_water_line = None

    @property
    def inst_account(self):
        return self._inst_account

    @inst_account.setter
    def inst_account(self, value):
        if isinstance(value, InstAccountDTO):
            self._inst_account = value
        else:
            self._inst_account = InstAccountDTO.from_alipay_dict(value)
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
    def limit_water_line(self):
        return self._limit_water_line

    @limit_water_line.setter
    def limit_water_line(self, value):
        self._limit_water_line = value
    @property
    def memo(self):
        return self._memo

    @memo.setter
    def memo(self, value):
        self._memo = value
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
    def parent_inst_account(self):
        return self._parent_inst_account

    @parent_inst_account.setter
    def parent_inst_account(self, value):
        if isinstance(value, InstAccountDTO):
            self._parent_inst_account = value
        else:
            self._parent_inst_account = InstAccountDTO.from_alipay_dict(value)
    @property
    def rule_name(self):
        return self._rule_name

    @rule_name.setter
    def rule_name(self, value):
        self._rule_name = value
    @property
    def rule_order(self):
        return self._rule_order

    @rule_order.setter
    def rule_order(self, value):
        self._rule_order = value
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
    def target_water_line(self):
        return self._target_water_line

    @target_water_line.setter
    def target_water_line(self, value):
        self._target_water_line = value


    def to_alipay_dict(self):
        params = dict()
        if self.inst_account:
            if hasattr(self.inst_account, 'to_alipay_dict'):
                params['inst_account'] = self.inst_account.to_alipay_dict()
            else:
                params['inst_account'] = self.inst_account
        if self.inst_rule_custom_memo:
            if hasattr(self.inst_rule_custom_memo, 'to_alipay_dict'):
                params['inst_rule_custom_memo'] = self.inst_rule_custom_memo.to_alipay_dict()
            else:
                params['inst_rule_custom_memo'] = self.inst_rule_custom_memo
        if self.limit_water_line:
            if hasattr(self.limit_water_line, 'to_alipay_dict'):
                params['limit_water_line'] = self.limit_water_line.to_alipay_dict()
            else:
                params['limit_water_line'] = self.limit_water_line
        if self.memo:
            if hasattr(self.memo, 'to_alipay_dict'):
                params['memo'] = self.memo.to_alipay_dict()
            else:
                params['memo'] = self.memo
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
        if self.parent_inst_account:
            if hasattr(self.parent_inst_account, 'to_alipay_dict'):
                params['parent_inst_account'] = self.parent_inst_account.to_alipay_dict()
            else:
                params['parent_inst_account'] = self.parent_inst_account
        if self.rule_name:
            if hasattr(self.rule_name, 'to_alipay_dict'):
                params['rule_name'] = self.rule_name.to_alipay_dict()
            else:
                params['rule_name'] = self.rule_name
        if self.rule_order:
            if hasattr(self.rule_order, 'to_alipay_dict'):
                params['rule_order'] = self.rule_order.to_alipay_dict()
            else:
                params['rule_order'] = self.rule_order
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
        if self.target_water_line:
            if hasattr(self.target_water_line, 'to_alipay_dict'):
                params['target_water_line'] = self.target_water_line.to_alipay_dict()
            else:
                params['target_water_line'] = self.target_water_line
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstCashPoolAllocationRuleVO()
        if 'inst_account' in d:
            o.inst_account = d['inst_account']
        if 'inst_rule_custom_memo' in d:
            o.inst_rule_custom_memo = d['inst_rule_custom_memo']
        if 'limit_water_line' in d:
            o.limit_water_line = d['limit_water_line']
        if 'memo' in d:
            o.memo = d['memo']
        if 'need_custom_memo' in d:
            o.need_custom_memo = d['need_custom_memo']
        if 'operator' in d:
            o.operator = d['operator']
        if 'parent_inst_account' in d:
            o.parent_inst_account = d['parent_inst_account']
        if 'rule_name' in d:
            o.rule_name = d['rule_name']
        if 'rule_order' in d:
            o.rule_order = d['rule_order']
        if 'rule_status' in d:
            o.rule_status = d['rule_status']
        if 'rule_type' in d:
            o.rule_type = d['rule_type']
        if 'target_water_line' in d:
            o.target_water_line = d['target_water_line']
        return o


