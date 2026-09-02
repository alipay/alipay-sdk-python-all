#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayTradeSaasBilldownloadurlQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayTradeSaasBilldownloadurlQueryResponse, self).__init__()
        self._bill_date = None
        self._bill_type = None
        self._download_url = None

    @property
    def bill_date(self):
        return self._bill_date

    @bill_date.setter
    def bill_date(self, value):
        self._bill_date = value
    @property
    def bill_type(self):
        return self._bill_type

    @bill_type.setter
    def bill_type(self, value):
        self._bill_type = value
    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayTradeSaasBilldownloadurlQueryResponse, self).parse_response_content(response_content)
        if 'bill_date' in response:
            self.bill_date = response['bill_date']
        if 'bill_type' in response:
            self.bill_type = response['bill_type']
        if 'download_url' in response:
            self.download_url = response['download_url']
