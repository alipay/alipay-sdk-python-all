#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSubscriptionEstimatedrefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSubscriptionEstimatedrefundQueryResponse, self).__init__()
        self._estimated_refund_amount = None
        self._refundable = None
        self._subscription_id = None
        self._subscription_status = None

    @property
    def estimated_refund_amount(self):
        return self._estimated_refund_amount

    @estimated_refund_amount.setter
    def estimated_refund_amount(self, value):
        self._estimated_refund_amount = value
    @property
    def refundable(self):
        return self._refundable

    @refundable.setter
    def refundable(self, value):
        self._refundable = value
    @property
    def subscription_id(self):
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        self._subscription_id = value
    @property
    def subscription_status(self):
        return self._subscription_status

    @subscription_status.setter
    def subscription_status(self, value):
        self._subscription_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSubscriptionEstimatedrefundQueryResponse, self).parse_response_content(response_content)
        if 'estimated_refund_amount' in response:
            self.estimated_refund_amount = response['estimated_refund_amount']
        if 'refundable' in response:
            self.refundable = response['refundable']
        if 'subscription_id' in response:
            self.subscription_id = response['subscription_id']
        if 'subscription_status' in response:
            self.subscription_status = response['subscription_status']
