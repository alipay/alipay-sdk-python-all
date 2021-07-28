#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBusinessPaymenthubRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBusinessPaymenthubRefundResponse, self).__init__()
        self._channel = None
        self._refund_amount = None
        self._refund_id = None
        self._refund_request_no = None
        self._refund_status = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def refund_amount(self):
        return self._refund_amount

    @refund_amount.setter
    def refund_amount(self, value):
        self._refund_amount = value
    @property
    def refund_id(self):
        return self._refund_id

    @refund_id.setter
    def refund_id(self, value):
        if isinstance(value, list):
            self._refund_id = list()
            for i in value:
                self._refund_id.append(i)
    @property
    def refund_request_no(self):
        return self._refund_request_no

    @refund_request_no.setter
    def refund_request_no(self, value):
        self._refund_request_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayBusinessPaymenthubRefundResponse, self).parse_response_content(response_content)
        if 'channel' in response:
            self.channel = response['channel']
        if 'refund_amount' in response:
            self.refund_amount = response['refund_amount']
        if 'refund_id' in response:
            self.refund_id = response['refund_id']
        if 'refund_request_no' in response:
            self.refund_request_no = response['refund_request_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
