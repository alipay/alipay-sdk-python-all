#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommerceHdfaitransferPictureocrIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommerceHdfaitransferPictureocrIdentifyResponse, self).__init__()
        self._ocr_result = None

    @property
    def ocr_result(self):
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, value):
        self._ocr_result = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommerceHdfaitransferPictureocrIdentifyResponse, self).parse_response_content(response_content)
        if 'ocr_result' in response:
            self.ocr_result = response['ocr_result']
