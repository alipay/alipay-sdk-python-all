#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SideloanInstitution import SideloanInstitution
from alipay.aop.api.domain.LendInstallment import LendInstallment
from alipay.aop.api.domain.GrantBankCard import GrantBankCard


class AlipayPcreditLoanSideloanlendLenddetailQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanlendLenddetailQueryResponse, self).__init__()
        self._fund_supplier = None
        self._installment_list = None
        self._institution_loan_no = None
        self._interest_rate = None
        self._loan_amount = None
        self._loan_bank_card = None
        self._loan_end_date = None
        self._loan_start_date = None
        self._loan_term = None
        self._loan_term_unit = None
        self._repayment_day = None
        self._repayment_method = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None
        self._status = None

    @property
    def fund_supplier(self):
        return self._fund_supplier

    @fund_supplier.setter
    def fund_supplier(self, value):
        if isinstance(value, SideloanInstitution):
            self._fund_supplier = value
        else:
            self._fund_supplier = SideloanInstitution.from_alipay_dict(value)
    @property
    def installment_list(self):
        return self._installment_list

    @installment_list.setter
    def installment_list(self, value):
        if isinstance(value, list):
            self._installment_list = list()
            for i in value:
                if isinstance(i, LendInstallment):
                    self._installment_list.append(i)
                else:
                    self._installment_list.append(LendInstallment.from_alipay_dict(i))
    @property
    def institution_loan_no(self):
        return self._institution_loan_no

    @institution_loan_no.setter
    def institution_loan_no(self, value):
        self._institution_loan_no = value
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        self._interest_rate = value
    @property
    def loan_amount(self):
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        self._loan_amount = value
    @property
    def loan_bank_card(self):
        return self._loan_bank_card

    @loan_bank_card.setter
    def loan_bank_card(self, value):
        if isinstance(value, GrantBankCard):
            self._loan_bank_card = value
        else:
            self._loan_bank_card = GrantBankCard.from_alipay_dict(value)
    @property
    def loan_end_date(self):
        return self._loan_end_date

    @loan_end_date.setter
    def loan_end_date(self, value):
        self._loan_end_date = value
    @property
    def loan_start_date(self):
        return self._loan_start_date

    @loan_start_date.setter
    def loan_start_date(self, value):
        self._loan_start_date = value
    @property
    def loan_term(self):
        return self._loan_term

    @loan_term.setter
    def loan_term(self, value):
        self._loan_term = value
    @property
    def loan_term_unit(self):
        return self._loan_term_unit

    @loan_term_unit.setter
    def loan_term_unit(self, value):
        self._loan_term_unit = value
    @property
    def repayment_day(self):
        return self._repayment_day

    @repayment_day.setter
    def repayment_day(self, value):
        self._repayment_day = value
    @property
    def repayment_method(self):
        return self._repayment_method

    @repayment_method.setter
    def repayment_method(self, value):
        self._repayment_method = value
    @property
    def return_code(self):
        return self._return_code

    @return_code.setter
    def return_code(self, value):
        self._return_code = value
    @property
    def return_sub_code(self):
        return self._return_sub_code

    @return_sub_code.setter
    def return_sub_code(self, value):
        self._return_sub_code = value
    @property
    def return_sub_message(self):
        return self._return_sub_message

    @return_sub_message.setter
    def return_sub_message(self, value):
        self._return_sub_message = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanlendLenddetailQueryResponse, self).parse_response_content(response_content)
        if 'fund_supplier' in response:
            self.fund_supplier = response['fund_supplier']
        if 'installment_list' in response:
            self.installment_list = response['installment_list']
        if 'institution_loan_no' in response:
            self.institution_loan_no = response['institution_loan_no']
        if 'interest_rate' in response:
            self.interest_rate = response['interest_rate']
        if 'loan_amount' in response:
            self.loan_amount = response['loan_amount']
        if 'loan_bank_card' in response:
            self.loan_bank_card = response['loan_bank_card']
        if 'loan_end_date' in response:
            self.loan_end_date = response['loan_end_date']
        if 'loan_start_date' in response:
            self.loan_start_date = response['loan_start_date']
        if 'loan_term' in response:
            self.loan_term = response['loan_term']
        if 'loan_term_unit' in response:
            self.loan_term_unit = response['loan_term_unit']
        if 'repayment_day' in response:
            self.repayment_day = response['repayment_day']
        if 'repayment_method' in response:
            self.repayment_method = response['repayment_method']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
        if 'status' in response:
            self.status = response['status']
