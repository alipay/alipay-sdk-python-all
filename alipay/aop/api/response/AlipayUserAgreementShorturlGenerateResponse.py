#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserAgreementShorturlGenerateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserAgreementShorturlGenerateResponse, self).__init__()
        self._short_url = None

    @property
    def short_url(self):
        return self._short_url

    @short_url.setter
    def short_url(self, value):
        self._short_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserAgreementShorturlGenerateResponse, self).parse_response_content(response_content)
        if 'short_url' in response:
            self.short_url = response['short_url']
