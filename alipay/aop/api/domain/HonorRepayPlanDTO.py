#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.HonorRepayPlanTermDTO import HonorRepayPlanTermDTO


class HonorRepayPlanDTO(object):

    def __init__(self):
        self._apply_no = None
        self._budget_type = None
        self._current_term = None
        self._duerepay = None
        self._loan_amount = None
        self._non_repayable_desc = None
        self._out_order_no = None
        self._overdue_amount = None
        self._overdue_days = None
        self._paydate = None
        self._repay_plan_terms = None
        self._status = None
        self._support_repay_type = None
        self._total_term = None

    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def budget_type(self):
        return self._budget_type

    @budget_type.setter
    def budget_type(self, value):
        self._budget_type = value
    @property
    def current_term(self):
        return self._current_term

    @current_term.setter
    def current_term(self, value):
        self._current_term = value
    @property
    def duerepay(self):
        return self._duerepay

    @duerepay.setter
    def duerepay(self, value):
        self._duerepay = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def non_repayable_desc(self):
        return self._non_repayable_desc

    @non_repayable_desc.setter
    def non_repayable_desc(self, value):
        self._non_repayable_desc = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def overdue_amount(self):
        return self._overdue_amount

    @overdue_amount.setter
    def overdue_amount(self, value):
        self._overdue_amount = value
    @property
    def overdue_days(self):
        return self._overdue_days

    @overdue_days.setter
    def overdue_days(self, value):
        self._overdue_days = value
    @property
    def paydate(self):
        return self._paydate

    @paydate.setter
    def paydate(self, value):
        self._paydate = value
    @property
    def repay_plan_terms(self):
        return self._repay_plan_terms

    @repay_plan_terms.setter
    def repay_plan_terms(self, value):
        if isinstance(value, list):
            self._repay_plan_terms = list()
            for i in value:
                if isinstance(i, HonorRepayPlanTermDTO):
                    self._repay_plan_terms.append(i)
                else:
                    self._repay_plan_terms.append(HonorRepayPlanTermDTO.from_alipay_dict(i))
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def support_repay_type(self):
        return self._support_repay_type

    @support_repay_type.setter
    def support_repay_type(self, value):
        if isinstance(value, list):
            self._support_repay_type = list()
            for i in value:
                self._support_repay_type.append(i)
    @property
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value


    def to_alipay_dict(self):
        params = dict()
        if self.apply_no:
            if hasattr(self.apply_no, 'to_alipay_dict'):
                params['apply_no'] = self.apply_no.to_alipay_dict()
            else:
                params['apply_no'] = self.apply_no
        if self.budget_type:
            if hasattr(self.budget_type, 'to_alipay_dict'):
                params['budget_type'] = self.budget_type.to_alipay_dict()
            else:
                params['budget_type'] = self.budget_type
        if self.current_term:
            if hasattr(self.current_term, 'to_alipay_dict'):
                params['current_term'] = self.current_term.to_alipay_dict()
            else:
                params['current_term'] = self.current_term
        if self.duerepay:
            if hasattr(self.duerepay, 'to_alipay_dict'):
                params['duerepay'] = self.duerepay.to_alipay_dict()
            else:
                params['duerepay'] = self.duerepay
        if self.loan_amount:
            if hasattr(self.loan_amount, 'to_alipay_dict'):
                params['loan_amount'] = self.loan_amount.to_alipay_dict()
            else:
                params['loan_amount'] = self.loan_amount
        if self.non_repayable_desc:
            if hasattr(self.non_repayable_desc, 'to_alipay_dict'):
                params['non_repayable_desc'] = self.non_repayable_desc.to_alipay_dict()
            else:
                params['non_repayable_desc'] = self.non_repayable_desc
        if self.out_order_no:
            if hasattr(self.out_order_no, 'to_alipay_dict'):
                params['out_order_no'] = self.out_order_no.to_alipay_dict()
            else:
                params['out_order_no'] = self.out_order_no
        if self.overdue_amount:
            if hasattr(self.overdue_amount, 'to_alipay_dict'):
                params['overdue_amount'] = self.overdue_amount.to_alipay_dict()
            else:
                params['overdue_amount'] = self.overdue_amount
        if self.overdue_days:
            if hasattr(self.overdue_days, 'to_alipay_dict'):
                params['overdue_days'] = self.overdue_days.to_alipay_dict()
            else:
                params['overdue_days'] = self.overdue_days
        if self.paydate:
            if hasattr(self.paydate, 'to_alipay_dict'):
                params['paydate'] = self.paydate.to_alipay_dict()
            else:
                params['paydate'] = self.paydate
        if self.repay_plan_terms:
            if isinstance(self.repay_plan_terms, list):
                for i in range(0, len(self.repay_plan_terms)):
                    element = self.repay_plan_terms[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.repay_plan_terms[i] = element.to_alipay_dict()
            if hasattr(self.repay_plan_terms, 'to_alipay_dict'):
                params['repay_plan_terms'] = self.repay_plan_terms.to_alipay_dict()
            else:
                params['repay_plan_terms'] = self.repay_plan_terms
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.support_repay_type:
            if isinstance(self.support_repay_type, list):
                for i in range(0, len(self.support_repay_type)):
                    element = self.support_repay_type[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_repay_type[i] = element.to_alipay_dict()
            if hasattr(self.support_repay_type, 'to_alipay_dict'):
                params['support_repay_type'] = self.support_repay_type.to_alipay_dict()
            else:
                params['support_repay_type'] = self.support_repay_type
        if self.total_term:
            if hasattr(self.total_term, 'to_alipay_dict'):
                params['total_term'] = self.total_term.to_alipay_dict()
            else:
                params['total_term'] = self.total_term
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = HonorRepayPlanDTO()
        if 'apply_no' in d:
            o.apply_no = d['apply_no']
        if 'budget_type' in d:
            o.budget_type = d['budget_type']
        if 'current_term' in d:
            o.current_term = d['current_term']
        if 'duerepay' in d:
            o.duerepay = d['duerepay']
        if 'loan_amount' in d:
            o.loan_amount = d['loan_amount']
        if 'non_repayable_desc' in d:
            o.non_repayable_desc = d['non_repayable_desc']
        if 'out_order_no' in d:
            o.out_order_no = d['out_order_no']
        if 'overdue_amount' in d:
            o.overdue_amount = d['overdue_amount']
        if 'overdue_days' in d:
            o.overdue_days = d['overdue_days']
        if 'paydate' in d:
            o.paydate = d['paydate']
        if 'repay_plan_terms' in d:
            o.repay_plan_terms = d['repay_plan_terms']
        if 'status' in d:
            o.status = d['status']
        if 'support_repay_type' in d:
            o.support_repay_type = d['support_repay_type']
        if 'total_term' in d:
            o.total_term = d['total_term']
        return o


