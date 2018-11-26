#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.SchemaVO import SchemaVO


class AlipayPcreditLoanCreditQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditLoanCreditQueryResponse, self).__init__()
        self._credit_amt = None
        self._loanable_amt = None
        self._reject_code = None
        self._reject_message = None
        self._repay_day = None
        self._schema = None
        self._status = None

    @property
    def credit_amt(self):
        return self._credit_amt

    @credit_amt.setter
    def credit_amt(self, value):
        self._credit_amt = value
    @property
    def loanable_amt(self):
        return self._loanable_amt

    @loanable_amt.setter
    def loanable_amt(self, value):
        self._loanable_amt = value
    @property
    def reject_code(self):
        return self._reject_code

    @reject_code.setter
    def reject_code(self, value):
        self._reject_code = value
    @property
    def reject_message(self):
        return self._reject_message

    @reject_message.setter
    def reject_message(self, value):
        self._reject_message = value
    @property
    def repay_day(self):
        return self._repay_day

    @repay_day.setter
    def repay_day(self, value):
        self._repay_day = value
    @property
    def schema(self):
        return self._schema

    @schema.setter
    def schema(self, value):
        if isinstance(value, SchemaVO):
            self._schema = value
        else:
            self._schema = SchemaVO.from_alipay_dict(value)
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditLoanCreditQueryResponse, self).parse_response_content(response_content)
        if 'credit_amt' in response:
            self.credit_amt = response['credit_amt']
        if 'loanable_amt' in response:
            self.loanable_amt = response['loanable_amt']
        if 'reject_code' in response:
            self.reject_code = response['reject_code']
        if 'reject_message' in response:
            self.reject_message = response['reject_message']
        if 'repay_day' in response:
            self.repay_day = response['repay_day']
        if 'schema' in response:
            self.schema = response['schema']
        if 'status' in response:
            self.status = response['status']
