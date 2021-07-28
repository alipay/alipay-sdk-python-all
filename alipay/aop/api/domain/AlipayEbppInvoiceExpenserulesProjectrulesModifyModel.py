#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseCtrRuleGroupInfo import ExpenseCtrRuleGroupInfo


class AlipayEbppInvoiceExpenserulesProjectrulesModifyModel(object):

    def __init__(self):
        self._account_id = None
        self._action = None
        self._agreement_no = None
        self._expense_ctrl_rule_info_group_list = None
        self._project_id = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def expense_ctrl_rule_info_group_list(self):
        return self._expense_ctrl_rule_info_group_list

    @expense_ctrl_rule_info_group_list.setter
    def expense_ctrl_rule_info_group_list(self, value):
        if isinstance(value, list):
            self._expense_ctrl_rule_info_group_list = list()
            for i in value:
                if isinstance(i, ExpenseCtrRuleGroupInfo):
                    self._expense_ctrl_rule_info_group_list.append(i)
                else:
                    self._expense_ctrl_rule_info_group_list.append(ExpenseCtrRuleGroupInfo.from_alipay_dict(i))
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.action:
            if hasattr(self.action, 'to_alipay_dict'):
                params['action'] = self.action.to_alipay_dict()
            else:
                params['action'] = self.action
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.expense_ctrl_rule_info_group_list:
            if isinstance(self.expense_ctrl_rule_info_group_list, list):
                for i in range(0, len(self.expense_ctrl_rule_info_group_list)):
                    element = self.expense_ctrl_rule_info_group_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.expense_ctrl_rule_info_group_list[i] = element.to_alipay_dict()
            if hasattr(self.expense_ctrl_rule_info_group_list, 'to_alipay_dict'):
                params['expense_ctrl_rule_info_group_list'] = self.expense_ctrl_rule_info_group_list.to_alipay_dict()
            else:
                params['expense_ctrl_rule_info_group_list'] = self.expense_ctrl_rule_info_group_list
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpenserulesProjectrulesModifyModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'action' in d:
            o.action = d['action']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'expense_ctrl_rule_info_group_list' in d:
            o.expense_ctrl_rule_info_group_list = d['expense_ctrl_rule_info_group_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        return o


