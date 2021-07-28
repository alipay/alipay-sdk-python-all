#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditCreditriskConsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditCreditriskConsultQueryResponse, self).__init__()
        self._available_amt = None
        self._consult_result_code = None
        self._consult_result_msg = None
        self._creditlmt_amt = None
        self._loan_int_rate = None

    @property
    def available_amt(self):
        return self._available_amt

    @available_amt.setter
    def available_amt(self, value):
        self._available_amt = value
    @property
    def consult_result_code(self):
        return self._consult_result_code

    @consult_result_code.setter
    def consult_result_code(self, value):
        self._consult_result_code = value
    @property
    def consult_result_msg(self):
        return self._consult_result_msg

    @consult_result_msg.setter
    def consult_result_msg(self, value):
        self._consult_result_msg = value
    @property
    def creditlmt_amt(self):
        return self._creditlmt_amt

    @creditlmt_amt.setter
    def creditlmt_amt(self, value):
        self._creditlmt_amt = value
    @property
    def loan_int_rate(self):
        return self._loan_int_rate

    @loan_int_rate.setter
    def loan_int_rate(self, value):
        self._loan_int_rate = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditCreditriskConsultQueryResponse, self).parse_response_content(response_content)
        if 'available_amt' in response:
            self.available_amt = response['available_amt']
        if 'consult_result_code' in response:
            self.consult_result_code = response['consult_result_code']
        if 'consult_result_msg' in response:
            self.consult_result_msg = response['consult_result_msg']
        if 'creditlmt_amt' in response:
            self.creditlmt_amt = response['creditlmt_amt']
        if 'loan_int_rate' in response:
            self.loan_int_rate = response['loan_int_rate']
