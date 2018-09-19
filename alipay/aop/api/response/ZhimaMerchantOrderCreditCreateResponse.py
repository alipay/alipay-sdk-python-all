#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantOrderCreditCreateResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantOrderCreditCreateResponse, self).__init__()
        self._error_code = None
        self._error_msg = None
        self._order_create_time = None
        self._order_status = None
        self._out_order_no = None
        self._page_type = None
        self._success = None
        self._zm_order_no = None

    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def order_create_time(self):
        return self._order_create_time

    @order_create_time.setter
    def order_create_time(self, value):
        self._order_create_time = value
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
    def page_type(self):
        return self._page_type

    @page_type.setter
    def page_type(self, value):
        self._page_type = value
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value
    @property
    def zm_order_no(self):
        return self._zm_order_no

    @zm_order_no.setter
    def zm_order_no(self, value):
        self._zm_order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantOrderCreditCreateResponse, self).parse_response_content(response_content)
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'order_create_time' in response:
            self.order_create_time = response['order_create_time']
        if 'order_status' in response:
            self.order_status = response['order_status']
        if 'out_order_no' in response:
            self.out_order_no = response['out_order_no']
        if 'page_type' in response:
            self.page_type = response['page_type']
        if 'success' in response:
            self.success = response['success']
        if 'zm_order_no' in response:
            self.zm_order_no = response['zm_order_no']
