#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyFundBatchtransferCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyFundBatchtransferCreateResponse, self).__init__()
        self._ecny_batch_transfer_url = None
        self._order_no = None
        self._out_request_from = None
        self._out_request_no = None

    @property
    def ecny_batch_transfer_url(self):
        return self._ecny_batch_transfer_url

    @ecny_batch_transfer_url.setter
    def ecny_batch_transfer_url(self, value):
        self._ecny_batch_transfer_url = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_request_from(self):
        return self._out_request_from

    @out_request_from.setter
    def out_request_from(self, value):
        self._out_request_from = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyFundBatchtransferCreateResponse, self).parse_response_content(response_content)
        if 'ecny_batch_transfer_url' in response:
            self.ecny_batch_transfer_url = response['ecny_batch_transfer_url']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_request_from' in response:
            self.out_request_from = response['out_request_from']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
