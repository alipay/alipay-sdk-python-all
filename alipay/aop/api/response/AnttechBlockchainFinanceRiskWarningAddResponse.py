#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceRiskWarningAddResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceRiskWarningAddResponse, self).__init__()
        self._submit_result = None

    @property
    def submit_result(self):
        return self._submit_result

    @submit_result.setter
    def submit_result(self, value):
        self._submit_result = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceRiskWarningAddResponse, self).parse_response_content(response_content)
        if 'submit_result' in response:
            self.submit_result = response['submit_result']
