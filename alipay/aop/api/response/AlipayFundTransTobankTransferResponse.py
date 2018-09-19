#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransTobankTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransTobankTransferResponse, self).__init__()
        self._arrival_time_end = None
        self._order_id = None
        self._out_biz_no = None

    @property
    def arrival_time_end(self):
        return self._arrival_time_end

    @arrival_time_end.setter
    def arrival_time_end(self, value):
        self._arrival_time_end = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_biz_no(self):
        return self._out_biz_no

    @out_biz_no.setter
    def out_biz_no(self, value):
        self._out_biz_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransTobankTransferResponse, self).parse_response_content(response_content)
        if 'arrival_time_end' in response:
            self.arrival_time_end = response['arrival_time_end']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
