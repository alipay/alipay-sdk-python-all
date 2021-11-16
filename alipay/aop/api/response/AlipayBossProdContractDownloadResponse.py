#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayBossProdContractDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayBossProdContractDownloadResponse, self).__init__()
        self._business_id = None
        self._file_url = None
        self._result_code = None
        self._result_message = None
        self._result_success = None

    @property
    def business_id(self):
        return self._business_id

    @business_id.setter
    def business_id(self, value):
        self._business_id = value
    @property
    def file_url(self):
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value
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
    @property
    def result_success(self):
        return self._result_success

    @result_success.setter
    def result_success(self, value):
        self._result_success = value

    def parse_response_content(self, response_content):
        response = super(AlipayBossProdContractDownloadResponse, self).parse_response_content(response_content)
        if 'business_id' in response:
            self.business_id = response['business_id']
        if 'file_url' in response:
            self.file_url = response['file_url']
        if 'result_code' in response:
            self.result_code = response['result_code']
        if 'result_message' in response:
            self.result_message = response['result_message']
        if 'result_success' in response:
            self.result_success = response['result_success']
