#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayEbppMerchantMeterialUploadResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppMerchantMeterialUploadResponse, self).__init__()
        self._md_5 = None

    @property
    def md_5(self):
        return self._md_5

    @md_5.setter
    def md_5(self, value):
        self._md_5 = value

    def parse_response_content(self, response_content):
        response = super(AlipayEbppMerchantMeterialUploadResponse, self).parse_response_content(response_content)
        if 'md_5' in response:
            self.md_5 = response['md_5']
