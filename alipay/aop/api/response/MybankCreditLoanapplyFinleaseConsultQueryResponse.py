#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankCreditLoanapplyFinleaseConsultQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankCreditLoanapplyFinleaseConsultQueryResponse, self).__init__()
        self._admit = None

    @property
    def admit(self):
        return self._admit

    @admit.setter
    def admit(self, value):
        self._admit = value

    def parse_response_content(self, response_content):
        response = super(MybankCreditLoanapplyFinleaseConsultQueryResponse, self).parse_response_content(response_content)
        if 'admit' in response:
            self.admit = response['admit']
