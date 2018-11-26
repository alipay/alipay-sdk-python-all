#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanApplyBudgetVO import LoanApplyBudgetVO


class AlipayPcreditLoanLoanUnclearQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanLoanUnclearQueryResponse, self).__init__()
        self._loan_apply_budget_list = None
        self._total = None

    @property
    def loan_apply_budget_list(self):
        return self._loan_apply_budget_list

    @loan_apply_budget_list.setter
    def loan_apply_budget_list(self, value):
        if isinstance(value, list):
            self._loan_apply_budget_list = list()
            for i in value:
                if isinstance(i, LoanApplyBudgetVO):
                    self._loan_apply_budget_list.append(i)
                else:
                    self._loan_apply_budget_list.append(LoanApplyBudgetVO.from_alipay_dict(i))
    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanLoanUnclearQueryResponse, self).parse_response_content(response_content)
        if 'loan_apply_budget_list' in response:
            self.loan_apply_budget_list = response['loan_apply_budget_list']
        if 'total' in response:
            self.total = response['total']
