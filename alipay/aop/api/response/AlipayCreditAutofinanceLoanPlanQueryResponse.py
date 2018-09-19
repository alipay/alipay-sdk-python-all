#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditAutofinanceLoanPlanQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditAutofinanceLoanPlanQueryResponse, self).__init__()
        self._loanplan = None

    @property
    def loanplan(self):
        return self._loanplan

    @loanplan.setter
    def loanplan(self, value):
        self._loanplan = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditAutofinanceLoanPlanQueryResponse, self).parse_response_content(response_content)
        if 'loanplan' in response:
            self.loanplan = response['loanplan']
