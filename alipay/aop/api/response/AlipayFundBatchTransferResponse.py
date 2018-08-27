#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayFundBatchTransferResponse(AlipayResponse):

    def __init__(self):
        super(AlipayFundBatchTransferResponse, self).__init__()
        self._batch_no = None
        self._batch_trans_id = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_trans_id(self):
        return self._batch_trans_id

    @batch_trans_id.setter
    def batch_trans_id(self, value):
        self._batch_trans_id = value

    def parse_response_content(self, response_content):
        response = super(AlipayFundBatchTransferResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_trans_id' in response:
            self.batch_trans_id = response['batch_trans_id']
