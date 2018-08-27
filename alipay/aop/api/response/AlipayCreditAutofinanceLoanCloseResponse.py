#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditAutofinanceLoanCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditAutofinanceLoanCloseResponse, self).__init__()
        self._outorderno = None

    @property
    def outorderno(self):
        return self._outorderno

    @outorderno.setter
    def outorderno(self, value):
        self._outorderno = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditAutofinanceLoanCloseResponse, self).parse_response_content(response_content)
        if 'outorderno' in response:
            self.outorderno = response['outorderno']
