#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class MybankEcnyEntwalletCreateResponse(AlipayResponse):

    def __init__(self):
        super(MybankEcnyEntwalletCreateResponse, self).__init__()
        self._out_request_no = None
        self._process_no = None
        self._status = None
        self._wallet_id = None

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
    @property
    def wallet_id(self):
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, value):
        self._wallet_id = value

    def parse_response_content(self, response_content):
        response = super(MybankEcnyEntwalletCreateResponse, self).parse_response_content(response_content)
        if 'out_request_no' in response:
            self.out_request_no = response['out_request_no']
        if 'process_no' in response:
            self.process_no = response['process_no']
        if 'status' in response:
            self.status = response['status']
        if 'wallet_id' in response:
            self.wallet_id = response['wallet_id']
