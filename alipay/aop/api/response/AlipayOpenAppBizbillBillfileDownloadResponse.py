#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOpenAppBizbillBillfileDownloadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOpenAppBizbillBillfileDownloadResponse, self).__init__()
        self._bill_date = None
        self._file_urls = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def file_urls(self):
        return self._file_urls

    @file_urls.setter
    def file_urls(self, value):
        if isinstance(value, list):
            self._file_urls = list()
            for i in value:
                self._file_urls.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayOpenAppBizbillBillfileDownloadResponse, self).parse_response_content(response_content)
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'file_urls' in response:
            self.file_urls = response['file_urls']
