#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBatchCloseResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBatchCloseResponse, self).__init__()
        self._batch_trans_id = None
        self._status = None

    @property
    def batch_trans_id(self):
        return self._batch_trans_id

    @batch_trans_id.setter
    def batch_trans_id(self, value):
        self._batch_trans_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBatchCloseResponse, self).parse_response_content(response_content)
        if 'batch_trans_id' in response:
            self.batch_trans_id = response['batch_trans_id']
        if 'status' in response:
            self.status = response['status']
