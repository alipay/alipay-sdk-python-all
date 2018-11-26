#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PreRepayPlanTermVO import PreRepayPlanTermVO


class AlipayPcreditLoanBudgetQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanBudgetQueryResponse, self).__init__()
        self._pre_repay_plan_term_list = None
        self._repay_amt_total = None
        self._repay_int_amt_total = None
        self._repay_prin_amt_total = None

    @property
    def pre_repay_plan_term_list(self):
        return self._pre_repay_plan_term_list

    @pre_repay_plan_term_list.setter
    def pre_repay_plan_term_list(self, value):
        if isinstance(value, list):
            self._pre_repay_plan_term_list = list()
            for i in value:
                if isinstance(i, PreRepayPlanTermVO):
                    self._pre_repay_plan_term_list.append(i)
                else:
                    self._pre_repay_plan_term_list.append(PreRepayPlanTermVO.from_alipay_dict(i))
    @property
    def repay_amt_total(self):
        return self._repay_amt_total

    @repay_amt_total.setter
    def repay_amt_total(self, value):
        self._repay_amt_total = value
    @property
    def repay_int_amt_total(self):
        return self._repay_int_amt_total

    @repay_int_amt_total.setter
    def repay_int_amt_total(self, value):
        self._repay_int_amt_total = value
    @property
    def repay_prin_amt_total(self):
        return self._repay_prin_amt_total

    @repay_prin_amt_total.setter
    def repay_prin_amt_total(self, value):
        self._repay_prin_amt_total = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanBudgetQueryResponse, self).parse_response_content(response_content)
        if 'pre_repay_plan_term_list' in response:
            self.pre_repay_plan_term_list = response['pre_repay_plan_term_list']
        if 'repay_amt_total' in response:
            self.repay_amt_total = response['repay_amt_total']
        if 'repay_int_amt_total' in response:
            self.repay_int_amt_total = response['repay_int_amt_total']
        if 'repay_prin_amt_total' in response:
            self.repay_prin_amt_total = response['repay_prin_amt_total']
