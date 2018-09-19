#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoantradeLoanrelationQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoantradeLoanrelationQueryResponse, self).__init__()
        self._loan_relation_flag = None

    @property
    def loan_relation_flag(self):
        return self._loan_relation_flag

    @loan_relation_flag.setter
    def loan_relation_flag(self, value):
        self._loan_relation_flag = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoantradeLoanrelationQueryResponse, self).parse_response_content(response_content)
        if 'loan_relation_flag' in response:
            self.loan_relation_flag = response['loan_relation_flag']
