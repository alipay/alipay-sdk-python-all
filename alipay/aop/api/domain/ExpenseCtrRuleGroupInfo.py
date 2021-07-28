#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseCtrRuleInfo import ExpenseCtrRuleInfo


class ExpenseCtrRuleGroupInfo(object):

    def __init__(self):
        self._expense_ctrl_rule_info_list = None
        self._expense_type = None
        self._group_id = None
        self._group_name = None

    @property
    def expense_ctrl_rule_info_list(self):
        return self._expense_ctrl_rule_info_list

    @expense_ctrl_rule_info_list.setter
    def expense_ctrl_rule_info_list(self, value):
        if isinstance(value, list):
            self._expense_ctrl_rule_info_list = list()
            for i in value:
                if isinstance(i, ExpenseCtrRuleInfo):
                    self._expense_ctrl_rule_info_list.append(i)
                else:
                    self._expense_ctrl_rule_info_list.append(ExpenseCtrRuleInfo.from_alipay_dict(i))
    @property
    def expense_type(self):
        return self._expense_type

    @expense_type.setter
    def expense_type(self, value):
        self._expense_type = value
    @property
    def group_id(self):
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        self._group_id = value
    @property
    def group_name(self):
        return self._group_name

    @group_name.setter
    def group_name(self, value):
        self._group_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.expense_ctrl_rule_info_list:
            if isinstance(self.expense_ctrl_rule_info_list, list):
                for i in range(0, len(self.expense_ctrl_rule_info_list)):
                    element = self.expense_ctrl_rule_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expense_ctrl_rule_info_list[i] = element.to_alipay_dict()
            if hasattr(self.expense_ctrl_rule_info_list, 'to_alipay_dict'):
                params['expense_ctrl_rule_info_list'] = self.expense_ctrl_rule_info_list.to_alipay_dict()
            else:
                params['expense_ctrl_rule_info_list'] = self.expense_ctrl_rule_info_list
        if self.expense_type:
            if hasattr(self.expense_type, 'to_alipay_dict'):
                params['expense_type'] = self.expense_type.to_alipay_dict()
            else:
                params['expense_type'] = self.expense_type
        if self.group_id:
            if hasattr(self.group_id, 'to_alipay_dict'):
                params['group_id'] = self.group_id.to_alipay_dict()
            else:
                params['group_id'] = self.group_id
        if self.group_name:
            if hasattr(self.group_name, 'to_alipay_dict'):
                params['group_name'] = self.group_name.to_alipay_dict()
            else:
                params['group_name'] = self.group_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ExpenseCtrRuleGroupInfo()
        if 'expense_ctrl_rule_info_list' in d:
            o.expense_ctrl_rule_info_list = d['expense_ctrl_rule_info_list']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'group_id' in d:
            o.group_id = d['group_id']
        if 'group_name' in d:
            o.group_name = d['group_name']
        return o


