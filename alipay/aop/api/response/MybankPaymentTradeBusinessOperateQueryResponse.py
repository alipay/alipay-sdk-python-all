#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankPaymentTradeBusinessOperateQueryResponse(AlipayResponse):

    def __init__(self):
        super(MybankPaymentTradeBusinessOperateQueryResponse, self).__init__()
        self._biz_scene = None
        self._currency_value = None
        self._finish_time = None
        self._operate_no = None
        self._operate_status = None
        self._operate_type = None
        self._order_no = None
        self._out_trade_no = None
        self._product_code = None
        self._request_no = None
        self._retry = None
        self._trade_amt = None

    @property
    def biz_scene(self):
        return self._biz_scene

    @biz_scene.setter
    def biz_scene(self, value):
        self._biz_scene = value
    @property
    def currency_value(self):
        return self._currency_value

    @currency_value.setter
    def currency_value(self, value):
        self._currency_value = value
    @property
    def finish_time(self):
        return self._finish_time

    @finish_time.setter
    def finish_time(self, value):
        self._finish_time = value
    @property
    def operate_no(self):
        return self._operate_no

    @operate_no.setter
    def operate_no(self, value):
        self._operate_no = value
    @property
    def operate_status(self):
        return self._operate_status

    @operate_status.setter
    def operate_status(self, value):
        self._operate_status = value
    @property
    def operate_type(self):
        return self._operate_type

    @operate_type.setter
    def operate_type(self, value):
        self._operate_type = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def product_code(self):
        return self._product_code

    @product_code.setter
    def product_code(self, value):
        self._product_code = value
    @property
    def request_no(self):
        return self._request_no

    @request_no.setter
    def request_no(self, value):
        self._request_no = value
    @property
    def retry(self):
        return self._retry

    @retry.setter
    def retry(self, value):
        self._retry = value
    @property
    def trade_amt(self):
        return self._trade_amt

    @trade_amt.setter
    def trade_amt(self, value):
        self._trade_amt = value

    def parse_response_content(self, response_content):
        response = super(MybankPaymentTradeBusinessOperateQueryResponse, self).parse_response_content(response_content)
        if 'biz_scene' in response:
            self.biz_scene = response['biz_scene']
        if 'currency_value' in response:
            self.currency_value = response['currency_value']
        if 'finish_time' in response:
            self.finish_time = response['finish_time']
        if 'operate_no' in response:
            self.operate_no = response['operate_no']
        if 'operate_status' in response:
            self.operate_status = response['operate_status']
        if 'operate_type' in response:
            self.operate_type = response['operate_type']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'product_code' in response:
            self.product_code = response['product_code']
        if 'request_no' in response:
            self.request_no = response['request_no']
        if 'retry' in response:
            self.retry = response['retry']
        if 'trade_amt' in response:
            self.trade_amt = response['trade_amt']
