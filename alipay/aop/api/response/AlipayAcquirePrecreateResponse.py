#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayAcquirePrecreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayAcquirePrecreateResponse, self).__init__()
        self._detail_error_code = None
        self._detail_error_des = None
        self._error = None
        self._is_success = None
        self._out_trade_no = None
        self._pic_url = None
        self._qr_code = None
        self._result_code = None
        self._trade_no = None
        self._voucher_type = None

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
    def error(self):
        return self._error

    @error.setter
    def error(self, value):
        self._error = value
    @property
    def is_success(self):
        return self._is_success

    @is_success.setter
    def is_success(self, value):
        self._is_success = value
    @property
    def out_trade_no(self):
        return self._out_trade_no

    @out_trade_no.setter
    def out_trade_no(self, value):
        self._out_trade_no = value
    @property
    def pic_url(self):
        return self._pic_url

    @pic_url.setter
    def pic_url(self, value):
        self._pic_url = value
    @property
    def qr_code(self):
        return self._qr_code

    @qr_code.setter
    def qr_code(self, value):
        self._qr_code = value
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
    @property
    def voucher_type(self):
        return self._voucher_type

    @voucher_type.setter
    def voucher_type(self, value):
        self._voucher_type = value

    def parse_response_content(self, response_content):
        response = super(AlipayAcquirePrecreateResponse, self).parse_response_content(response_content)
        if 'detail_error_code' in response:
            self.detail_error_code = response['detail_error_code']
        if 'detail_error_des' in response:
            self.detail_error_des = response['detail_error_des']
        if 'error' in response:
            self.error = response['error']
        if 'is_success' in response:
            self.is_success = response['is_success']
        if 'out_trade_no' in response:
            self.out_trade_no = response['out_trade_no']
        if 'pic_url' in response:
            self.pic_url = response['pic_url']
        if 'qr_code' in response:
            self.qr_code = response['qr_code']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'trade_no' in response:
            self.trade_no = response['trade_no']
        if 'voucher_type' in response:
            self.voucher_type = response['voucher_type']
