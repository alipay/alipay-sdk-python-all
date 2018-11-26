#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.BudgetVO import BudgetVO
from alipay.aop.api.domain.LoanTerm import LoanTerm
from alipay.aop.api.domain.RepayPlanTermVO import RepayPlanTermVO


class LoanApplyBudgetVO(object):

    def __init__(self):
        self._apply_amt = None
        self._apply_date = None
        self._apply_receipt_no = None
        self._budget = None
        self._current_term = None
        self._current_term_repay_date = None
        self._loan_term = None
        self._repay_plan_term_list = None

    @property
    def apply_amt(self):
        return self._apply_amt

    @apply_amt.setter
    def apply_amt(self, value):
        self._apply_amt = value
    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_receipt_no(self):
        return self._apply_receipt_no

    @apply_receipt_no.setter
    def apply_receipt_no(self, value):
        self._apply_receipt_no = value
    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if isinstance(value, BudgetVO):
            self._budget = value
        else:
            self._budget = BudgetVO.from_alipay_dict(value)
    @property
    def current_term(self):
        return self._current_term

    @current_term.setter
    def current_term(self, value):
        self._current_term = value
    @property
    def current_term_repay_date(self):
        return self._current_term_repay_date

    @current_term_repay_date.setter
    def current_term_repay_date(self, value):
        self._current_term_repay_date = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        if isinstance(value, LoanTerm):
            self._loan_term = value
        else:
            self._loan_term = LoanTerm.from_alipay_dict(value)
    @property
    def repay_plan_term_list(self):
        return self._repay_plan_term_list

    @repay_plan_term_list.setter
    def repay_plan_term_list(self, value):
        if isinstance(value, list):
            self._repay_plan_term_list = list()
            for i in value:
                if isinstance(i, RepayPlanTermVO):
                    self._repay_plan_term_list.append(i)
                else:
                    self._repay_plan_term_list.append(RepayPlanTermVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.apply_amt:
            if hasattr(self.apply_amt, 'to_alipay_dict'):
                params['apply_amt'] = self.apply_amt.to_alipay_dict()
            else:
                params['apply_amt'] = self.apply_amt
        if self.apply_date:
            if hasattr(self.apply_date, 'to_alipay_dict'):
                params['apply_date'] = self.apply_date.to_alipay_dict()
            else:
                params['apply_date'] = self.apply_date
        if self.apply_receipt_no:
            if hasattr(self.apply_receipt_no, 'to_alipay_dict'):
                params['apply_receipt_no'] = self.apply_receipt_no.to_alipay_dict()
            else:
                params['apply_receipt_no'] = self.apply_receipt_no
        if self.budget:
            if hasattr(self.budget, 'to_alipay_dict'):
                params['budget'] = self.budget.to_alipay_dict()
            else:
                params['budget'] = self.budget
        if self.current_term:
            if hasattr(self.current_term, 'to_alipay_dict'):
                params['current_term'] = self.current_term.to_alipay_dict()
            else:
                params['current_term'] = self.current_term
        if self.current_term_repay_date:
            if hasattr(self.current_term_repay_date, 'to_alipay_dict'):
                params['current_term_repay_date'] = self.current_term_repay_date.to_alipay_dict()
            else:
                params['current_term_repay_date'] = self.current_term_repay_date
        if self.loan_term:
            if hasattr(self.loan_term, 'to_alipay_dict'):
                params['loan_term'] = self.loan_term.to_alipay_dict()
            else:
                params['loan_term'] = self.loan_term
        if self.repay_plan_term_list:
            if isinstance(self.repay_plan_term_list, list):
                for i in range(0, len(self.repay_plan_term_list)):
                    element = self.repay_plan_term_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan_term_list[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan_term_list, 'to_alipay_dict'):
                params['repay_plan_term_list'] = self.repay_plan_term_list.to_alipay_dict()
            else:
                params['repay_plan_term_list'] = self.repay_plan_term_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LoanApplyBudgetVO()
        if 'apply_amt' in d:
            o.apply_amt = d['apply_amt']
        if 'apply_date' in d:
            o.apply_date = d['apply_date']
        if 'apply_receipt_no' in d:
            o.apply_receipt_no = d['apply_receipt_no']
        if 'budget' in d:
            o.budget = d['budget']
        if 'current_term' in d:
            o.current_term = d['current_term']
        if 'current_term_repay_date' in d:
            o.current_term_repay_date = d['current_term_repay_date']
        if 'loan_term' in d:
            o.loan_term = d['loan_term']
        if 'repay_plan_term_list' in d:
            o.repay_plan_term_list = d['repay_plan_term_list']
        return o


