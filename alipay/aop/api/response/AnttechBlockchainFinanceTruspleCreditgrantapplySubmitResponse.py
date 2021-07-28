#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceTruspleCreditgrantapplySubmitResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceTruspleCreditgrantapplySubmitResponse, self).__init__()
        self._inst_credit_grant_id = None
        self._result_status = None

    @property
    def inst_credit_grant_id(self):
        return self._inst_credit_grant_id

    @inst_credit_grant_id.setter
    def inst_credit_grant_id(self, value):
        self._inst_credit_grant_id = value
    @property
    def result_status(self):
        return self._result_status

    @result_status.setter
    def result_status(self, value):
        self._result_status = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceTruspleCreditgrantapplySubmitResponse, self).parse_response_content(response_content)
        if 'inst_credit_grant_id' in response:
            self.inst_credit_grant_id = response['inst_credit_grant_id']
        if 'result_status' in response:
            self.result_status = response['result_status']
