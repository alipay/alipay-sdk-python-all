#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseCtrRuleInfo import ExpenseCtrRuleInfo


class AlipayEbppInvoiceExpenserulesSceneruleCreateModel(object):

    def __init__(self):
        self._account_id = None
        self._agreement_no = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._employee_list = None
        self._expense_ctrl_rule_info_list = None
        self._expense_type = None
        self._payment_policy = None
        self._scene_type = None
        self._standard_desc = None
        self._standard_name = None

    @property
    def account_id(self):
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        self._account_id = value
    @property
    def agreement_no(self):
        return self._agreement_no

    @agreement_no.setter
    def agreement_no(self, value):
        self._agreement_no = value
    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def employee_list(self):
        return self._employee_list

    @employee_list.setter
    def employee_list(self, value):
        if isinstance(value, list):
            self._employee_list = list()
            for i in value:
                self._employee_list.append(i)
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
    def payment_policy(self):
        return self._payment_policy

    @payment_policy.setter
    def payment_policy(self, value):
        self._payment_policy = value
    @property
    def scene_type(self):
        return self._scene_type

    @scene_type.setter
    def scene_type(self, value):
        self._scene_type = value
    @property
    def standard_desc(self):
        return self._standard_desc

    @standard_desc.setter
    def standard_desc(self, value):
        self._standard_desc = value
    @property
    def standard_name(self):
        return self._standard_name

    @standard_name.setter
    def standard_name(self, value):
        self._standard_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.account_id:
            if hasattr(self.account_id, 'to_alipay_dict'):
                params['account_id'] = self.account_id.to_alipay_dict()
            else:
                params['account_id'] = self.account_id
        if self.agreement_no:
            if hasattr(self.agreement_no, 'to_alipay_dict'):
                params['agreement_no'] = self.agreement_no.to_alipay_dict()
            else:
                params['agreement_no'] = self.agreement_no
        if self.effective_end_date:
            if hasattr(self.effective_end_date, 'to_alipay_dict'):
                params['effective_end_date'] = self.effective_end_date.to_alipay_dict()
            else:
                params['effective_end_date'] = self.effective_end_date
        if self.effective_start_date:
            if hasattr(self.effective_start_date, 'to_alipay_dict'):
                params['effective_start_date'] = self.effective_start_date.to_alipay_dict()
            else:
                params['effective_start_date'] = self.effective_start_date
        if self.employee_list:
            if isinstance(self.employee_list, list):
                for i in range(0, len(self.employee_list)):
                    element = self.employee_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.employee_list[i] = element.to_alipay_dict()
            if hasattr(self.employee_list, 'to_alipay_dict'):
                params['employee_list'] = self.employee_list.to_alipay_dict()
            else:
                params['employee_list'] = self.employee_list
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
        if self.payment_policy:
            if hasattr(self.payment_policy, 'to_alipay_dict'):
                params['payment_policy'] = self.payment_policy.to_alipay_dict()
            else:
                params['payment_policy'] = self.payment_policy
        if self.scene_type:
            if hasattr(self.scene_type, 'to_alipay_dict'):
                params['scene_type'] = self.scene_type.to_alipay_dict()
            else:
                params['scene_type'] = self.scene_type
        if self.standard_desc:
            if hasattr(self.standard_desc, 'to_alipay_dict'):
                params['standard_desc'] = self.standard_desc.to_alipay_dict()
            else:
                params['standard_desc'] = self.standard_desc
        if self.standard_name:
            if hasattr(self.standard_name, 'to_alipay_dict'):
                params['standard_name'] = self.standard_name.to_alipay_dict()
            else:
                params['standard_name'] = self.standard_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEbppInvoiceExpenserulesSceneruleCreateModel()
        if 'account_id' in d:
            o.account_id = d['account_id']
        if 'agreement_no' in d:
            o.agreement_no = d['agreement_no']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'employee_list' in d:
            o.employee_list = d['employee_list']
        if 'expense_ctrl_rule_info_list' in d:
            o.expense_ctrl_rule_info_list = d['expense_ctrl_rule_info_list']
        if 'expense_type' in d:
            o.expense_type = d['expense_type']
        if 'payment_policy' in d:
            o.payment_policy = d['payment_policy']
        if 'scene_type' in d:
            o.scene_type = d['scene_type']
        if 'standard_desc' in d:
            o.standard_desc = d['standard_desc']
        if 'standard_name' in d:
            o.standard_name = d['standard_name']
        return o


