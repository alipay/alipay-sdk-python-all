#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceTransportEtcSettlementApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceTransportEtcSettlementApplyResponse, self).__init__()
        self._ext_info = None
        self._out_order_id = None
        self._pay_time = None
        self._total_amount = None
        self._trade_biz_code = None
        self._trade_biz_msg = None
        self._trade_no = None
        self._trade_status = None
        self._trip_id = None

    @property
    def ext_info(self):
        return self._ext_info

    @ext_info.setter
    def ext_info(self, value):
        self._ext_info = value
    @property
    def out_order_id(self):
        return self._out_order_id

    @out_order_id.setter
    def out_order_id(self, value):
        self._out_order_id = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_biz_code(self):
        return self._trade_biz_code

    @trade_biz_code.setter
    def trade_biz_code(self, value):
        self._trade_biz_code = value
    @property
    def trade_biz_msg(self):
        return self._trade_biz_msg

    @trade_biz_msg.setter
    def trade_biz_msg(self, value):
        self._trade_biz_msg = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value
    @property
    def trade_status(self):
        return self._trade_status

    @trade_status.setter
    def trade_status(self, value):
        self._trade_status = value
    @property
    def trip_id(self):
        return self._trip_id

    @trip_id.setter
    def trip_id(self, value):
        self._trip_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceTransportEtcSettlementApplyResponse, self).parse_response_content(response_content)
        if 'ext_info' in response:
            self.ext_info = response['ext_info']
        if 'out_order_id' in response:
            self.out_order_id = response['out_order_id']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_biz_code' in response:
            self.trade_biz_code = response['trade_biz_code']
        if 'trade_biz_msg' in response:
            self.trade_biz_msg = response['trade_biz_msg']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'trade_status' in response:
            self.trade_status = response['trade_status']
        if 'trip_id' in response:
            self.trip_id = response['trip_id']
