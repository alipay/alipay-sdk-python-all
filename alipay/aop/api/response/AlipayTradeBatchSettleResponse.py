#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeBatchSettleResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeBatchSettleResponse, self).__init__()
        self._gmt_create = None
        self._out_request_no = None
        self._result_code = None
        self._settle_no = None

    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
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
    def settle_no(self):
        return self._settle_no

    @settle_no.setter
    def settle_no(self, value):
        self._settle_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeBatchSettleResponse, self).parse_response_content(response_content)
        if 'gmt_create' in response:
            self.gmt_create = response['gmt_create']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'settle_no' in response:
            self.settle_no = response['settle_no']
