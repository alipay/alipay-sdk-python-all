#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayIserviceBillEreceiptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayIserviceBillEreceiptQueryResponse, self).__init__()
        self._download_url = None
        self._error_code = None
        self._error_msg = None
        self._file_id = None
        self._status = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def error_code(self):
        return self._error_code

    @error_code.setter
    def error_code(self, value):
        self._error_code = value
    @property
    def error_msg(self):
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value):
        self._error_msg = value
    @property
    def file_id(self):
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        self._file_id = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayIserviceBillEreceiptQueryResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'error_code' in response:
            self.error_code = response['error_code']
        if 'error_msg' in response:
            self.error_msg = response['error_msg']
        if 'file_id' in response:
            self.file_id = response['file_id']
        if 'status' in response:
            self.status = response['status']
