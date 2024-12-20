#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Loan import Loan


class AlipayPcreditLoanSideloanrepayLoanarBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanSideloanrepayLoanarBatchqueryResponse, self).__init__()
        self._loan_list = None
        self._return_code = None
        self._return_sub_code = None
        self._return_sub_message = None

    @property
    def loan_list(self):
        return self._loan_list

    @loan_list.setter
    def loan_list(self, value):
        if isinstance(value, list):
            self._loan_list = list()
            for i in value:
                if isinstance(i, Loan):
                    self._loan_list.append(i)
                else:
                    self._loan_list.append(Loan.from_alipay_dict(i))
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
        response = super(AlipayPcreditLoanSideloanrepayLoanarBatchqueryResponse, self).parse_response_content(response_content)
        if 'loan_list' in response:
            self.loan_list = response['loan_list']
        if 'return_code' in response:
            self.return_code = response['return_code']
        if 'return_sub_code' in response:
            self.return_sub_code = response['return_sub_code']
        if 'return_sub_message' in response:
            self.return_sub_message = response['return_sub_message']
