#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayBossFncAntbudgetGroupbudgetBatchqueryModel(object):

    def __init__(self):
        self._budget_fy = None
        self._department_code = None
        self._group_budget_code = None
        self._operator_work_no = None
        self._page_num = None
        self._page_size = None

    @property
    def budget_fy(self):
        return self._budget_fy

    @budget_fy.setter
    def budget_fy(self, value):
        self._budget_fy = value
    @property
    def department_code(self):
        return self._department_code

    @department_code.setter
    def department_code(self, value):
        self._department_code = value
    @property
    def group_budget_code(self):
        return self._group_budget_code

    @group_budget_code.setter
    def group_budget_code(self, value):
        self._group_budget_code = value
    @property
    def operator_work_no(self):
        return self._operator_work_no

    @operator_work_no.setter
    def operator_work_no(self, value):
        self._operator_work_no = value
    @property
    def page_num(self):
        return self._page_num

    @page_num.setter
    def page_num(self, value):
        self._page_num = value
    @property
    def page_size(self):
        return self._page_size

    @page_size.setter
    def page_size(self, value):
        self._page_size = value


    def to_alipay_dict(self):
        params = dict()
        if self.budget_fy:
            if hasattr(self.budget_fy, 'to_alipay_dict'):
                params['budget_fy'] = self.budget_fy.to_alipay_dict()
            else:
                params['budget_fy'] = self.budget_fy
        if self.department_code:
            if hasattr(self.department_code, 'to_alipay_dict'):
                params['department_code'] = self.department_code.to_alipay_dict()
            else:
                params['department_code'] = self.department_code
        if self.group_budget_code:
            if hasattr(self.group_budget_code, 'to_alipay_dict'):
                params['group_budget_code'] = self.group_budget_code.to_alipay_dict()
            else:
                params['group_budget_code'] = self.group_budget_code
        if self.operator_work_no:
            if hasattr(self.operator_work_no, 'to_alipay_dict'):
                params['operator_work_no'] = self.operator_work_no.to_alipay_dict()
            else:
                params['operator_work_no'] = self.operator_work_no
        if self.page_num:
            if hasattr(self.page_num, 'to_alipay_dict'):
                params['page_num'] = self.page_num.to_alipay_dict()
            else:
                params['page_num'] = self.page_num
        if self.page_size:
            if hasattr(self.page_size, 'to_alipay_dict'):
                params['page_size'] = self.page_size.to_alipay_dict()
            else:
                params['page_size'] = self.page_size
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayBossFncAntbudgetGroupbudgetBatchqueryModel()
        if 'budget_fy' in d:
            o.budget_fy = d['budget_fy']
        if 'department_code' in d:
            o.department_code = d['department_code']
        if 'group_budget_code' in d:
            o.group_budget_code = d['group_budget_code']
        if 'operator_work_no' in d:
            o.operator_work_no = d['operator_work_no']
        if 'page_num' in d:
            o.page_num = d['page_num']
        if 'page_size' in d:
            o.page_size = d['page_size']
        return o


