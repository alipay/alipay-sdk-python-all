#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.HonorBankCardDTO import HonorBankCardDTO
from alipay.aop.api.domain.HonorContractDTO import HonorContractDTO
from alipay.aop.api.domain.HonorRepayPlanTermDTO import HonorRepayPlanTermDTO


class AlipayPcreditLoanHonorLendcalcConsultResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanHonorLendcalcConsultResponse, self).__init__()
        self._annual_rate = None
        self._bank_card = None
        self._contract = None
        self._first_repay_date = None
        self._last_repay_date = None
        self._original_rate = None
        self._refuse_code = None
        self._refuse_msg = None
        self._refuse_msg_data = None
        self._repay_plan_terms = None
        self._should_repay_amount = None
        self._should_repay_inter_amount = None
        self._should_repay_prin_amount = None
        self._stakeholders = None
        self._status = None
        self._total_discount = None
        self._trial_serial_no = None

    @property
    def annual_rate(self):
        return self._annual_rate

    @annual_rate.setter
    def annual_rate(self, value):
        self._annual_rate = value
    @property
    def bank_card(self):
        return self._bank_card

    @bank_card.setter
    def bank_card(self, value):
        if isinstance(value, HonorBankCardDTO):
            self._bank_card = value
        else:
            self._bank_card = HonorBankCardDTO.from_alipay_dict(value)
    @property
    def contract(self):
        return self._contract

    @contract.setter
    def contract(self, value):
        if isinstance(value, list):
            self._contract = list()
            for i in value:
                if isinstance(i, HonorContractDTO):
                    self._contract.append(i)
                else:
                    self._contract.append(HonorContractDTO.from_alipay_dict(i))
    @property
    def first_repay_date(self):
        return self._first_repay_date

    @first_repay_date.setter
    def first_repay_date(self, value):
        self._first_repay_date = value
    @property
    def last_repay_date(self):
        return self._last_repay_date

    @last_repay_date.setter
    def last_repay_date(self, value):
        self._last_repay_date = value
    @property
    def original_rate(self):
        return self._original_rate

    @original_rate.setter
    def original_rate(self, value):
        self._original_rate = value
    @property
    def refuse_code(self):
        return self._refuse_code

    @refuse_code.setter
    def refuse_code(self, value):
        self._refuse_code = value
    @property
    def refuse_msg(self):
        return self._refuse_msg

    @refuse_msg.setter
    def refuse_msg(self, value):
        self._refuse_msg = value
    @property
    def refuse_msg_data(self):
        return self._refuse_msg_data

    @refuse_msg_data.setter
    def refuse_msg_data(self, value):
        self._refuse_msg_data = value
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
    def should_repay_amount(self):
        return self._should_repay_amount

    @should_repay_amount.setter
    def should_repay_amount(self, value):
        self._should_repay_amount = value
    @property
    def should_repay_inter_amount(self):
        return self._should_repay_inter_amount

    @should_repay_inter_amount.setter
    def should_repay_inter_amount(self, value):
        self._should_repay_inter_amount = value
    @property
    def should_repay_prin_amount(self):
        return self._should_repay_prin_amount

    @should_repay_prin_amount.setter
    def should_repay_prin_amount(self, value):
        self._should_repay_prin_amount = value
    @property
    def stakeholders(self):
        return self._stakeholders

    @stakeholders.setter
    def stakeholders(self, value):
        self._stakeholders = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def total_discount(self):
        return self._total_discount

    @total_discount.setter
    def total_discount(self, value):
        self._total_discount = value
    @property
    def trial_serial_no(self):
        return self._trial_serial_no

    @trial_serial_no.setter
    def trial_serial_no(self, value):
        self._trial_serial_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanHonorLendcalcConsultResponse, self).parse_response_content(response_content)
        if 'annual_rate' in response:
            self.annual_rate = response['annual_rate']
        if 'bank_card' in response:
            self.bank_card = response['bank_card']
        if 'contract' in response:
            self.contract = response['contract']
        if 'first_repay_date' in response:
            self.first_repay_date = response['first_repay_date']
        if 'last_repay_date' in response:
            self.last_repay_date = response['last_repay_date']
        if 'original_rate' in response:
            self.original_rate = response['original_rate']
        if 'refuse_code' in response:
            self.refuse_code = response['refuse_code']
        if 'refuse_msg' in response:
            self.refuse_msg = response['refuse_msg']
        if 'refuse_msg_data' in response:
            self.refuse_msg_data = response['refuse_msg_data']
        if 'repay_plan_terms' in response:
            self.repay_plan_terms = response['repay_plan_terms']
        if 'should_repay_amount' in response:
            self.should_repay_amount = response['should_repay_amount']
        if 'should_repay_inter_amount' in response:
            self.should_repay_inter_amount = response['should_repay_inter_amount']
        if 'should_repay_prin_amount' in response:
            self.should_repay_prin_amount = response['should_repay_prin_amount']
        if 'stakeholders' in response:
            self.stakeholders = response['stakeholders']
        if 'status' in response:
            self.status = response['status']
        if 'total_discount' in response:
            self.total_discount = response['total_discount']
        if 'trial_serial_no' in response:
            self.trial_serial_no = response['trial_serial_no']
