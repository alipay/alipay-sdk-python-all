#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataBillAccountbookereceiptQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataBillAccountbookereceiptQueryResponse, self).__init__()
        self._download_url = None
        self._error_message = None
        self._status = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def error_message(self):
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        self._error_message = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataBillAccountbookereceiptQueryResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
        if 'error_message' in response:
            self.error_message = response['error_message']
        if 'status' in response:
            self.status = response['status']
