#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderCreditPayResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderCreditPayResponse, self).__init__()
        self._alipay_fund_order_no = None
        self._channel = None
        self._message = None
        self._out_order_no = None
        self._out_trans_no = None
        self._pay_amount = None
        self._pay_status = None
        self._pay_time = None
        self._zm_order_no = None

    @property
    def alipay_fund_order_no(self):
        return self._alipay_fund_order_no

    @alipay_fund_order_no.setter
    def alipay_fund_order_no(self, value):
        self._alipay_fund_order_no = value
    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value
    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
    @property
    def out_order_no(self):
        return self._out_order_no

    @out_order_no.setter
    def out_order_no(self, value):
        self._out_order_no = value
    @property
    def out_trans_no(self):
        return self._out_trans_no

    @out_trans_no.setter
    def out_trans_no(self, value):
        self._out_trans_no = value
    @property
    def pay_amount(self):
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, value):
        self._pay_amount = value
    @property
    def pay_status(self):
        return self._pay_status

    @pay_status.setter
    def pay_status(self, value):
        self._pay_status = value
    @property
    def pay_time(self):
        return self._pay_time

    @pay_time.setter
    def pay_time(self, value):
        self._pay_time = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderCreditPayResponse, self).parse_response_content(response_content)
        if 'alipay_fund_order_no' in response:
            self.alipay_fund_order_no = response['alipay_fund_order_no']
        if 'channel' in response:
            self.channel = response['channel']
        if 'message' in response:
            self.message = response['message']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'out_trans_no' in response:
            self.out_trans_no = response['out_trans_no']
        if 'pay_amount' in response:
            self.pay_amount = response['pay_amount']
        if 'pay_status' in response:
            self.pay_status = response['pay_status']
        if 'pay_time' in response:
            self.pay_time = response['pay_time']
        if 'zm_order_no' in response:
            self.zm_order_no = response['zm_order_no']
