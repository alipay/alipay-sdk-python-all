#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyMerchantSignResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyMerchantSignResponse, self).__init__()
        self._merchant_id = None
        self._out_request_no = None
        self._process_no = None
        self._status = None

    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def process_no(self):
        return self._process_no

    @process_no.setter
    def process_no(self, value):
        self._process_no = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyMerchantSignResponse, self).parse_response_content(response_content)
        if 'merchant_id' in response:
            self.merchant_id = response['merchant_id']
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'process_no' in response:
            self.process_no = response['process_no']
        if 'status' in response:
            self.status = response['status']
