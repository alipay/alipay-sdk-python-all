#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantSubsidiariesCloseResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantSubsidiariesCloseResponse, self).__init__()
        self._biz_error_code = None
        self._biz_error_message = None
        self._order_memo = None
        self._order_no = None
        self._order_status = None

    @property
    def biz_error_code(self):
        return self._biz_error_code

    @biz_error_code.setter
    def biz_error_code(self, value):
        self._biz_error_code = value
    @property
    def biz_error_message(self):
        return self._biz_error_message

    @biz_error_message.setter
    def biz_error_message(self, value):
        self._biz_error_message = value
    @property
    def order_memo(self):
        return self._order_memo

    @order_memo.setter
    def order_memo(self, value):
        self._order_memo = value
    @property
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value
    @property
    def order_status(self):
        return self._order_status

    @order_status.setter
    def order_status(self, value):
        self._order_status = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantSubsidiariesCloseResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'biz_error_message' in response:
            self.biz_error_message = response['biz_error_message']
        if 'order_memo' in response:
            self.order_memo = response['order_memo']
        if 'order_no' in response:
            self.order_no = response['order_no']
        if 'order_status' in response:
            self.order_status = response['order_status']
