#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.BarcodeEventResponseHeader import BarcodeEventResponseHeader


class AlipayPayCodecApplepayBarcodeeventNotifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPayCodecApplepayBarcodeeventNotifyResponse, self).__init__()
        self._response_header = None
        self._transaction_available = None

    @property
    def response_header(self):
        return self._response_header

    @response_header.setter
    def response_header(self, value):
        if isinstance(value, BarcodeEventResponseHeader):
            self._response_header = value
        else:
            self._response_header = BarcodeEventResponseHeader.from_alipay_dict(value)
    @property
    def transaction_available(self):
        return self._transaction_available

    @transaction_available.setter
    def transaction_available(self, value):
        self._transaction_available = value

    def parse_response_content(self, response_content):
        response = super(AlipayPayCodecApplepayBarcodeeventNotifyResponse, self).parse_response_content(response_content)
        if 'response_header' in response:
            self.response_header = response['response_header']
        if 'transaction_available' in response:
            self.transaction_available = response['transaction_available']
