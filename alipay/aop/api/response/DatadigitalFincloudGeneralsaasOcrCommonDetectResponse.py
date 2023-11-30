#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class DatadigitalFincloudGeneralsaasOcrCommonDetectResponse(AlipayResponse):

    def __init__(self):
        super(DatadigitalFincloudGeneralsaasOcrCommonDetectResponse, self).__init__()
        self._certify_id = None
        self._ocr_data = None

    @property
    def certify_id(self):
        return self._certify_id

    @certify_id.setter
    def certify_id(self, value):
        self._certify_id = value
    @property
    def ocr_data(self):
        return self._ocr_data

    @ocr_data.setter
    def ocr_data(self, value):
        self._ocr_data = value

    def parse_response_content(self, response_content):
        response = super(DatadigitalFincloudGeneralsaasOcrCommonDetectResponse, self).parse_response_content(response_content)
        if 'certify_id' in response:
            self.certify_id = response['certify_id']
        if 'ocr_data' in response:
            self.ocr_data = response['ocr_data']
