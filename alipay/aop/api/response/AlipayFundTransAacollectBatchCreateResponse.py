#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAacollectBatchCreateResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAacollectBatchCreateResponse, self).__init__()
        self._batch_no = None
        self._batch_token = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_token(self):
        return self._batch_token

    @batch_token.setter
    def batch_token(self, value):
        self._batch_token = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAacollectBatchCreateResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_token' in response:
            self.batch_token = response['batch_token']
