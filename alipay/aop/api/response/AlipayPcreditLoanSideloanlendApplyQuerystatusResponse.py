#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SideloanInstitution import SideloanInstitution
from alipay.aop.api.domain.GrantBankCard import GrantBankCard


class AlipayPcreditLoanSideloanlendApplyQuerystatusResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanlendApplyQuerystatusResponse, self).__init__()
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._fund_supplier = None
        self._institution_loan_apply_no = None
        self._institution_loan_no = None
        self._loan_amount = None
        self._loan_bank_card = None
        self._loan_status = None
        self._loan_time = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def fail_reason_code(self):
        return self._fail_reason_code

    @fail_reason_code.setter
    def fail_reason_code(self, value):
        self._fail_reason_code = value
    @property
    def fail_reason_message(self):
        return self._fail_reason_message

    @fail_reason_message.setter
    def fail_reason_message(self, value):
        self._fail_reason_message = value
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
    def institution_loan_apply_no(self):
        return self._institution_loan_apply_no

    @institution_loan_apply_no.setter
    def institution_loan_apply_no(self, value):
        self._institution_loan_apply_no = value
    @property
    def institution_loan_no(self):
        return self._institution_loan_no

    @institution_loan_no.setter
    def institution_loan_no(self, value):
        self._institution_loan_no = value
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
    def loan_status(self):
        return self._loan_status

    @loan_status.setter
    def loan_status(self, value):
        self._loan_status = value
    @property
    def loan_time(self):
        return self._loan_time

    @loan_time.setter
    def loan_time(self, value):
        self._loan_time = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanSideloanlendApplyQuerystatusResponse, self).parse_response_content(response_content)
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'fund_supplier' in response:
            self.fund_supplier = response['fund_supplier']
        if 'institution_loan_apply_no' in response:
            self.institution_loan_apply_no = response['institution_loan_apply_no']
        if 'institution_loan_no' in response:
            self.institution_loan_no = response['institution_loan_no']
        if 'loan_amount' in response:
            self.loan_amount = response['loan_amount']
        if 'loan_bank_card' in response:
            self.loan_bank_card = response['loan_bank_card']
        if 'loan_status' in response:
            self.loan_status = response['loan_status']
        if 'loan_time' in response:
            self.loan_time = response['loan_time']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
