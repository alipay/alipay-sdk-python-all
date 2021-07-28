#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceSportsVenueOrderRefundResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceSportsVenueOrderRefundResponse, self).__init__()
        self._desc = None
        self._order_id = None
        self._out_order_id = None
        self._refund_status = None
        self._trade_no = None

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value
    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, value):
        self._order_id = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceSportsVenueOrderRefundResponse, self).parse_response_content(response_content)
        if 'desc' in response:
            self.desc = response['desc']
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
