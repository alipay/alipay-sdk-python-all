#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceLogisticsFreightflowTradereceiptApplyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceLogisticsFreightflowTradereceiptApplyResponse, self).__init__()
        self._pdf_download_url = None

    @property
    def pdf_download_url(self):
        return self._pdf_download_url

    @pdf_download_url.setter
    def pdf_download_url(self, value):
        self._pdf_download_url = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceLogisticsFreightflowTradereceiptApplyResponse, self).parse_response_content(response_content)
        if 'pdf_download_url' in response:
            self.pdf_download_url = response['pdf_download_url']
