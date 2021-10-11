#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeSubaccountInfoQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeSubaccountInfoQueryResponse, self).__init__()
        self._out_channel_id = None
        self._request_no = None
        self._sub_card_no = None

    @property
    def out_channel_id(self):
        return self._out_channel_id

    @out_channel_id.setter
    def out_channel_id(self, value):
        self._out_channel_id = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def sub_card_no(self):
        return self._sub_card_no

    @sub_card_no.setter
    def sub_card_no(self, value):
        self._sub_card_no = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeSubaccountInfoQueryResponse, self).parse_response_content(response_content)
        if 'out_channel_id' in response:
            self.out_channel_id = response['out_channel_id']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'sub_card_no' in response:
            self.sub_card_no = response['sub_card_no']
