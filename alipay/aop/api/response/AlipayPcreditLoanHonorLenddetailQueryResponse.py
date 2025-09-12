#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorContractDTO import HonorContractDTO
from alipay.aop.api.domain.HonorRepayPlanTermDTO import HonorRepayPlanTermDTO


class AlipayPcreditLoanHonorLenddetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLenddetailQueryResponse, self).__init__()
        self._apply_date = None
        self._apply_no = None
        self._apply_time = None
        self._apr = None
        self._bind_bank_code = None
        self._bind_bank_name = None
        self._bind_card_no = None
        self._contract_list = None
        self._coupon_no = None
        self._day_rate = None
        self._effective_date = None
        self._institution_names = None
        self._loan_amount = None
        self._loan_source = None
        self._out_order_no = None
        self._overdue_amount = None
        self._overdue_days = None
        self._repay_method = None
        self._repay_plan_terms = None
        self._status = None
        self._total_term = None

    @property
    def apply_date(self):
        return self._apply_date

    @apply_date.setter
    def apply_date(self, value):
        self._apply_date = value
    @property
    def apply_no(self):
        return self._apply_no

    @apply_no.setter
    def apply_no(self, value):
        self._apply_no = value
    @property
    def apply_time(self):
        return self._apply_time

    @apply_time.setter
    def apply_time(self, value):
        self._apply_time = value
    @property
    def apr(self):
        return self._apr

    @apr.setter
    def apr(self, value):
        self._apr = value
    @property
    def bind_bank_code(self):
        return self._bind_bank_code

    @bind_bank_code.setter
    def bind_bank_code(self, value):
        self._bind_bank_code = value
    @property
    def bind_bank_name(self):
        return self._bind_bank_name

    @bind_bank_name.setter
    def bind_bank_name(self, value):
        self._bind_bank_name = value
    @property
    def bind_card_no(self):
        return self._bind_card_no

    @bind_card_no.setter
    def bind_card_no(self, value):
        self._bind_card_no = value
    @property
    def contract_list(self):
        return self._contract_list

    @contract_list.setter
    def contract_list(self, value):
        if isinstance(value, list):
            self._contract_list = list()
            for i in value:
                if isinstance(i, HonorContractDTO):
                    self._contract_list.append(i)
                else:
                    self._contract_list.append(HonorContractDTO.from_alipay_dict(i))
    @property
    def coupon_no(self):
        return self._coupon_no

    @coupon_no.setter
    def coupon_no(self, value):
        self._coupon_no = value
    @property
    def day_rate(self):
        return self._day_rate

    @day_rate.setter
    def day_rate(self, value):
        self._day_rate = value
    @property
    def effective_date(self):
        return self._effective_date

    @effective_date.setter
    def effective_date(self, value):
        self._effective_date = value
    @property
    def institution_names(self):
        return self._institution_names

    @institution_names.setter
    def institution_names(self, value):
        self._institution_names = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_source(self):
        return self._loan_source

    @loan_source.setter
    def loan_source(self, value):
        self._loan_source = value
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
    def repay_method(self):
        return self._repay_method

    @repay_method.setter
    def repay_method(self, value):
        self._repay_method = value
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
    def total_term(self):
        return self._total_term

    @total_term.setter
    def total_term(self, value):
        self._total_term = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorLenddetailQueryResponse, self).parse_response_content(response_content)
        if 'apply_date' in response:
            self.apply_date = response['apply_date']
        if 'apply_no' in response:
            self.apply_no = response['apply_no']
        if 'apply_time' in response:
            self.apply_time = response['apply_time']
        if 'apr' in response:
            self.apr = response['apr']
        if 'bind_bank_code' in response:
            self.bind_bank_code = response['bind_bank_code']
        if 'bind_bank_name' in response:
            self.bind_bank_name = response['bind_bank_name']
        if 'bind_card_no' in response:
            self.bind_card_no = response['bind_card_no']
        if 'contract_list' in response:
            self.contract_list = response['contract_list']
        if 'coupon_no' in response:
            self.coupon_no = response['coupon_no']
        if 'day_rate' in response:
            self.day_rate = response['day_rate']
        if 'effective_date' in response:
            self.effective_date = response['effective_date']
        if 'institution_names' in response:
            self.institution_names = response['institution_names']
        if 'loan_amount' in response:
            self.loan_amount = response['loan_amount']
        if 'loan_source' in response:
            self.loan_source = response['loan_source']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'overdue_amount' in response:
            self.overdue_amount = response['overdue_amount']
        if 'overdue_days' in response:
            self.overdue_days = response['overdue_days']
        if 'repay_method' in response:
            self.repay_method = response['repay_method']
        if 'repay_plan_terms' in response:
            self.repay_plan_terms = response['repay_plan_terms']
        if 'status' in response:
            self.status = response['status']
        if 'total_term' in response:
            self.total_term = response['total_term']
