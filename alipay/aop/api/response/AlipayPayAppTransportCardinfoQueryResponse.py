#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPayAppTransportCardinfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayAppTransportCardinfoQueryResponse, self).__init__()
        self._card_data_cipher = None

    @property
    def card_data_cipher(self):
        return self._card_data_cipher

    @card_data_cipher.setter
    def card_data_cipher(self, value):
        self._card_data_cipher = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayAppTransportCardinfoQueryResponse, self).parse_response_content(response_content)
        if 'card_data_cipher' in response:
            self.card_data_cipher = response['card_data_cipher']
