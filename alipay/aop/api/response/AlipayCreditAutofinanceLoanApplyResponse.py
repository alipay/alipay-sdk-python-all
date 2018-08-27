#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCreditAutofinanceLoanApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCreditAutofinanceLoanApplyResponse, self).__init__()
        self._applyno = None
        self._needauth = None
        self._outorderno = None

    @property
    def applyno(self):
        return self._applyno

    @applyno.setter
    def applyno(self, value):
        self._applyno = value
    @property
    def needauth(self):
        return self._needauth

    @needauth.setter
    def needauth(self, value):
        self._needauth = value
    @property
    def outorderno(self):
        return self._outorderno

    @outorderno.setter
    def outorderno(self, value):
        self._outorderno = value

    def parse_response_content(self, response_content):
        response = super(AlipayCreditAutofinanceLoanApplyResponse, self).parse_response_content(response_content)
        if 'applyno' in response:
            self.applyno = response['applyno']
        if 'needauth' in response:
            self.needauth = response['needauth']
        if 'outorderno' in response:
            self.outorderno = response['outorderno']
