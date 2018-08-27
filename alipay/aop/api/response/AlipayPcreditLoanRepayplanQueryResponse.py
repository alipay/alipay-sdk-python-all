#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanMoneyTypeAmt import LoanMoneyTypeAmt
from alipay.aop.api.domain.LoanRepayPlanTerm import LoanRepayPlanTerm


class AlipayPcreditLoanRepayplanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanRepayplanQueryResponse, self).__init__()
        self._ar_no = None
        self._current_term = None
        self._due_date = None
        self._loan_apply_no = None
        self._loan_date = None
        self._ovd_date = None
        self._remain_repay_amt = None
        self._repay_mode = None
        self._repay_plan_term_list = None
        self._settle_date = None
        self._status = None
        self._term_unit = None
        self._terms = None

    @property
    def ar_no(self):
        return self._ar_no

    @ar_no.setter
    def ar_no(self, value):
        self._ar_no = value
    @property
    def current_term(self):
        return self._current_term

    @current_term.setter
    def current_term(self, value):
        self._current_term = value
    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        self._due_date = value
    @property
    def loan_apply_no(self):
        return self._loan_apply_no

    @loan_apply_no.setter
    def loan_apply_no(self, value):
        self._loan_apply_no = value
    @property
    def loan_date(self):
        return self._loan_date

    @loan_date.setter
    def loan_date(self, value):
        self._loan_date = value
    @property
    def ovd_date(self):
        return self._ovd_date

    @ovd_date.setter
    def ovd_date(self, value):
        self._ovd_date = value
    @property
    def remain_repay_amt(self):
        return self._remain_repay_amt

    @remain_repay_amt.setter
    def remain_repay_amt(self, value):
        if isinstance(value, LoanMoneyTypeAmt):
            self._remain_repay_amt = value
        else:
            self._remain_repay_amt = LoanMoneyTypeAmt.from_alipay_dict(value)
    @property
    def repay_mode(self):
        return self._repay_mode

    @repay_mode.setter
    def repay_mode(self, value):
        self._repay_mode = value
    @property
    def repay_plan_term_list(self):
        return self._repay_plan_term_list

    @repay_plan_term_list.setter
    def repay_plan_term_list(self, value):
        if isinstance(value, list):
            self._repay_plan_term_list = list()
            for i in value:
                if isinstance(i, LoanRepayPlanTerm):
                    self._repay_plan_term_list.append(i)
                else:
                    self._repay_plan_term_list.append(LoanRepayPlanTerm.from_alipay_dict(i))
    @property
    def settle_date(self):
        return self._settle_date

    @settle_date.setter
    def settle_date(self, value):
        self._settle_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def term_unit(self):
        return self._term_unit

    @term_unit.setter
    def term_unit(self, value):
        self._term_unit = value
    @property
    def terms(self):
        return self._terms

    @terms.setter
    def terms(self, value):
        self._terms = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanRepayplanQueryResponse, self).parse_response_content(response_content)
        if 'ar_no' in response:
            self.ar_no = response['ar_no']
        if 'current_term' in response:
            self.current_term = response['current_term']
        if 'due_date' in response:
            self.due_date = response['due_date']
        if 'loan_apply_no' in response:
            self.loan_apply_no = response['loan_apply_no']
        if 'loan_date' in response:
            self.loan_date = response['loan_date']
        if 'ovd_date' in response:
            self.ovd_date = response['ovd_date']
        if 'remain_repay_amt' in response:
            self.remain_repay_amt = response['remain_repay_amt']
        if 'repay_mode' in response:
            self.repay_mode = response['repay_mode']
        if 'repay_plan_term_list' in response:
            self.repay_plan_term_list = response['repay_plan_term_list']
        if 'settle_date' in response:
            self.settle_date = response['settle_date']
        if 'status' in response:
            self.status = response['status']
        if 'term_unit' in response:
            self.term_unit = response['term_unit']
        if 'terms' in response:
            self.terms = response['terms']
