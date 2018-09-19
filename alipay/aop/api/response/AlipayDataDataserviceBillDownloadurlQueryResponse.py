#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataserviceBillDownloadurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataserviceBillDownloadurlQueryResponse, self).__init__()
        self._bill_download_url = None

    @property
    def bill_download_url(self):
        return self._bill_download_url

    @bill_download_url.setter
    def bill_download_url(self, value):
        self._bill_download_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataserviceBillDownloadurlQueryResponse, self).parse_response_content(response_content)
        if 'bill_download_url' in response:
            self.bill_download_url = response['bill_download_url']
