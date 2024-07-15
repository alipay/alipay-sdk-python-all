#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCloudCloudbaseEnvRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCloudCloudbaseEnvRefundQueryResponse, self).__init__()
        self._refund_amount = None
        self._refund_type = None
        self._total_amount = None
        self._use_amount = None
        self._use_time = None

    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_type(self):
        return self._refund_type

    @refund_type.setter
    def refund_type(self, value):
        self._refund_type = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def use_amount(self):
        return self._use_amount

    @use_amount.setter
    def use_amount(self, value):
        self._use_amount = value
    @property
    def use_time(self):
        return self._use_time

    @use_time.setter
    def use_time(self, value):
        self._use_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayCloudCloudbaseEnvRefundQueryResponse, self).parse_response_content(response_content)
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_type' in response:
            self.refund_type = response['refund_type']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'use_amount' in response:
            self.use_amount = response['use_amount']
        if 'use_time' in response:
            self.use_time = response['use_time']
