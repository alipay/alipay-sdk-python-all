#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.AccessReturnQrcodeResult import AccessReturnQrcodeResult


class KoubeiSalesKbassetStuffQrcodereturnSyncResponse(AlipayResponse):

    def __init__(self):
        super(KoubeiSalesKbassetStuffQrcodereturnSyncResponse, self).__init__()
        self._return_qrcode_results = None

    @property
    def return_qrcode_results(self):
        return self._return_qrcode_results

    @return_qrcode_results.setter
    def return_qrcode_results(self, value):
        if isinstance(value, list):
            self._return_qrcode_results = list()
            for i in value:
                if isinstance(i, AccessReturnQrcodeResult):
                    self._return_qrcode_results.append(i)
                else:
                    self._return_qrcode_results.append(AccessReturnQrcodeResult.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(KoubeiSalesKbassetStuffQrcodereturnSyncResponse, self).parse_response_content(response_content)
        if 'return_qrcode_results' in response:
            self.return_qrcode_results = response['return_qrcode_results']
