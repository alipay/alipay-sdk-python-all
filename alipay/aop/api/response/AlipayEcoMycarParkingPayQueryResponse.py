#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEcoMycarParkingPayQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEcoMycarParkingPayQueryResponse, self).__init__()
        self._biz_code = None
        self._biz_msg = None
        self._gmt_pay = None
        self._order_status = None
        self._out_order_no = None
        self._parking_order_no = None
        self._plate_color = None
        self._plate_no = None
        self._total_amount = None
        self._trade_desc = None
        self._trade_no = None

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
    def gmt_pay(self):
        return self._gmt_pay

    @gmt_pay.setter
    def gmt_pay(self, value):
        self._gmt_pay = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def parking_order_no(self):
        return self._parking_order_no

    @parking_order_no.setter
    def parking_order_no(self, value):
        self._parking_order_no = value
    @property
    def plate_color(self):
        return self._plate_color

    @plate_color.setter
    def plate_color(self, value):
        self._plate_color = value
    @property
    def plate_no(self):
        return self._plate_no

    @plate_no.setter
    def plate_no(self, value):
        self._plate_no = value
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value
    @property
    def trade_desc(self):
        return self._trade_desc

    @trade_desc.setter
    def trade_desc(self, value):
        self._trade_desc = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayEcoMycarParkingPayQueryResponse, self).parse_response_content(response_content)
        if 'biz_code' in response:
            self.biz_code = response['biz_code']
        if 'biz_msg' in response:
            self.biz_msg = response['biz_msg']
        if 'gmt_pay' in response:
            self.gmt_pay = response['gmt_pay']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'parking_order_no' in response:
            self.parking_order_no = response['parking_order_no']
        if 'plate_color' in response:
            self.plate_color = response['plate_color']
        if 'plate_no' in response:
            self.plate_no = response['plate_no']
        if 'total_amount' in response:
            self.total_amount = response['total_amount']
        if 'trade_desc' in response:
            self.trade_desc = response['trade_desc']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
