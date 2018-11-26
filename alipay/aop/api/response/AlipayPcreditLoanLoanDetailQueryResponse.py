#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.LoanTerm import LoanTerm
from alipay.aop.api.domain.RepayPlanTermVO import RepayPlanTermVO


class AlipayPcreditLoanLoanDetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanLoanDetailQueryResponse, self).__init__()
        self._apply_amt = None
        self._apply_date = None
        self._clear_date = None
        self._contract_type_list = None
        self._ext_variable = None
        self._loan_term = None
        self._ovd_day_num = None
        self._paid_int = None
        self._paid_ovd_int_penalty = None
        self._paid_ovd_prin_penalty = None
        self._paid_prin = None
        self._remain_repay_amt = None
        self._remain_repay_int_amt = None
        self._remain_repay_prin_amt = None
        self._repay_mode = None
        self._repay_plan_term_list = None
        self._start_date = None
        self._status = None

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
    def clear_date(self):
        return self._clear_date

    @clear_date.setter
    def clear_date(self, value):
        self._clear_date = value
    @property
    def contract_type_list(self):
        return self._contract_type_list

    @contract_type_list.setter
    def contract_type_list(self, value):
        if isinstance(value, list):
            self._contract_type_list = list()
            for i in value:
                self._contract_type_list.append(i)
    @property
    def ext_variable(self):
        return self._ext_variable

    @ext_variable.setter
    def ext_variable(self, value):
        self._ext_variable = value
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
    def ovd_day_num(self):
        return self._ovd_day_num

    @ovd_day_num.setter
    def ovd_day_num(self, value):
        self._ovd_day_num = value
    @property
    def paid_int(self):
        return self._paid_int

    @paid_int.setter
    def paid_int(self, value):
        self._paid_int = value
    @property
    def paid_ovd_int_penalty(self):
        return self._paid_ovd_int_penalty

    @paid_ovd_int_penalty.setter
    def paid_ovd_int_penalty(self, value):
        self._paid_ovd_int_penalty = value
    @property
    def paid_ovd_prin_penalty(self):
        return self._paid_ovd_prin_penalty

    @paid_ovd_prin_penalty.setter
    def paid_ovd_prin_penalty(self, value):
        self._paid_ovd_prin_penalty = value
    @property
    def paid_prin(self):
        return self._paid_prin

    @paid_prin.setter
    def paid_prin(self, value):
        self._paid_prin = value
    @property
    def remain_repay_amt(self):
        return self._remain_repay_amt

    @remain_repay_amt.setter
    def remain_repay_amt(self, value):
        self._remain_repay_amt = value
    @property
    def remain_repay_int_amt(self):
        return self._remain_repay_int_amt

    @remain_repay_int_amt.setter
    def remain_repay_int_amt(self, value):
        self._remain_repay_int_amt = value
    @property
    def remain_repay_prin_amt(self):
        return self._remain_repay_prin_amt

    @remain_repay_prin_amt.setter
    def remain_repay_prin_amt(self, value):
        self._remain_repay_prin_amt = value
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
                if isinstance(i, RepayPlanTermVO):
                    self._repay_plan_term_list.append(i)
                else:
                    self._repay_plan_term_list.append(RepayPlanTermVO.from_alipay_dict(i))
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanLoanDetailQueryResponse, self).parse_response_content(response_content)
        if 'apply_amt' in response:
            self.apply_amt = response['apply_amt']
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'clear_date' in response:
            self.clear_date = response['clear_date']
        if 'contract_type_list' in response:
            self.contract_type_list = response['contract_type_list']
        if 'ext_variable' in response:
            self.ext_variable = response['ext_variable']
        if 'loan_term' in response:
            self.loan_term = response['loan_term']
        if 'ovd_day_num' in response:
            self.ovd_day_num = response['ovd_day_num']
        if 'paid_int' in response:
            self.paid_int = response['paid_int']
        if 'paid_ovd_int_penalty' in response:
            self.paid_ovd_int_penalty = response['paid_ovd_int_penalty']
        if 'paid_ovd_prin_penalty' in response:
            self.paid_ovd_prin_penalty = response['paid_ovd_prin_penalty']
        if 'paid_prin' in response:
            self.paid_prin = response['paid_prin']
        if 'remain_repay_amt' in response:
            self.remain_repay_amt = response['remain_repay_amt']
        if 'remain_repay_int_amt' in response:
            self.remain_repay_int_amt = response['remain_repay_int_amt']
        if 'remain_repay_prin_amt' in response:
            self.remain_repay_prin_amt = response['remain_repay_prin_amt']
        if 'repay_mode' in response:
            self.repay_mode = response['repay_mode']
        if 'repay_plan_term_list' in response:
            self.repay_plan_term_list = response['repay_plan_term_list']
        if 'start_date' in response:
            self.start_date = response['start_date']
        if 'status' in response:
            self.status = response['status']
