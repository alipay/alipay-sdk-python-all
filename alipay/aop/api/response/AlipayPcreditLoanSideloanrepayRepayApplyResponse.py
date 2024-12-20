#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditLoanSideloanrepayRepayApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanrepayRepayApplyResponse, self).__init__()
        self._extension = None
        self._institution_repayment_no = None
        self._open_id = None
        self._payment_params = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value
    @property
    def institution_repayment_no(self):
        return self._institution_repayment_no

    @institution_repayment_no.setter
    def institution_repayment_no(self, value):
        self._institution_repayment_no = value
    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        self._open_id = value
    @property
    def payment_params(self):
        return self._payment_params

    @payment_params.setter
    def payment_params(self, value):
        self._payment_params = value
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
        response = super(AlipayPcreditLoanSideloanrepayRepayApplyResponse, self).parse_response_content(response_content)
        if 'extension' in response:
            self.extension = response['extension']
        if 'institution_repayment_no' in response:
            self.institution_repayment_no = response['institution_repayment_no']
        if 'open_id' in response:
            self.open_id = response['open_id']
        if 'payment_params' in response:
            self.payment_params = response['payment_params']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
