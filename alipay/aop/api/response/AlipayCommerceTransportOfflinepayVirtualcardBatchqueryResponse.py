#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AlipayQueryCardModelResult import AlipayQueryCardModelResult


class AlipayCommerceTransportOfflinepayVirtualcardBatchqueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportOfflinepayVirtualcardBatchqueryResponse, self).__init__()
        self._card_models = None
        self._error_message = None
        self._sub_error_code = None

    @property
    def card_models(self):
        return self._card_models

    @card_models.setter
    def card_models(self, value):
        if isinstance(value, list):
            self._card_models = list()
            for i in value:
                if isinstance(i, AlipayQueryCardModelResult):
                    self._card_models.append(i)
                else:
                    self._card_models.append(AlipayQueryCardModelResult.from_alipay_dict(i))
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def sub_error_code(self):
        return self._sub_error_code

    @sub_error_code.setter
    def sub_error_code(self, value):
        self._sub_error_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportOfflinepayVirtualcardBatchqueryResponse, self).parse_response_content(response_content)
        if 'card_models' in response:
            self.card_models = response['card_models']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'sub_error_code' in response:
            self.sub_error_code = response['sub_error_code']
