#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class TechriskInnovateSalesgptOrderModifyResponse(AlipayResponse):

    def __init__(self):
        super(TechriskInnovateSalesgptOrderModifyResponse, self).__init__()
        self._order_submit_code = None
        self._order_submit_msg = None
        self._order_submit_result = None

    @property
    def order_submit_code(self):
        return self._order_submit_code

    @order_submit_code.setter
    def order_submit_code(self, value):
        self._order_submit_code = value
    @property
    def order_submit_msg(self):
        return self._order_submit_msg

    @order_submit_msg.setter
    def order_submit_msg(self, value):
        self._order_submit_msg = value
    @property
    def order_submit_result(self):
        return self._order_submit_result

    @order_submit_result.setter
    def order_submit_result(self, value):
        self._order_submit_result = value

    def parse_response_content(self, response_content):
        response = super(TechriskInnovateSalesgptOrderModifyResponse, self).parse_response_content(response_content)
        if 'order_submit_code' in response:
            self.order_submit_code = response['order_submit_code']
        if 'order_submit_msg' in response:
            self.order_submit_msg = response['order_submit_msg']
        if 'order_submit_result' in response:
            self.order_submit_result = response['order_submit_result']
