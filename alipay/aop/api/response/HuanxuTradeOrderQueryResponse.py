#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class HuanxuTradeOrderQueryResponse(AlipayResponse):

    def __init__(self):
        super(HuanxuTradeOrderQueryResponse, self).__init__()
        self._amount = None
        self._channel = None
        self._instruction_id = None
        self._instruction_type = None
        self._out_request_no = None
        self._status = None

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def instruction_id(self):
        return self._instruction_id

    @instruction_id.setter
    def instruction_id(self, value):
        self._instruction_id = value
    @property
    def instruction_type(self):
        return self._instruction_type

    @instruction_type.setter
    def instruction_type(self, value):
        self._instruction_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(HuanxuTradeOrderQueryResponse, self).parse_response_content(response_content)
        if 'amount' in response:
            self.amount = response['amount']
        if 'channel' in response:
            self.channel = response['channel']
        if 'instruction_id' in response:
            self.instruction_id = response['instruction_id']
        if 'instruction_type' in response:
            self.instruction_type = response['instruction_type']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'status' in response:
            self.status = response['status']
