#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.EduOcrResult import EduOcrResult


class AlipayEbppIndustryEducertifyResultGetResponse(AlipayResponse):

    def __init__(self):
        super(AlipayEbppIndustryEducertifyResultGetResponse, self).__init__()
        self._certify_token = None
        self._ocr_result = None

    @property
    def certify_token(self):
        return self._certify_token

    @certify_token.setter
    def certify_token(self, value):
        self._certify_token = value
    @property
    def ocr_result(self):
        return self._ocr_result

    @ocr_result.setter
    def ocr_result(self, value):
        if isinstance(value, EduOcrResult):
            self._ocr_result = value
        else:
            self._ocr_result = EduOcrResult.from_alipay_dict(value)

    def parse_response_content(self, response_content):
        response = super(AlipayEbppIndustryEducertifyResultGetResponse, self).parse_response_content(response_content)
        if 'certify_token' in response:
            self.certify_token = response['certify_token']
        if 'ocr_result' in response:
            self.ocr_result = response['ocr_result']
