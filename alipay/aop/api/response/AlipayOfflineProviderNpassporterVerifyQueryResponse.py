#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineProviderNpassporterVerifyQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineProviderNpassporterVerifyQueryResponse, self).__init__()
        self._phone_number = None
        self._verified = None

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def verified(self):
        return self._verified

    @verified.setter
    def verified(self, value):
        self._verified = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineProviderNpassporterVerifyQueryResponse, self).parse_response_content(response_content)
        if 'phone_number' in response:
            self.phone_number = response['phone_number']
        if 'verified' in response:
            self.verified = response['verified']
