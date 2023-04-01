#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceEcServiceOrderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceEcServiceOrderCancelResponse, self).__init__()
        self._cancel_contract_url = None

    @property
    def cancel_contract_url(self):
        return self._cancel_contract_url

    @cancel_contract_url.setter
    def cancel_contract_url(self, value):
        self._cancel_contract_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceEcServiceOrderCancelResponse, self).parse_response_content(response_content)
        if 'cancel_contract_url' in response:
            self.cancel_contract_url = response['cancel_contract_url']
