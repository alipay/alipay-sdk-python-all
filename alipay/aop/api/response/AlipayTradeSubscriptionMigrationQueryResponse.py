#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionMigrationQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionMigrationQueryResponse, self).__init__()
        self._status = None
        self._subscription_id = None

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionMigrationQueryResponse, self).parse_response_content(response_content)
        if 'status' in response:
            self.status = response['status']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
