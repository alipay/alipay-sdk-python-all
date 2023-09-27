#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenMiniOrderOrderbillDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenMiniOrderOrderbillDownloadResponse, self).__init__()
        self._bill_download_url = None
        self._bill_file_code = None

    @property
    def bill_download_url(self):
        return self._bill_download_url

    @bill_download_url.setter
    def bill_download_url(self, value):
        self._bill_download_url = value
    @property
    def bill_file_code(self):
        return self._bill_file_code

    @bill_file_code.setter
    def bill_file_code(self, value):
        self._bill_file_code = value

    def parse_response_content(self, response_content):
        response = super(AlipayOpenMiniOrderOrderbillDownloadResponse, self).parse_response_content(response_content)
        if 'bill_download_url' in response:
            self.bill_download_url = response['bill_download_url']
        if 'bill_file_code' in response:
            self.bill_file_code = response['bill_file_code']
