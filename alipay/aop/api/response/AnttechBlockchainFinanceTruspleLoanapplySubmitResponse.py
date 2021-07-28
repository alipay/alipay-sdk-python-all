#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTruspleLoanapplySubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTruspleLoanapplySubmitResponse, self).__init__()
        self._loan_id = None
        self._result_status = None

    @property
    def loan_id(self):
        return self._loan_id

    @loan_id.setter
    def loan_id(self, value):
        self._loan_id = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTruspleLoanapplySubmitResponse, self).parse_response_content(response_content)
        if 'loan_id' in response:
            self.loan_id = response['loan_id']
        if 'result_status' in response:
            self.result_status = response['result_status']
