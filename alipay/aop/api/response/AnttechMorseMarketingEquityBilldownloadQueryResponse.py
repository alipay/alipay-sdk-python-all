#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechMorseMarketingEquityBilldownloadQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechMorseMarketingEquityBilldownloadQueryResponse, self).__init__()
        self._file_download_url = None

    @property
    def file_download_url(self):
        return self._file_download_url

    @file_download_url.setter
    def file_download_url(self, value):
        self._file_download_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechMorseMarketingEquityBilldownloadQueryResponse, self).parse_response_content(response_content)
        if 'file_download_url' in response:
            self.file_download_url = response['file_download_url']
