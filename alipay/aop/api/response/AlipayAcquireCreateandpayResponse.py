#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAcquireCreateandpayResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAcquireCreateandpayResponse, self).__init__()
        self._buyer_logon_id = None
        self._buyer_user_id = None
        self._detail_error_code = None
        self._detail_error_des = None
        self._extend_info = None
        self._out_trade_no = None
        self._result_code = None
        self._trade_no = None

    @property
    def buyer_logon_id(self):
        return self._buyer_logon_id

    @buyer_logon_id.setter
    def buyer_logon_id(self, value):
        self._buyer_logon_id = value
    @property
    def buyer_user_id(self):
        return self._buyer_user_id

    @buyer_user_id.setter
    def buyer_user_id(self, value):
        self._buyer_user_id = value
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
    def extend_info(self):
        return self._extend_info

    @extend_info.setter
    def extend_info(self, value):
        self._extend_info = value
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
    def trade_no(self):
        return self._trade_no

    @trade_no.setter
    def trade_no(self, value):
        self._trade_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayAcquireCreateandpayResponse, self).parse_response_content(response_content)
        if 'buyer_logon_id' in response:
            self.buyer_logon_id = response['buyer_logon_id']
        if 'buyer_user_id' in response:
            self.buyer_user_id = response['buyer_user_id']
        if 'detail_error_code' in response:
            self.detail_error_code = response['detail_error_code']
        if 'detail_error_des' in response:
            self.detail_error_des = response['detail_error_des']
        if 'extend_info' in response:
            self.extend_info = response['extend_info']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
