#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBailOperationDepositCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBailOperationDepositCreateResponse, self).__init__()
        self._auth_no = None
        self._biz_error = None
        self._gmt_create = None
        self._operation_id = None
        self._out_request_no = None
        self._result_code = None
        self._result_message = None

    @property
    def auth_no(self):
        return self._auth_no

    @auth_no.setter
    def auth_no(self, value):
        self._auth_no = value
    @property
    def biz_error(self):
        return self._biz_error

    @biz_error.setter
    def biz_error(self, value):
        self._biz_error = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def operation_id(self):
        return self._operation_id

    @operation_id.setter
    def operation_id(self, value):
        self._operation_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def result_code(self):
        return self._result_code

    @result_code.setter
    def result_code(self, value):
        self._result_code = value
    @property
    def result_message(self):
        return self._result_message

    @result_message.setter
    def result_message(self, value):
        self._result_message = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBailOperationDepositCreateResponse, self).parse_response_content(response_content)
        if 'auth_no' in response:
            self.auth_no = response['auth_no']
        if 'biz_error' in response:
            self.biz_error = response['biz_error']
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'operation_id' in response:
            self.operation_id = response['operation_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
