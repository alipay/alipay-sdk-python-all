#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDigitalmgmtPunchoutBasketCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDigitalmgmtPunchoutBasketCreateResponse, self).__init__()
        self._redirect_url = None

    @property
    def redirect_url(self):
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, value):
        self._redirect_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayDigitalmgmtPunchoutBasketCreateResponse, self).parse_response_content(response_content)
        if 'redirect_url' in response:
            self.redirect_url = response['redirect_url']
