#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloansignCreditApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloansignCreditApplyResponse, self).__init__()
        self._credit_status = None
        self._fail_reason_code = None
        self._fail_reason_message = None
        self._institution_loan_apply_no = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def credit_status(self):
        return self._credit_status

    @credit_status.setter
    def credit_status(self, value):
        self._credit_status = value
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
    def institution_loan_apply_no(self):
        return self._institution_loan_apply_no

    @institution_loan_apply_no.setter
    def institution_loan_apply_no(self, value):
        self._institution_loan_apply_no = value
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
        response = super(AlipayPcreditLoanSideloansignCreditApplyResponse, self).parse_response_content(response_content)
        if 'credit_status' in response:
            self.credit_status = response['credit_status']
        if 'fail_reason_code' in response:
            self.fail_reason_code = response['fail_reason_code']
        if 'fail_reason_message' in response:
            self.fail_reason_message = response['fail_reason_message']
        if 'institution_loan_apply_no' in response:
            self.institution_loan_apply_no = response['institution_loan_apply_no']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
