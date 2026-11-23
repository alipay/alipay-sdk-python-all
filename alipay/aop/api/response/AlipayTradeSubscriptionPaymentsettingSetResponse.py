#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionPaymentsettingSetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionPaymentsettingSetResponse, self).__init__()
        self._subscription_id = None

    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionPaymentsettingSetResponse, self).parse_response_content(response_content)
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
