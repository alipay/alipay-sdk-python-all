#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechNftCtocSmscodeQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechNftCtocSmscodeQueryResponse, self).__init__()
        self._sms_code = None

    @property
    def sms_code(self):
        return self._sms_code

    @sms_code.setter
    def sms_code(self, value):
        self._sms_code = value

    def parse_response_content(self, response_content):
        response = super(AnttechNftCtocSmscodeQueryResponse, self).parse_response_content(response_content)
        if 'sms_code' in response:
            self.sms_code = response['sms_code']
