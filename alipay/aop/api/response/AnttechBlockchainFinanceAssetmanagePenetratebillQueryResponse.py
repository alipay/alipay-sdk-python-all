#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AnttechBlockchainFinanceAssetmanagePenetratebillQueryResponse(AlipayResponse):

    def __init__(self):
        super(AnttechBlockchainFinanceAssetmanagePenetratebillQueryResponse, self).__init__()
        self._download_url = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value

    def parse_response_content(self, response_content):
        response = super(AnttechBlockchainFinanceAssetmanagePenetratebillQueryResponse, self).parse_response_content(response_content)
        if 'download_url' in response:
            self.download_url = response['download_url']
