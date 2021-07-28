#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayPcreditHuabeiPcreditmerchantProductorderCancelResponse(AlipayResponse):

    def __init__(self):
        super(AlipayPcreditHuabeiPcreditmerchantProductorderCancelResponse, self).__init__()
        self._biz_success = None
        self._data = None
        self._error_code = None
        self._error_message = None

    @property
    def biz_success(self):
        return self._biz_success

    @biz_success.setter
    def biz_success(self, value):
        self._biz_success = value
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayPcreditHuabeiPcreditmerchantProductorderCancelResponse, self).parse_response_content(response_content)
        if 'biz_success' in response:
            self.biz_success = response['biz_success']
        if 'data' in response:
            self.data = response['data']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_message' in response:
            self.error_message = response['error_message']
