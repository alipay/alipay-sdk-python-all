#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingRefundQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingRefundQueryResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._out_order_no = None
        self._out_refund_no = None
        self._parking_order_no = None
        self._parking_refund_no = None
        self._refund_status = None

    @property
    def biz_code(self):
        return self._biz_code

    @biz_code.setter
    def biz_code(self, value):
        self._biz_code = value
    @property
    def biz_msg(self):
        return self._biz_msg

    @biz_msg.setter
    def biz_msg(self, value):
        self._biz_msg = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_refund_no(self):
        return self._out_refund_no

    @out_refund_no.setter
    def out_refund_no(self, value):
        self._out_refund_no = value
    @property
    def parking_order_no(self):
        return self._parking_order_no

    @parking_order_no.setter
    def parking_order_no(self, value):
        self._parking_order_no = value
    @property
    def parking_refund_no(self):
        return self._parking_refund_no

    @parking_refund_no.setter
    def parking_refund_no(self, value):
        self._parking_refund_no = value
    @property
    def refund_status(self):
        return self._refund_status

    @refund_status.setter
    def refund_status(self, value):
        self._refund_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingRefundQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_refund_no' in response:
            self.out_refund_no = response['out_refund_no']
        if 'parking_order_no' in response:
            self.parking_order_no = response['parking_order_no']
        if 'parking_refund_no' in response:
            self.parking_refund_no = response['parking_refund_no']
        if 'refund_status' in response:
            self.refund_status = response['refund_status']
