#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiSelleradmitRealtimeCertifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiSelleradmitRealtimeCertifyResponse, self).__init__()
        self._reason_code = None
        self._result = None

    @property
    def reason_code(self):
        return self._reason_code

    @reason_code.setter
    def reason_code(self, value):
        self._reason_code = value
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiSelleradmitRealtimeCertifyResponse, self).parse_response_content(response_content)
        if 'reason_code' in response:
            self.reason_code = response['reason_code']
        if 'result' in response:
            self.result = response['result']
