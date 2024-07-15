#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayMerchantSolutionBatchQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayMerchantSolutionBatchQueryResponse, self).__init__()
        self._batch_no = None
        self._batch_status_code = None
        self._batch_status_desc = None
        self._file_token = None
        self._file_url = None
        self._out_batch_no = None

    @property
    def batch_no(self):
        return self._batch_no

    @batch_no.setter
    def batch_no(self, value):
        self._batch_no = value
    @property
    def batch_status_code(self):
        return self._batch_status_code

    @batch_status_code.setter
    def batch_status_code(self, value):
        self._batch_status_code = value
    @property
    def batch_status_desc(self):
        return self._batch_status_desc

    @batch_status_desc.setter
    def batch_status_desc(self, value):
        self._batch_status_desc = value
    @property
    def file_token(self):
        return self._file_token

    @file_token.setter
    def file_token(self, value):
        self._file_token = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
    @property
    def out_batch_no(self):
        return self._out_batch_no

    @out_batch_no.setter
    def out_batch_no(self, value):
        self._out_batch_no = value

    def parse_response_content(self, response_content):
        response = super(AlipayMerchantSolutionBatchQueryResponse, self).parse_response_content(response_content)
        if 'batch_no' in response:
            self.batch_no = response['batch_no']
        if 'batch_status_code' in response:
            self.batch_status_code = response['batch_status_code']
        if 'batch_status_desc' in response:
            self.batch_status_desc = response['batch_status_desc']
        if 'file_token' in response:
            self.file_token = response['file_token']
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'out_batch_no' in response:
            self.out_batch_no = response['out_batch_no']
