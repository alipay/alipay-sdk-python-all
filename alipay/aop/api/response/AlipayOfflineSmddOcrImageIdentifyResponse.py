#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayOfflineSmddOcrImageIdentifyResponse(AlipayResponse):

    def __init__(self):
        super(AlipayOfflineSmddOcrImageIdentifyResponse, self).__init__()
        self._ocr_data = None

    @property
    def ocr_data(self):
        return self._ocr_data

    @ocr_data.setter
    def ocr_data(self, value):
        self._ocr_data = value

    def parse_response_content(self, response_content):
        response = super(AlipayOfflineSmddOcrImageIdentifyResponse, self).parse_response_content(response_content)
        if 'ocr_data' in response:
            self.ocr_data = response['ocr_data']
