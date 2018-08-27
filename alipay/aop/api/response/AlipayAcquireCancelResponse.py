#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAcquireCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAcquireCancelResponse, self).__init__()
        self._detail_error_code = None
        self._detail_error_des = None
        self._out_trade_no = None
        self._result_code = None
        self._retry_flag = None
        self._trade_no = None

    @property
    def detail_error_code(self):
        return self._detail_error_code

    @detail_error_code.setter
    def detail_error_code(self, value):
        self._detail_error_code = value
    @property
    def detail_error_des(self):
        return self._detail_error_des

    @detail_error_des.setter
    def detail_error_des(self, value):
        self._detail_error_des = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def retry_flag(self):
        return self._retry_flag

    @retry_flag.setter
    def retry_flag(self, value):
        self._retry_flag = value
    @property
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAcquireCancelResponse, self).parse_response_content(response_content)
        if 'detail_error_code' in response:
            self.detail_error_code = response['detail_error_code']
        if 'detail_error_des' in response:
            self.detail_error_des = response['detail_error_des']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'retry_flag' in response:
            self.retry_flag = response['retry_flag']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
