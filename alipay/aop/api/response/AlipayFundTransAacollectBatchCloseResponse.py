#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundTransAacollectBatchCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundTransAacollectBatchCloseResponse, self).__init__()
        self._batch_status = None

    @property
    def batch_status(self):
        return self._batch_status

    @batch_status.setter
    def batch_status(self, value):
        self._batch_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundTransAacollectBatchCloseResponse, self).parse_response_content(response_content)
        if 'batch_status' in response:
            self.batch_status = response['batch_status']
