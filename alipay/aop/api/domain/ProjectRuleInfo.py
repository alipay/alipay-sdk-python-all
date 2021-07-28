#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ExpenseCtrRuleGroupInfo import ExpenseCtrRuleGroupInfo


class ProjectRuleInfo(object):

    def __init__(self):
        self._effective_end_date = None
        self._effective_start_date = None
        self._employee_list = None
        self._expense_ctrl_rule_info_group_list = None
        self._project_id = None
        self._project_name = None

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
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value


    def to_alipay_dict(self):
        params = dict()
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
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ProjectRuleInfo()
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'employee_list' in d:
            o.employee_list = d['employee_list']
        if 'expense_ctrl_rule_info_group_list' in d:
            o.expense_ctrl_rule_info_group_list = d['expense_ctrl_rule_info_group_list']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        return o


