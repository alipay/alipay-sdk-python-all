#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.Subscription import Subscription


class AlipayTradeSubscriptionQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionQueryResponse, self).__init__()
        self._subscriptions = None

    @property
    def subscriptions(self):
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, value):
        if isinstance(value, list):
            self._subscriptions = list()
            for i in value:
                if isinstance(i, Subscription):
                    self._subscriptions.append(i)
                else:
                    self._subscriptions.append(Subscription.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionQueryResponse, self).parse_response_content(response_content)
        if 'subscriptions' in response:
            self.subscriptions = response['subscriptions']
