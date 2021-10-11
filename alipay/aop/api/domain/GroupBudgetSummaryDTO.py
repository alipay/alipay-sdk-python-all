#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class GroupBudgetSummaryDTO(object):

    def __init__(self):
        self._benefiting_dept = None
        self._benefiting_dept_name = None
        self._bg_code = None
        self._bu_code = None
        self._budget_account = None
        self._budget_account_name = None
        self._budget_fy = None
        self._group_budget_code = None
        self._making_dept = None
        self._making_dept_name = None
        self._remain_amount = None
        self._remain_amount_currency = None

    @property
    def benefiting_dept(self):
        return self._benefiting_dept

    @benefiting_dept.setter
    def benefiting_dept(self, value):
        self._benefiting_dept = value
    @property
    def benefiting_dept_name(self):
        return self._benefiting_dept_name

    @benefiting_dept_name.setter
    def benefiting_dept_name(self, value):
        self._benefiting_dept_name = value
    @property
    def bg_code(self):
        return self._bg_code

    @bg_code.setter
    def bg_code(self, value):
        self._bg_code = value
    @property
    def bu_code(self):
        return self._bu_code

    @bu_code.setter
    def bu_code(self, value):
        self._bu_code = value
    @property
    def budget_account(self):
        return self._budget_account

    @budget_account.setter
    def budget_account(self, value):
        self._budget_account = value
    @property
    def budget_account_name(self):
        return self._budget_account_name

    @budget_account_name.setter
    def budget_account_name(self, value):
        self._budget_account_name = value
    @property
    def budget_fy(self):
        return self._budget_fy

    @budget_fy.setter
    def budget_fy(self, value):
        self._budget_fy = value
    @property
    def group_budget_code(self):
        return self._group_budget_code

    @group_budget_code.setter
    def group_budget_code(self, value):
        self._group_budget_code = value
    @property
    def making_dept(self):
        return self._making_dept

    @making_dept.setter
    def making_dept(self, value):
        self._making_dept = value
    @property
    def making_dept_name(self):
        return self._making_dept_name

    @making_dept_name.setter
    def making_dept_name(self, value):
        self._making_dept_name = value
    @property
    def remain_amount(self):
        return self._remain_amount

    @remain_amount.setter
    def remain_amount(self, value):
        self._remain_amount = value
    @property
    def remain_amount_currency(self):
        return self._remain_amount_currency

    @remain_amount_currency.setter
    def remain_amount_currency(self, value):
        self._remain_amount_currency = value


    def to_alipay_dict(self):
        params = dict()
        if self.benefiting_dept:
            if hasattr(self.benefiting_dept, 'to_alipay_dict'):
                params['benefiting_dept'] = self.benefiting_dept.to_alipay_dict()
            else:
                params['benefiting_dept'] = self.benefiting_dept
        if self.benefiting_dept_name:
            if hasattr(self.benefiting_dept_name, 'to_alipay_dict'):
                params['benefiting_dept_name'] = self.benefiting_dept_name.to_alipay_dict()
            else:
                params['benefiting_dept_name'] = self.benefiting_dept_name
        if self.bg_code:
            if hasattr(self.bg_code, 'to_alipay_dict'):
                params['bg_code'] = self.bg_code.to_alipay_dict()
            else:
                params['bg_code'] = self.bg_code
        if self.bu_code:
            if hasattr(self.bu_code, 'to_alipay_dict'):
                params['bu_code'] = self.bu_code.to_alipay_dict()
            else:
                params['bu_code'] = self.bu_code
        if self.budget_account:
            if hasattr(self.budget_account, 'to_alipay_dict'):
                params['budget_account'] = self.budget_account.to_alipay_dict()
            else:
                params['budget_account'] = self.budget_account
        if self.budget_account_name:
            if hasattr(self.budget_account_name, 'to_alipay_dict'):
                params['budget_account_name'] = self.budget_account_name.to_alipay_dict()
            else:
                params['budget_account_name'] = self.budget_account_name
        if self.budget_fy:
            if hasattr(self.budget_fy, 'to_alipay_dict'):
                params['budget_fy'] = self.budget_fy.to_alipay_dict()
            else:
                params['budget_fy'] = self.budget_fy
        if self.group_budget_code:
            if hasattr(self.group_budget_code, 'to_alipay_dict'):
                params['group_budget_code'] = self.group_budget_code.to_alipay_dict()
            else:
                params['group_budget_code'] = self.group_budget_code
        if self.making_dept:
            if hasattr(self.making_dept, 'to_alipay_dict'):
                params['making_dept'] = self.making_dept.to_alipay_dict()
            else:
                params['making_dept'] = self.making_dept
        if self.making_dept_name:
            if hasattr(self.making_dept_name, 'to_alipay_dict'):
                params['making_dept_name'] = self.making_dept_name.to_alipay_dict()
            else:
                params['making_dept_name'] = self.making_dept_name
        if self.remain_amount:
            if hasattr(self.remain_amount, 'to_alipay_dict'):
                params['remain_amount'] = self.remain_amount.to_alipay_dict()
            else:
                params['remain_amount'] = self.remain_amount
        if self.remain_amount_currency:
            if hasattr(self.remain_amount_currency, 'to_alipay_dict'):
                params['remain_amount_currency'] = self.remain_amount_currency.to_alipay_dict()
            else:
                params['remain_amount_currency'] = self.remain_amount_currency
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = GroupBudgetSummaryDTO()
        if 'benefiting_dept' in d:
            o.benefiting_dept = d['benefiting_dept']
        if 'benefiting_dept_name' in d:
            o.benefiting_dept_name = d['benefiting_dept_name']
        if 'bg_code' in d:
            o.bg_code = d['bg_code']
        if 'bu_code' in d:
            o.bu_code = d['bu_code']
        if 'budget_account' in d:
            o.budget_account = d['budget_account']
        if 'budget_account_name' in d:
            o.budget_account_name = d['budget_account_name']
        if 'budget_fy' in d:
            o.budget_fy = d['budget_fy']
        if 'group_budget_code' in d:
            o.group_budget_code = d['group_budget_code']
        if 'making_dept' in d:
            o.making_dept = d['making_dept']
        if 'making_dept_name' in d:
            o.making_dept_name = d['making_dept_name']
        if 'remain_amount' in d:
            o.remain_amount = d['remain_amount']
        if 'remain_amount_currency' in d:
            o.remain_amount_currency = d['remain_amount_currency']
        return o


