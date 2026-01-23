#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsExpressOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsExpressOrderQueryResponse, self).__init__()
        self._card_url = None

    @property
    def card_url(self):
        return self._card_url

    @card_url.setter
    def card_url(self, value):
        self._card_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsExpressOrderQueryResponse, self).parse_response_content(response_content)
        if 'card_url' in response:
            self.card_url = response['card_url']
