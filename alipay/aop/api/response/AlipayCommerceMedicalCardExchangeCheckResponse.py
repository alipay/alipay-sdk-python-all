#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceMedicalCardExchangeCheckResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceMedicalCardExchangeCheckResponse, self).__init__()
        self._content = None
        self._used = None

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
    @property
    def used(self):
        return self._used

    @used.setter
    def used(self, value):
        self._used = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceMedicalCardExchangeCheckResponse, self).parse_response_content(response_content)
        if 'content' in response:
            self.content = response['content']
        if 'used' in response:
            self.used = response['used']
