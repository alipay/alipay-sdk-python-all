#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransPayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransPayResponse, self).__init__()
        self._order_id = None
        self._out_biz_no = None
        self._pay_fund_order_id = None
        self._status = None
        self._trans_pay_time = None

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
    @property
    def pay_fund_order_id(self):
        return self._pay_fund_order_id

    @pay_fund_order_id.setter
    def pay_fund_order_id(self, value):
        self._pay_fund_order_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def trans_pay_time(self):
        return self._trans_pay_time

    @trans_pay_time.setter
    def trans_pay_time(self, value):
        self._trans_pay_time = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransPayResponse, self).parse_response_content(response_content)
        if 'order_id' in response:
            self.order_id = response['order_id']
        if 'out_biz_no' in response:
            self.out_biz_no = response['out_biz_no']
        if 'pay_fund_order_id' in response:
            self.pay_fund_order_id = response['pay_fund_order_id']
        if 'status' in response:
            self.status = response['status']
        if 'trans_pay_time' in response:
            self.trans_pay_time = response['trans_pay_time']
