#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainDefinSaasFunditemQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainDefinSaasFunditemQueryResponse, self).__init__()
        self._fund_type = None
        self._out_order_id = None
        self._out_request_id = None
        self._platform_member_id = None
        self._request_amount = None
        self._request_currency = None
        self._state = None

    @property
    def fund_type(self):
        return self._fund_type

    @fund_type.setter
    def fund_type(self, value):
        self._fund_type = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def out_request_id(self):
        return self._out_request_id

    @out_request_id.setter
    def out_request_id(self, value):
        self._out_request_id = value
    @property
    def platform_member_id(self):
        return self._platform_member_id

    @platform_member_id.setter
    def platform_member_id(self, value):
        self._platform_member_id = value
    @property
    def request_amount(self):
        return self._request_amount

    @request_amount.setter
    def request_amount(self, value):
        self._request_amount = value
    @property
    def request_currency(self):
        return self._request_currency

    @request_currency.setter
    def request_currency(self, value):
        self._request_currency = value
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainDefinSaasFunditemQueryResponse, self).parse_response_content(response_content)
        if 'fund_type' in response:
            self.fund_type = response['fund_type']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'out_request_id' in response:
            self.out_request_id = response['out_request_id']
        if 'platform_member_id' in response:
            self.platform_member_id = response['platform_member_id']
        if 'request_amount' in response:
            self.request_amount = response['request_amount']
        if 'request_currency' in response:
            self.request_currency = response['request_currency']
        if 'state' in response:
            self.state = response['state']
