#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyInsturlQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyInsturlQueryResponse, self).__init__()
        self._target_url = None

    @property
    def target_url(self):
        return self._target_url

    @target_url.setter
    def target_url(self, value):
        self._target_url = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyInsturlQueryResponse, self).parse_response_content(response_content)
        if 'target_url' in response:
            self.target_url = response['target_url']
