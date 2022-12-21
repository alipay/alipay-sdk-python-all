#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class ZhimaMerchantSubsidiariesApplyResponse(AlipayResponse):

    def __init__(self):
        super(ZhimaMerchantSubsidiariesApplyResponse, self).__init__()
        self._biz_error_code = None
        self._biz_error_message = None
        self._order_no = None

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
    def order_no(self):
        return self._order_no

    @order_no.setter
    def order_no(self, value):
        self._order_no = value

    def parse_response_content(self, response_content):
        response = super(ZhimaMerchantSubsidiariesApplyResponse, self).parse_response_content(response_content)
        if 'biz_error_code' in response:
            self.biz_error_code = response['biz_error_code']
        if 'biz_error_message' in response:
            self.biz_error_message = response['biz_error_message']
        if 'order_no' in response:
            self.order_no = response['order_no']
