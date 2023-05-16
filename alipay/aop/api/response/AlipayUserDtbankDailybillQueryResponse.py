#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayUserDtbankDailybillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayUserDtbankDailybillQueryResponse, self).__init__()
        self._bill_download_url = None

    @property
    def bill_download_url(self):
        return self._bill_download_url

    @bill_download_url.setter
    def bill_download_url(self, value):
        self._bill_download_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayUserDtbankDailybillQueryResponse, self).parse_response_content(response_content)
        if 'bill_download_url' in response:
            self.bill_download_url = response['bill_download_url']
